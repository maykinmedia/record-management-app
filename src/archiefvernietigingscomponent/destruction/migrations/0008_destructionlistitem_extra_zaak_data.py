# Generated by Django 2.2.12 on 2021-02-08 13:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("destruction", "0007_auto_20200715_1649"),
    ]

    operations = [
        migrations.AddField(
            model_name="destructionlistitem",
            name="extra_zaak_data",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                help_text="Additional information of the zaak",
                null=True,
                verbose_name="extra zaak data",
            ),
        ),
    ]
