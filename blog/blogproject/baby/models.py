from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime
# Create your models here.

class Age(models.Model):
    name = models.CharField(max_length=100)
    bgurl = models.URLField(blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('baby:babyindex', kwargs={'pk': self.pk})

class Group(models.Model):
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(blank=True, null=True,default=datetime.date.today)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('baby:babyindex', kwargs={'pk': self.pk})
        # 指定排序方式
    class Meta:
        ordering = ['-created_time']

class Picture(models.Model):

    # 图片标题
    title = models.CharField(max_length=70)
    # 图片链接
    picurl = models.URLField()
    tinypicurl = models.URLField()

    # 介绍正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField(blank=True)

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(blank=True, null=True,default=datetime.date.today)
    modified_time = models.DateTimeField(blank=True, null=True,default=datetime.date.today)

    # 这是分类与标签，分类与标签的模型我们已经定义。
    # 我们规定一个图片只能对应一个分类，但是一个分类下可以有多个图片，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    # 如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # 新增 views 字段记录阅读量
    views = models.PositiveIntegerField(default=0)
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    def __str__(self):
        return self.title
    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('baby:detail', kwargs={'pk': self.pk})
    # 指定排序方式
    class Meta:
        ordering = ['-created_time']

