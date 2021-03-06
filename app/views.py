"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def clients(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/clients.html',
        {
            'title':'Clients',
            'message':'Your clients.',
            'year':datetime.now().year,
        }
    )

def caregivers(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/caregivers.html',
        {
            'title':'Caregivers',
            'message':'Your caregivers.',
            'year':datetime.now().year,
        }
    )

def scheduling(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/scheduling.html',
        {
            'title':'Scheduling',
            'message':'Your scheduler.',
            'year':datetime.now().year,
        }
    )

def accounting(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/accounting.html',
        {
            'title':'Accounting',
            'message':'Your accounting.',
            'year':datetime.now().year,
        }
    )

def reports(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/reports.html',
        {
            'title':'Reports',
            'message':'Your reports.',
            'year':datetime.now().year,
        }
    )

def manageoffice(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/manage-office.html',
        {
            'title':'Company Information',
            'message':'Your manage office.',
            'year':datetime.now().year,
        }
    )

def staff(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/staff.html',
        {
            'title':'Staff',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def ratetypes(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/rate-types.html',
        {
            'title':'Rate Types',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def offices(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/offices.html',
        {
            'title':'Offices',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def payrolloptions(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/payroll-options.html',
        {
            'title':'Payroll Options',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def payrollrates(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/payroll-rates.html',
        {
            'title':'Payroll Rates',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def referralmanager(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/referral-manager.html',
        {
            'title':'Referral Manager',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def holidaysetup(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/holiday-setup.html',
        {
            'title':'Holiday Setup',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def billingoptions(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/billing-options.html',
        {
            'title':'Billing Options',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def billingrates(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/billing-rates.html',
        {
            'title':'Billing Rates',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def insurances(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/insurances.html',
        {
            'title':'Insurances',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def billingsetup(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/billing-setup.html',
        {
            'title':'Billing Setup',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def servicetypes(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/service-types.html',
        {
            'title':'Service Types',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def medications(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/medications.html',
        {
            'title':'Medications',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def diagnosis(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/diagnosis.html',
        {
            'title':'Diagnosis',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def taskcodes(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/task-codes.html',
        {
            'title':'Task Codes',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def typesofcare(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/types-of-care.html',
        {
            'title':'Types of Care',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
