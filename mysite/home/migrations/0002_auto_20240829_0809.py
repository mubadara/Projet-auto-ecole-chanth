# Generated by Django 3.2.25 on 2024-08-29 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='About',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='About_Chanth',
            new_name='about_Chanth',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='About_Julien',
            new_name='about_Julien',
        ),
        migrations.RenameField(
            model_name='tarif',
            old_name='Formule',
            new_name='formule',
        ),
        migrations.AlterField(
            model_name='tarif',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
