# Generated by Django 2.1.7 on 2019-04-21 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allObservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(choices=[('Application Security', 'Application Security'), ('Network Review ', 'Network Review')], default='Application Security', max_length=20)),
                ('observation', models.CharField(max_length=200)),
                ('detOb', models.TextField()),
                ('criticality', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='High', max_length=10)),
                ('risk', models.TextField()),
                ('recommendation', models.TextField()),
                ('abbr', models.CharField(max_length=8)),
            ],
        ),
    ]
