# Generated by Django 4.1 on 2022-08-19 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlackList_app', '0002_complain'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complain',
            name='bully_id',
            field=models.CharField(max_length=40, verbose_name='Bully ID'),
        ),
    ]
