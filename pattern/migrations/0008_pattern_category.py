# Generated by Django 4.2.9 on 2024-01-28 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0007_pattern_content_alter_pattern_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='category',
            field=models.IntegerField(choices=[(0, ''), (1, 'Sweater'), (2, 'Cardigan'), (3, 'Skirt'), (4, 'Pants'), (5, 'Hat'), (6, 'Scarf')], default=0),
        ),
    ]
