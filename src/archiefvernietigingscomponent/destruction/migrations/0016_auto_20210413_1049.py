# Generated by Django 2.2.18 on 2021-04-13 08:49

from django.db import migrations
from django.db.models import Value
from django.db.models.functions import Replace


def convert_log_templates(apps, schema_editor):
    TimelineLog = apps.get_model("timeline_logger", "TimelineLog")

    TimelineLog.objects.filter(template__endswith=".txt").update(
        template=Replace("template", Value(".txt"), Value(".html"))
    )


class Migration(migrations.Migration):

    dependencies = [
        ("destruction", "0016_archiveconfig_link_to_zac"),
        ("timeline_logger", "0004_alter_fields"),
    ]

    operations = [
        migrations.RunPython(convert_log_templates),
    ]
