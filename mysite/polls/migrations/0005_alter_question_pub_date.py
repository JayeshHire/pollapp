# Generated by Django 4.2.4 on 2023-09-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
