# Generated by Django 4.2.10 on 2024-02-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameNew', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
                ('textNew', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]