# Generated by Django 4.0.5 on 2022-06-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0005_rename_product_task_remove_cart_user_delete_article_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
