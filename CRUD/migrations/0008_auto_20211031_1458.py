# Generated by Django 3.2.7 on 2021-10-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0007_auto_20211031_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='a_f_eaf_c_crs_list',
            field=models.CharField(choices=[('CRS', 'CRS'), ('A', 'A'), ('C', 'C'), ('F', 'F'), ('EAF', 'EAF')], max_length=3),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='background_passed',
            field=models.CharField(choices=[('NA', 'NA'), ('F', 'fail'), ('P', 'pass')], max_length=2),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='masters',
            field=models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='adjunctfacultymember',
            name='step_rate',
            field=models.CharField(choices=[('3', 'step 3'), ('2', 'step 2'), ('F', 'faculty'), ('1', 'step 1')], default='step 1', max_length=10),
        ),
    ]