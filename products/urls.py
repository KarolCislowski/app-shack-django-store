from .views import CategoryView, ProductView, user_get_categories, user_get_products
from django.conf.urls import url
from django.urls import path
from .views import CategoryView, user_get_categories
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register('admin/categories', CategoryView)


urlpatterns = router.urls + [
    path('categories/', user_get_categories),
]

router = DefaultRouter(trailing_slash=False)

router.register('admin/categories', CategoryView)
router.register('admin/products', ProductView)


urlpatterns = router.urls + [
    path('categories/', user_get_categories),
    path('products/', user_get_products)
]
