# Generated by Django 4.1 on 2023-04-04 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("author", "0002_alter_myuser_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myuser",
            name="birthday",
            field=models.DateField(
                blank=True, null=True, verbose_name="Dia do nascimento"
            ),
        ),
    ]
