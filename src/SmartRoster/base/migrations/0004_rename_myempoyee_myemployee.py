# Generated by Django 4.1.4 on 2023-02-03 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_events_patient"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MyEmpoyee",
            new_name="MyEmployee",
        ),
    ]