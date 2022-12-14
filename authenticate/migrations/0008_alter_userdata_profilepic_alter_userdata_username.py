# Generated by Django 4.1.2 on 2022-10-24 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0007_userdata_profilepic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdata",
            name="profilepic",
            field=models.ImageField(blank=True, upload_to="images"),
        ),
        migrations.AlterField(
            model_name="userdata",
            name="username",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
