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