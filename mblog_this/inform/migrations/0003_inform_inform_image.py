# Generated by Django 2.2.11 on 2020-06-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform', '0002_auto_20200617_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='inform',
            name='inform_image',
            field=models.ImageField(blank=True, null=True, upload_to='inform_images', verbose_name='通知图片'),
        ),
    ]
