# Generated by Django 4.0.3 on 2022-03-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
