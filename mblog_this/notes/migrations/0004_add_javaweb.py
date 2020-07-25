# Generated by Django 3.0 on 2020-03-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20200316_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='type',
            field=models.CharField(choices=[('Python', 'Python'), ('Django', 'Django'), ('Java', 'Java'), ('Scrapy', 'Scrapy'), ('Pandas', 'Pandas'), ('Numpy', 'Numpy'), ('Layui', 'Layui'), ('English', 'English'), ('machine_learning', 'machine_learning'), ('C#', 'C#'), ('C++', 'C++'), ('Linux', 'Linux'), ('Mysql', 'Mysql'), ('Leetcode', 'Leetcode'), ('Cmd', 'Cmd'), ('jquery', 'jquery'), ('个人信息', '个人信息'), ('Celery', 'Celery'), ('Pyecharts', 'Pyecharts'), ('javaScripts', 'javaScripts'), ('Restful Api', 'Restful Api'), ('Flask', 'Flask'), ('深度学习', '深度学习'), ('Redis', 'Redis'), ('Mongodb', 'Mongodb'), ('Spring', 'Spring'), ('Oracle', 'Oracle'), ('Javaweb', 'Javaweb')], help_text='选择记录的笔记类型', max_length=20, verbose_name='笔记类型'),
        ),
    ]
