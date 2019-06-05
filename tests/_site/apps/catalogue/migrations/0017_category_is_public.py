# Generated by Django 2.1.9 on 2019-06-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_auto_20190327_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_public',
            field=models.BooleanField(default=True, help_text='Show this category in search results and catalogue listings.', verbose_name='Is public'),
        ),
    ]
