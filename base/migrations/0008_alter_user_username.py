# Generated by Django 4.0.2 on 2022-03-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_user_business_only'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
