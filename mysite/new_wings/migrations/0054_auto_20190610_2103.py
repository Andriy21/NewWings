# Generated by Django 2.1.7 on 2019-06-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_wings', '0053_auto_20190604_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='reabil',
            name='title',
            field=models.CharField(help_text='Ведіть назву процедури', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='reabil',
            name='text',
            field=models.TextField(help_text='Ведіть опис процедури', max_length=1000),
        ),
    ]
