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

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
