# Generated by Django 4.0.4 on 2022-06-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acatdog', '0006_alter_assistinfo_用户名'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistinfo',
            name='是否可被领养',
            field=models.CharField(max_length=10),
        ),
    ]
