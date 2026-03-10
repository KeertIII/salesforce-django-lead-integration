import os
from simple_salesforce import Salesforce

def get_salesforce_connection():
    return Salesforce(
        username=os.getenv("SF_USERNAME"),
        password=os.getenv("SF_PASSWORD"),
        security_token=os.getenv("SF_SECURITY_TOKEN"),
        domain=os.getenv("SF_DOMAIN"),
    )


def create_salesforce_lead(lead):
    sf = get_salesforce_connection()

    response = sf.Lead.create({
        'FirstName': lead.first_name,
        'LastName': lead.last_name,
        'Email': lead.email,
        'Company': lead.company,
        'Phone': lead.phone or '',
        'Rating': lead.lead_status,
        'Lead_Score__c': lead.lead_score,
    })

    return response.get('id')

def calculate_lead_score(lead):
    score = 0

    # Email scoring
    if not lead.email.endswith(("gmail.com", "yahoo.com", "hotmail.com")):
        score += 40
    else:
        score += 15

    # Company name scoring
    if len(lead.company) > 5:
        score += 25

    # Phone provided
    if lead.phone:
        score += 25

    return score

def assign_lead_status(score):
    if score >= 30:
        return "Hot"
    elif score >= 15:
        return "Warm"
    else:
        return "Cold"
    

'''def get_lead_funnel_data():

    sf = Salesforce(
        username=os.getenv("SF_USERNAME"),
        password=os.getenv("SF_PASSWORD"),
        security_token=os.getenv("SF_SECURITY_TOKEN")
    )

    report_id = os.getenv("SF_LEAD_REPORT_ID")

    result = sf.restful(f'analytics/reports/{report_id}')

    #data = result["factMap"]["T!T"]["rows"]
    factmap = result["factMap"]
    rows = list(factmap.values())[0]["rows"]

    labels = []
    values = []

    for row in rows: #data:
        labels.append(row["dataCells"][0]["label"])
        values.append(row["dataCells"][1]["value"])

    return {
        "labels": labels,
        "values": values
    }'''


def get_lead_funnel_data():

    sf = Salesforce(
        username=os.getenv("SF_USERNAME"),
        password=os.getenv("SF_PASSWORD"),
        security_token=os.getenv("SF_SECURITY_TOKEN")
    )

    report_id = os.getenv("SF_LEAD_REPORT_ID")

    result = sf.restful(f'analytics/reports/{report_id}')

    groupings = result["groupingsDown"]["groupings"]

    labels = []
    values = []

    for group in groupings:
        labels.append(group["label"])

        key = group["key"]
        count = result["factMap"][f"{key}!T"]["aggregates"][0]["value"]

        values.append(count)

    return {
        "labels": labels,
        "values": values
    }