# Generated by Django 3.1.3 on 2022-12-20 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='contnet',
            new_name='content',
        ),
    ]
