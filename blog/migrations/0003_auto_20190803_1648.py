# Generated by Django 2.2.4 on 2019-08-03 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190803_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publishe_date',
            new_name='published_date',
        ),
    ]
