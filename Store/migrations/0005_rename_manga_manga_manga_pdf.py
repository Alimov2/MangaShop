# Generated by Django 4.2.4 on 2023-08-12 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_manga_manga'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='manga',
            new_name='manga_pdf',
        ),
    ]
