# Generated by Django 5.1.6 on 2025-02-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('head', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('upcoming_events', models.TextField(blank=True, null=True)),
                ('members', models.TextField()),
                ('projects', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
