# Generated by Django 3.0.8 on 2020-11-01 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appsecObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation', models.CharField(max_length=200)),
                ('abbr', models.CharField(max_length=8)),
                ('criticality', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='High', max_length=10)),
                ('detOb', models.TextField()),
                ('risk', models.TextField()),
                ('recommendation', models.TextField()),
                ('comments', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='scrObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation', models.CharField(max_length=200)),
                ('abbr', models.CharField(max_length=8)),
                ('criticality', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='High', max_length=10)),
                ('language', models.CharField(choices=[('Java', 'Java'), ('Python', 'Python')], max_length=10)),
                ('detOb', models.TextField()),
                ('risk', models.TextField()),
                ('recommendation', models.TextField()),
                ('comments', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='vaptObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation', models.CharField(max_length=200)),
                ('abbr', models.CharField(max_length=8)),
                ('criticality', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='High', max_length=10)),
                ('detOb', models.TextField()),
                ('risk', models.TextField()),
                ('recommendation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='vaptPlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pluginID', models.CharField(max_length=20)),
                ('vapt_observation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vaptObservation')),
            ],
        ),
    ]
