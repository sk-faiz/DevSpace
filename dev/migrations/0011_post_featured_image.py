# Generated by Django 4.1.3 on 2023-02-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0010_remove_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
