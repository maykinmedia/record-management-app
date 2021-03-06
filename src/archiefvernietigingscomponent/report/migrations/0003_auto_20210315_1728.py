# Generated by Django 2.2.12 on 2021-03-15 16:28

from django.db import migrations
import privates.fields
import privates.storages


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0002_destructionreport_destruction_list"),
    ]

    operations = [
        migrations.RenameField(
            model_name="destructionreport", old_name="content", new_name="content_pdf"
        ),
        migrations.AddField(
            model_name="destructionreport",
            name="content_csv",
            field=privates.fields.PrivateMediaFileField(
                blank=True,
                help_text="Content of the destruction report in CSV format",
                null=True,
                storage=privates.storages.PrivateMediaFileSystemStorage(),
                upload_to="reports/%Y/%m/",
                verbose_name="content csv",
            ),
        ),
        migrations.AlterField(
            model_name="destructionreport",
            name="content_pdf",
            field=privates.fields.PrivateMediaFileField(
                blank=True,
                help_text="Content of the destruction report in PDF format",
                null=True,
                storage=privates.storages.PrivateMediaFileSystemStorage(),
                upload_to="reports/%Y/%m/",
                verbose_name="content pdf",
            ),
        ),
    ]
