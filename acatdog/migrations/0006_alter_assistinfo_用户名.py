# Generated by Django 4.0.4 on 2022-06-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acatdog', '0005_alter_animalinfo_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistinfo',
            name='用户名',
            field=models.CharField(db_column='用户名', default='admin', max_length=20),
        ),
    ]
