"""
Definition of urls for privateduty.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^clients$', app.views.clients, name='clients'),
    url(r'^caregivers$', app.views.caregivers, name='caregivers'),
    url(r'^scheduling$', app.views.scheduling, name='scheduling'),
    url(r'^accounting$', app.views.accounting, name='accounting'),
    url(r'^reports', app.views.reports, name='reports'),
    url(r'^manage-office', app.views.manageoffice, name='manage-office'),
    url(r'^about', app.views.about, name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
