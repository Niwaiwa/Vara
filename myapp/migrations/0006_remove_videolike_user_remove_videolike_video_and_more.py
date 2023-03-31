# Generated by Django 4.1.7 on 2023-03-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_video_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videolike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='videolike',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(related_name='TagVideo', to='myapp.tag'),
        ),
        migrations.DeleteModel(
            name='TagVideo',
        ),
        migrations.DeleteModel(
            name='VideoLike',
        ),
    ]
