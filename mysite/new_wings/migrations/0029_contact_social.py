# Generated by Django 2.1.7 on 2019-05-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_wings', '0028_information_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('icon', models.ImageField(null=True, upload_to='image')),
            ],
        ),
    ]
