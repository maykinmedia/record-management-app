# Generated by Django 2.2.12 on 2021-02-18 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import privates.fields
import privates.storages


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DestructionReport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title of the destruction report",
                        max_length=200,
                        verbose_name="title",
                    ),
                ),
                (
                    "content",
                    privates.fields.PrivateMediaFileField(
                        help_text="Content of the destruction report",
                        storage=privates.storages.PrivateMediaFileSystemStorage(),
                        upload_to="reports/%Y/%m/",
                        verbose_name="content",
                    ),
                ),
                (
                    "process_owner",
                    models.ForeignKey(
                        blank=True,
                        help_text="Process owner of the destruction list for which the report was created",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="process owner",
                    ),
                ),
            ],
            options={
                "verbose_name": "Destruction report",
                "verbose_name_plural": "Destruction reports",
            },
        ),
    ]
