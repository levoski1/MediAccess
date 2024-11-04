# Generated by Django 5.1.2 on 2024-11-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Blog post'},
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default='Default comment body'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='lname',
            field=models.CharField(max_length=40),
        ),
    ]
