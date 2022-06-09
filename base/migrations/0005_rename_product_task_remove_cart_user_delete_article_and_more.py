# Generated by Django 4.0.5 on 2022-06-08 20:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_articletype_publication_article'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Task',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='ArticleType',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
