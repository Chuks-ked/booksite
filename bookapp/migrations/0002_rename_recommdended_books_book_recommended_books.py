# Generated by Django 4.1.5 on 2023-01-09 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='recommdended_books',
            new_name='recommended_books',
        ),
    ]
