# Generated by Django 4.1.2 on 2022-10-23 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0003_tasks_task_description"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Tasks",
        ),
    ]
