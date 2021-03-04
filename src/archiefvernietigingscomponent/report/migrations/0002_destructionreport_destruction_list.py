# Generated by Django 2.2.12 on 2021-02-24 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("destruction", "0008_destructionlistitem_extra_zaak_data"),
        ("report", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="destructionreport",
            name="destruction_list",
            field=models.ForeignKey(
                blank=True,
                help_text="Destruction list for which the report was created.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="destruction.DestructionList",
                verbose_name="destruction list",
            ),
        ),
    ]