# Generated by Django 2.2.9 on 2020-09-06 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_shop_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='shop_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shop_name',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='shop_name',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
