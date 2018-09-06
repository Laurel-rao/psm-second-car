from django import template
register = template.Library()
# 添加过滤器 get_key 和get_attr
# index.html中，首先需要通过标签加载上面定义的过滤器文件 carmodelinfo.py
#    {% load articleinfo %}

# get_key获取字典不同键对应的值
@register.filter
def get_key(d, key_name):
    return d.get(key_name)

#get_attr获取Article对象中不同字段对应的值
@register.filter
def get_attr(d, m):
    if hasattr(d, m):
        return getattr(d, m)