# Generated by Django 4.2 on 2024-09-30 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lear_code', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
