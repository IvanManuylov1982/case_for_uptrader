# Generated by Django 3.2.18 on 2023-02-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('do_menu', '0003_auto_20230222_2117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('order', 'name')},
        ),
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]