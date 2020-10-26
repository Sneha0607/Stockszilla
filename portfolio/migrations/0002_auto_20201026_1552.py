# Generated by Django 3.1.2 on 2020-10-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amout',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='gain_loss',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
