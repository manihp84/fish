# Generated by Django 5.0.4 on 2024-05-30 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='age',
        ),
        migrations.AddField(
            model_name='emp',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='emp',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
