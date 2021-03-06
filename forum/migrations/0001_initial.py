# Generated by Django 4.0.4 on 2022-06-08 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlePost', models.CharField(max_length=50)),
                ('contentPost', models.TextField()),
                ('datePost', models.DateTimeField(auto_now=True)),
                ('lastModificationPost', models.DateTimeField(auto_now=True)),
                ('slugPost', models.SlugField(blank=True)),
                ('authorPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentComment', models.TextField(max_length=1000)),
                ('commentAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.posts')),
            ],
        ),
    ]
