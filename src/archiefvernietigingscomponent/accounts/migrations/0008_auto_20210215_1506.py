# Generated by Django 2.2.12 on 2021-02-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_set_role_order"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="role",
            options={
                "ordering": ("order",),
                "verbose_name": "role",
                "verbose_name_plural": "roles",
            },
        ),
        migrations.AddField(
            model_name="role",
            name="type",
            field=models.CharField(
                choices=[
                    ("archivist", "Archivist"),
                    ("record_manager", "Record manager"),
                    ("process_owner", "Process owner"),
                    ("functional_admin", "Functional administrator"),
                    ("other", "Other"),
                ],
                default="record_manager",
                help_text="The type of role",
                max_length=255,
                verbose_name="type",
            ),
        ),
    ]
