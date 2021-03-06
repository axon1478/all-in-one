# Generated by Django 2.2.9 on 2020-09-06 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200906_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shop_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Shop'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='shop_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Shop'),
        ),
    ]
