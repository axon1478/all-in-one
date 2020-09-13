from django import template
from django.utils.safestring import mark_safe

from core.models import Category, Order

register = template.Library()


@register.simple_tag
def categories():
    items = Category.objects.filter(is_active=True).order_by('title')
    items_li = ""
    for i in items:
        items_li += """<li><a href="/category/{}">{}</a></li>""".format(i.slug, i.title)
    return mark_safe(items_li)


@register.simple_tag
def categories_mobile():
    items = Category.objects.filter(is_active=True).order_by('title')
    items_li = ""
    for i in items:
        items_li += """<li class="item-menu-mobile"><a href="/category/{}">{}</a></li>""".format(i.slug, i.title)
    return mark_safe(items_li)


@register.simple_tag
def categories_li_a():
    items = Category.objects.filter(is_active=True).order_by('title')
    items_li_a = ""
    for i in items:
        items_li_a += """<li class="p-t-4"><a href="/category/{}" class="s-text13">{}</a></li>""".format(i.slug,
                                                                                                         i.title)
    return mark_safe(items_li_a)


@register.simple_tag
def categories_div():
    """
    section banner
    :return:
    """
    items = Category.objects.filter(is_active=True).order_by('title')
    items_div = ""
    item_div_list = ""
    for i, j in enumerate(items):
        items_div += """<div class="block1 hov-img-zoom pos-relative m-b-30"><img width="500" height="400" src="/media/{}" alt="IMG-BENNER"><div class="block1-wrapbtn w-size2"><a href="/category/{}" class="flex-c-m size2 m-text2 bg3 hov1 trans-0-4">{}</a></div></div>""".format(
            j.image, j.slug, j.title)

        item_div_list += """<div class="col-sm-10 col-md-8 col-lg-4 m-l-r-auto">""" + items_div + """</div>"""
        items_div = ""

    return mark_safe(item_div_list)


