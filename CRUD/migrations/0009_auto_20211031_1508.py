# Generated by Django 3.2.7 on 2021-10-31 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0008_auto_20211031_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='a_f_eaf_c_crs_list',
            field=models.CharField(choices=[('C', 'C'), ('F', 'F'), ('EAF', 'EAF'), ('A', 'A'), ('CRS', 'CRS')], max_length=3),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='background_passed',
            field=models.CharField(choices=[('P', 'pass'), ('F', 'fail'), ('NA', 'NA')], max_length=2),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='masters',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='step_rate',
            field=models.CharField(choices=[('2', 'step 2'), ('F', 'faculty'), ('3', 'step 3'), ('1', 'step 1')], default='step 1', max_length=10),
        ),
    ]