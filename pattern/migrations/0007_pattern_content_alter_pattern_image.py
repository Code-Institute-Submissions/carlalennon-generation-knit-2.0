# Generated by Django 4.2.9 on 2024-01-28 21:18

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0006_pattern_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pattern',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='patterns/'),
        ),
    ]
