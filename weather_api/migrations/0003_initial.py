# Generated by Django 4.1.7 on 2023-02-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('weather_api', '0002_delete_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('met_office_location_id', models.IntegerField()),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
            ],
        ),
    ]
