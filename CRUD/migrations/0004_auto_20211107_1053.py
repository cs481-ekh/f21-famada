# Generated by Django 3.2.9 on 2021-11-07 17:53

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0003_auto_20211025_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='a_f_eaf_c_crs_list',
            field=models.CharField(choices=[('CRS', 'CRS'), ('A', 'A'), ('F', 'F'), ('EAF', 'EAF'), ('C', 'C')], max_length=3),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='background_passed',
            field=models.CharField(choices=[('P', 'pass'), ('NA', 'NA'), ('F', 'fail')], max_length=2),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='cv_resume',
            field=models.IntegerField(help_text='please enter a 4 digit year'),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='primary_phone',
            field=phone_field.models.PhoneField(max_length=31),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='secondary_phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='semester',
            field=models.CharField(help_text='please enter SP, FA, or SU followed by a 2 digit year. (ex. SP21)', max_length=4),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='step_rate',
            field=models.CharField(choices=[('F', 'faculty'), ('1', 'step 1'), ('2', 'step 2'), ('3', 'step 3')], default='step 1', max_length=10),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='zip',
            field=models.IntegerField(help_text='please enter a 5 digit zipcode'),
        ),
    ]
