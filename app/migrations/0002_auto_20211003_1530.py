# Generated by Django 3.2.6 on 2021-10-03 10:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mobile_number',
            field=models.IntegerField(default=91, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Andaman & Nicobar Island', 'Andaman & Nicobar Island'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadar & Nagar Haveli', 'Dadar & Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharakhand', 'Jharakhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], default='----', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('FW', 'Foot Wear'), ('BP', 'Beauty Products'), ('F', 'Furnitures'), ('M', 'Mobiles'), ('L', 'Laptops'), ('C', 'Consoles'), ('EA', 'Electronics Accessories'), ('G', 'Games'), ('TV', 'Televisions'), ('HA', 'Home Appliances')], max_length=2),
        ),
    ]
