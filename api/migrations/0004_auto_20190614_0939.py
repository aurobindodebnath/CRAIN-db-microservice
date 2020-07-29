# Generated by Django 2.1.7 on 2019-06-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190614_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allobservations',
            name='ptype',
            field=models.CharField(choices=[('Application Security', 'Application Security'), ('Network Architecture Review', 'Network Architecture Review'), ('Vulnerability Assessment', 'Vulnerability Assessment'), ('Mobile Application Security', 'Mobile Application Security')], default='Application Security', max_length=20),
        ),
    ]