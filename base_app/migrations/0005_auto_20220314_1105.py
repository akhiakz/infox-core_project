# Generated by Django 3.2.12 on 2022-03-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_auto_20220314_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='expqr',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='offerqr',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='relieveqr',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
