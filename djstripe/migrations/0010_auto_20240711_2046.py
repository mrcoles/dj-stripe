# Generated by Django 2.2.16 on 2024-07-11 20:46

from django.db import migrations
import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0009_auto_20220520_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentintent',
            name='capture_method',
            field=djstripe.fields.StripeEnumField(enum=djstripe.enums.CaptureMethod, help_text='Capture method of this PaymentIntent, one of automatic or manual.', max_length=15),
        ),
    ]
