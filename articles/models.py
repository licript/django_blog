from django.db import models
from django.utils import timezone
# Create your models here.


class Articles(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=100, verbose_name="文章标题")
    article_summary = models.CharField(max_length=300, verbose_name="文章摘要")
    article_content = models.TextField(verbose_name="文章内容")
    article_published_date = models.DateTimeField(auto_now=True, verbose_name="发表时间")

    class Meta:
        verbose_name_plural = "文章"


