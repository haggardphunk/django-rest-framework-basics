# Generated by Django 4.0.4 on 2022-04-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=60)),
                ('company_email', models.CharField(max_length=60)),
                ('job_title', models.CharField(max_length=60)),
                ('job_desc', models.TextField(blank=True)),
                ('salary', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
