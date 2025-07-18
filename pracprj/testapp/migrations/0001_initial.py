# Generated by Django 5.2.4 on 2025-07-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_name', models.TextField(max_length=100)),
                ('Emp_address', models.TextField(max_length=200)),
                ('Emp_department', models.CharField(choices=[('HR', 'Human Resource'), ('SL', 'Sales'), ('FN', 'Finance'), ('TH', 'Technical')], default='Sales', max_length=50)),
                ('Emp_profile', models.ImageField(upload_to='emp_prf_img/')),
            ],
        ),
    ]
