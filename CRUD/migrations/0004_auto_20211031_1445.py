# Generated by Django 3.2.7 on 2021-10-31 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0003_auto_20211028_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='a_f_eaf_c_crs_list',
            field=models.CharField(choices=[('EAF', 'EAF'), ('CRS', 'CRS'), ('C', 'C'), ('A', 'A'), ('F', 'F')], max_length=3),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='background_passed',
            field=models.CharField(choices=[('NA', 'NA'), ('P', 'pass'), ('F', 'fail')], max_length=2),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='masters',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=3),
        ),
    ]
