# Generated by Django 4.1.7 on 2023-03-31 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_video_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='taged_videos', to='myapp.tag'),
        ),
    ]
