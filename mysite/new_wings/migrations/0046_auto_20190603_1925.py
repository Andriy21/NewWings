# Generated by Django 2.1.7 on 2019-06-03 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_wings', '0045_auto_20190601_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suport',
            name='city',
            field=models.TextField(max_length=200, verbose_name='Місце проживання'),
        ),
        migrations.AlterField(
            model_name='suport',
            name='reabil_type',
            field=models.CharField(max_length=100, verbose_name='Вид реабілітації'),
        ),
    ]
