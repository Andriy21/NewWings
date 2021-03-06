# Generated by Django 2.1.7 on 2019-05-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_wings', '0039_remove_new_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuportForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=50)),
                ('trade', models.CharField(max_length=150)),
                ('problem', models.CharField(max_length=200)),
                ('live_through', models.CharField(max_length=200)),
                ('real_problem', models.CharField(max_length=200)),
                ('recent_treatment', models.CharField(max_length=200)),
                ('exemption', models.CharField(max_length=150)),
            ],
        ),
    ]
