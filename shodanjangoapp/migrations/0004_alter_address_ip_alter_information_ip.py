# Generated by Django 4.1.5 on 2023-02-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shodanjangoapp', '0003_address_alter_information_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='information',
            name='ip',
            field=models.GenericIPAddressField(default='', primary_key=True, serialize=False),
        ),
    ]