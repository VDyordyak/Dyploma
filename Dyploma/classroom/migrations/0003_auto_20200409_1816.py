# Generated by Django 2.2.7 on 2020-04-09 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_quiz_type_of_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='code_text',
            field=models.CharField(default=0, max_length=1000, verbose_name='Answer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='correct_text',
            field=models.CharField(default=0, max_length=255, verbose_name='Answer'),
            preserve_default=False,
        ),
    ]