# Generated by Django 4.1.5 on 2023-01-28 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answermodel',
            name='feel',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answermodel',
            name='role',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
