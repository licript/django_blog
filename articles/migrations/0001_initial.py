# Generated by Django 2.2 on 2019-04-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('article_summary', models.CharField(max_length=300, verbose_name='文章摘要')),
                ('article_content', models.TextField(verbose_name='文章内容')),
                ('article_published_date', models.DateTimeField(auto_now=True, verbose_name='发表时间')),
            ],
            options={
                'verbose_name_plural': '文章',
            },
        ),
    ]