# Generated by Django 2.2.3 on 2019-07-29 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_contents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='contents',
            new_name='content',
        ),
    ]
