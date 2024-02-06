# Generated by Django 4.2.9 on 2024-02-06 21:13

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='user-temp.png', upload_to='profiles/'),
        ),
    ]
