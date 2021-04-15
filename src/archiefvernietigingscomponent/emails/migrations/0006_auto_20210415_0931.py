# Generated by Django 2.2.18 on 2021-04-15 07:31

from django.db import migrations


def add_email_preferences_for_old_users(apps, schema_editor):
    User = apps.get_model("accounts", "User")
    EmailPreference = apps.get_model("emails", "EmailPreference")

    for existing_user in User.objects.all():
        if not EmailPreference.objects.filter(user=existing_user).exists():
            EmailPreference.objects.create(user=existing_user)


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0005_emailconfig_from_email"),
        ("accounts", "0008_auto_20210215_1506"),
    ]

    operations = [
        migrations.RunPython(add_email_preferences_for_old_users),
    ]
