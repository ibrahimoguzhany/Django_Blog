# Generated by Django 3.1.2 on 2020-11-12 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20201112_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='Makaleye Fotograf Ekleyin'),
        ),
    ]
