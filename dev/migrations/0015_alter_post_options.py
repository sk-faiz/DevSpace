# Generated by Django 4.1.3 on 2023-03-26 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0014_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-vote_ratio', '-vote_count', '-created_at']},
        ),
    ]