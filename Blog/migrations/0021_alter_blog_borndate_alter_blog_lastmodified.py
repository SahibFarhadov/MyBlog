# Generated by Django 4.2.2 on 2023-07-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0020_blog_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='borndate',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Yaranma tarixi'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='lastmodified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Sonuncu deyişiklik tarixi'),
        ),
    ]