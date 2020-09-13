from django.urls import path
from .views import (
    ItemDetailView,
    HomeView,
    add_to_cart,
    add_to_cart_cate,
    add_to_cart_det,
    add_to_cart_shop,
    remove_from_cart,
    ShopView,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    CategoryView,
    AccountView,
    CashOnDeliveryView,

    ContactView,

    SearchView)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('account/', AccountView.as_view(), name='account'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-to-cart-cate/<slug>/', add_to_cart_cate, name='add-to-cart-cate'),
    path('add-to-cart-shop/<slug>/', add_to_cart_shop, name='add-to-cart-shop'),
    path('add-to-cart-det/<slug>/', add_to_cart_det, name='add-to-cart-det'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('search/', SearchView, name='search'),

    path('contact/', ContactView, name='contact'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('cod/<payment_option>/', CashOnDeliveryView.as_view(), name='cod'),
    path('request-refund/<str:ref_code>', RequestRefundView.as_view(), name='request-refund')
]
