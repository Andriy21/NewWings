# Generated by Django 2.1.7 on 2019-05-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_wings', '0024_auto_20190513_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='screen',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]