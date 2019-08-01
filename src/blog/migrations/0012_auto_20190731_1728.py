# Generated by Django 2.2.3 on 2019-07-31 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190730_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='timp_stamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]