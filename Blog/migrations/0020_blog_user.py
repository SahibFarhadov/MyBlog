# Generated by Django 4.2.2 on 2023-07-12 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_initial'),
        ('Blog', '0019_alter_blog_lastmodified_alter_blog_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Account.myuser'),
        ),
    ]
