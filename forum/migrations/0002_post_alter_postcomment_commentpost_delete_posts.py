# Generated by Django 4.0.4 on 2022-06-08 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlePost', models.CharField(max_length=50)),
                ('contentPost', models.TextField()),
                ('datePost', models.DateTimeField(auto_now=True)),
                ('lastModificationPost', models.DateTimeField(auto_now=True)),
                ('authorPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='commentPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.post'),
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]