from django import template
register = template.Library()
# cắt chuỗi
@register.filter
def cat_chuoi(value, length=70):
    if len(value) > length:
        return value[:length] + ' ...'
    return value