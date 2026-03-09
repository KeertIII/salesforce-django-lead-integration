# Salesforce Lead Automation with Django

## Project Overview
This project demonstrates a real-world integration between a Django web application and Salesforce CRM.

Users submit lead information through a Django web form. The application calculates a lead score and sends the lead to Salesforce using the Salesforce REST API. Salesforce automation then assigns the lead to the appropriate sales representative.

---

## Tech Stack

Backend
- Python
- Django

Integration
- Salesforce REST API
- simple-salesforce

Automation
- Salesforce Flow

Tools
- Git
- GitHub
- python-dotenv

---

## Features

Lead Capture Form  
Users can submit lead information through a Django interface.

Lead Scoring Logic  
The system automatically calculates a lead score.

Salesforce Integration  
Leads are created in Salesforce using API integration.

Automated Lead Routing  
Salesforce Flow assigns leads based on score.

Secure Credentials  
Environment variables store sensitive credentials.

---

## Project Architecture

User submits form  
↓  
Django processes request  
↓  
Lead score calculated  
↓  
Salesforce API creates Lead  
↓  
Salesforce Flow triggered  
↓  
Lead Owner assigned automatically

---


## Lead Scoring Logic

The system calculates a lead score based on key information provided in the form.

### Scoring Rules

- Business Email (non-gmail/yahoo/hotmail) → **+40**
- Personal Email (gmail/yahoo/hotmail) → **+15**
- Company Name Length > 5 → **+25**
- Phone Number Provided → **+25**

### Lead Assignment Logic

The calculated score helps determine lead priority and enables automatic routing to the appropriate users inside Salesforce.
Higher scoring leads are prioritized for faster follow-up..

---

## Installation

Clone repository

git clone https://github.com/KeertIII/salesforce-django-lead-integration.git

Navigate to project

cd salesforce-django-lead-integration

Create virtual environment

python -m venv venv

Activate environment

Windows:
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run server

python manage.py runserver

---

## Environment Variables

Create a `.env` file:

SF_USERNAME=your_salesforce_username  
SF_PASSWORD=your_salesforce_password  
SF_SECURITY_TOKEN=your_security_token  

---

## Future Improvements

Duplicate lead detection  
AI lead scoring  
Lead conversion automation

---

## Author

Keerti Pandey
Aspiring Salesforce Developer
