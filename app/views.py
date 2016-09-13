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
            'title':'Manage Office',
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
            'title':'Manage Office Staff',
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
            'title':'Manage Office Staff',
            'message':'Your manage office staff.',
            'year':datetime.now().year,
        }
    )

def payrollsetup(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/payroll-setup.html',
        {
            'title':'Manage Office Staff',
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
            'title':'Manage Office Staff',
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
            'title':'Manage Office Staff',
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
            'title':'Manage Office Staff',
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
            'title':'Manage Office Staff',
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
            'title':'Manage Office Staff',
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
            'title':'Manage Office Staff',
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
            'title':'About',
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
            'title':'About',
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
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
