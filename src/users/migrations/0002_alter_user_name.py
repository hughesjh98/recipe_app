# Generated by Django 4.2.5 on 2023-09-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(help_text='please enter your name....', max_length=30),
        ),
    ]
