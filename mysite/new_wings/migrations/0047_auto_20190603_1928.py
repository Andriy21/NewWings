# Generated by Django 2.1.7 on 2019-06-03 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_wings', '0046_auto_20190603_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suport',
            name='age',
            field=models.IntegerField(max_length=50, verbose_name='ваш вік'),
        ),
    ]