from django.urls import path
from .views import CategoryView, user_get_categories
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register('admin/categories', CategoryView)


urlpatterns = router.urls + [
    path('categories/', user_get_categories),
]
