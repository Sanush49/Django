# Generated by Django 2.2.3 on 2019-07-31 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190731_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='timp_stamp',
            new_name='timestamp',
        ),
    ]
