# Generated by Django 3.2.6 on 2021-10-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='title',
            field=models.CharField(default='Product Name', max_length=100),
        ),
    ]
