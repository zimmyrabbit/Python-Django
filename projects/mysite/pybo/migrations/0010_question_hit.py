# Generated by Django 3.1.3 on 2023-01-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_question_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]