# Generated by Django 4.2.3 on 2023-12-25 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Add your title tag', max_length=255),
        ),
    ]