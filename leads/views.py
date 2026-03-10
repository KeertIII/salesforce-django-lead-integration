from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import LeadForm
from .services import create_salesforce_lead, calculate_lead_score, assign_lead_status, get_lead_funnel_data


def create_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            lead=form.save()

            score = calculate_lead_score(lead)
            status = assign_lead_status(score)

            lead.lead_score = score
            lead.lead_status = status
            lead.save()

            sf_id = create_salesforce_lead(lead)
            lead.salesforce_id = sf_id
            lead.save()

            return redirect('success')
    else:
        form = LeadForm()

    return render(request, 'create_lead.html', {'form': form})


def success(request):
    return render(request, 'success.html')


# loads dashboard page
def dashboard(request):
    return render(request, "dashboard.html")


# returns chart data
def dashboard_data(request):
    data = get_lead_funnel_data()
    return JsonResponse(data)