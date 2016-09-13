# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 00:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('agency_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100, null=True)),
                ('primary_contact_name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=50, null=True)),
                ('address2', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('office_number', models.CharField(max_length=15, null=True)),
                ('other_number', models.CharField(max_length=15, null=True)),
                ('fax', models.CharField(max_length=15, null=True)),
                ('created_date', models.DateField()),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('modified_date', models.DateField(null=True)),
                ('modified_by', models.CharField(max_length=50, null=True)),
                ('longitude', models.CharField(max_length=50, null=True)),
                ('latitude', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Caregiver',
            fields=[
                ('caregiver_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('employee_id', models.CharField(max_length=50, null=True)),
                ('ssn', models.CharField(max_length=9, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('height', models.CharField(max_length=10, null=True)),
                ('weight', models.CharField(max_length=10, null=True)),
                ('address1', models.CharField(max_length=50, null=True)),
                ('address2', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('home_number', models.CharField(max_length=15, null=True)),
                ('mobile_number', models.CharField(max_length=15, null=True)),
                ('office_number', models.CharField(max_length=15, null=True)),
                ('fax', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('hire_date', models.DateField(null=True)),
                ('termination_date', models.DateField(null=True)),
                ('status_date', models.DateField(null=True)),
                ('status_note', models.CharField(max_length=400, null=True)),
                ('created_date', models.DateField()),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('modified_date', models.DateField(null=True)),
                ('modified_by', models.CharField(max_length=50, null=True)),
                ('longitude', models.CharField(max_length=50, null=True)),
                ('latitude', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('client_acct_number', models.CharField(max_length=15, null=True)),
                ('ssn', models.CharField(max_length=9, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('height', models.CharField(max_length=10, null=True)),
                ('weight', models.CharField(max_length=10, null=True)),
                ('address1', models.CharField(max_length=50, null=True)),
                ('address2', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('home_number', models.CharField(max_length=15, null=True)),
                ('mobile_number', models.CharField(max_length=15, null=True)),
                ('office_number', models.CharField(max_length=15, null=True)),
                ('fax', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('start_of_care', models.DateField(null=True)),
                ('status_date', models.DateField(null=True)),
                ('status_note', models.CharField(max_length=400, null=True)),
                ('created_date', models.DateField()),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('modified_date', models.DateField(null=True)),
                ('modified_by', models.CharField(max_length=50, null=True)),
                ('longitude', models.CharField(max_length=50, null=True)),
                ('latitude', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField(default=1)),
                ('care_manager_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListAgencyType',
            fields=[
                ('agency_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('agency_type', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ListClientStatus',
            fields=[
                ('client_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_status', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ListEmployeeType',
            fields=[
                ('employee_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_type', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ListEthnicity',
            fields=[
                ('ethnicity_id', models.AutoField(primary_key=True, serialize=False)),
                ('ethnicity', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ListLanguage',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ListMaritalStatus',
            fields=[
                ('marital_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('marital_status', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ListReligion',
            fields=[
                ('religion_id', models.AutoField(primary_key=True, serialize=False)),
                ('religion', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ListStaffStatus',
            fields=[
                ('staff_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_status', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ListTimeZone',
            fields=[
                ('time_zone_id', models.AutoField(primary_key=True, serialize=False)),
                ('time_zone', models.CharField(max_length=50)),
                ('system_default', models.BooleanField(default=0)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ReferralCompany',
            fields=[
                ('referral_company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100, null=True)),
                ('address1', models.CharField(max_length=50, null=True)),
                ('address2', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('office_number', models.CharField(max_length=15, null=True)),
                ('other_number', models.CharField(max_length=15, null=True)),
                ('fax', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('created_date', models.DateField()),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('modified_date', models.DateField(null=True)),
                ('modified_by', models.CharField(max_length=50, null=True)),
                ('longitude', models.CharField(max_length=50, null=True)),
                ('latitude', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ReferralContact',
            fields=[
                ('referral_contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=100, null=True)),
                ('address1', models.CharField(max_length=50, null=True)),
                ('address2', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('office_number', models.CharField(max_length=15, null=True)),
                ('other_number', models.CharField(max_length=15, null=True)),
                ('fax', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('created_date', models.DateField()),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('modified_date', models.DateField(null=True)),
                ('modified_by', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField(default=1)),
                ('referral_company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ReferralCompany')),
            ],
        ),
        migrations.CreateModel(
            name='ReferralType',
            fields=[
                ('referral_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('referral_type', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_id', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('ssn', models.CharField(max_length=9, null=True)),
                ('dob', models.DateField(null=True)),
                ('address1', models.CharField(max_length=50, null=True)),
                ('address2', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('home_phone', models.CharField(max_length=15, null=True)),
                ('mobile_phone', models.CharField(max_length=15, null=True)),
                ('hire_date', models.DateField(null=True)),
                ('termination_date', models.DateField(null=True)),
                ('status_date', models.DateField(null=True)),
                ('status_note', models.CharField(max_length=400, null=True)),
                ('created_date', models.DateField()),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('modified_date', models.DateField(null=True)),
                ('modified_by', models.CharField(max_length=50, null=True)),
                ('velocicare_admin', models.BooleanField(default=0)),
                ('active', models.BooleanField(default=1)),
                ('employee_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListEmployeeType')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListLanguage')),
                ('staff_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListStaffStatus')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='referralcompany',
            name='referral_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ReferralType'),
        ),
        migrations.AddField(
            model_name='client',
            name='client_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListClientStatus'),
        ),
        migrations.AddField(
            model_name='client',
            name='ethnicity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListEthnicity'),
        ),
        migrations.AddField(
            model_name='client',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListLanguage'),
        ),
        migrations.AddField(
            model_name='client',
            name='marital_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListMaritalStatus'),
        ),
        migrations.AddField(
            model_name='client',
            name='referral_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ReferralCompany'),
        ),
        migrations.AddField(
            model_name='client',
            name='referral_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ReferralContact'),
        ),
        migrations.AddField(
            model_name='client',
            name='religion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListReligion'),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='employee_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListEmployeeType'),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='ethnicity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListEthnicity'),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListLanguage'),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='marital_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListMaritalStatus'),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='referral_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ReferralCompany'),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='referral_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ReferralContact'),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='religion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListReligion'),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='staff_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListStaffStatus'),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='supervisor_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agency',
            name='time_zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ListTimeZone'),
        ),
    ]
