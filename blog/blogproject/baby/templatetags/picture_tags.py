from django import template
from ..models import Picture, Age, Group

register = template.Library()

# # 获取最新文章
# @register.simple_tag
# def get_recent_pictures(num=3):
#     return Picture.objects.all().order_by('-created_time')[:num]

# 分类模板标签
@register.simple_tag
def get_ages():
    return Age.objects.all()

# @register.simple_tag
# def get_recent_group():
#     return Group.objects.latest('created_time')

# @register.simple_tag
# def get_pic_by_group(group):
#     return Age.objects.filter(group=group)