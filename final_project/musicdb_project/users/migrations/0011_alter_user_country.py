# Generated by Django 3.2.9 on 2021-12-03 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(default='United States', max_length=50),
        ),
    ]
