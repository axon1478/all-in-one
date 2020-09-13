from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, BillingAddress, Category, Slide, UserProfile



# Register your models here.


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'



class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'billing_address',
                    'ordered',
                    'payment_received',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'coupon',
                    ]
    list_display_links = [
        'user',
        'billing_address',
        'coupon',
    ]
    list_filter = [
                   'ordered',
                   'payment_received',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted',
                  ]
    search_fields = [
        'user__username',
        'user__email',
        'ref_code',

    ]
    actions = [make_refund_accepted]



class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'street_address',
        'apartment_address',
        'Pin_Code',
        'default',

    ]
    list_filter = ['default', 'Pin_Code']
    search_fields = ['name', 'street_address', 'apartment_address', 'Pin_Code']



def copy_items(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


copy_items.short_description = 'Copy Items'


class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
    ]
    list_filter = ['title', 'category']
    search_fields = ['title', 'category']
    prepopulated_fields = {"slug": ("title",)}
    actions = [copy_items]

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active'
    ]
    list_filter = ['title', 'is_active']
    search_fields = ['title', 'is_active']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slide)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(UserProfile)

admin.site.register(BillingAddress, AddressAdmin)
