from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,CategoryViewSet,ReviewViewSet
from .services.flash_sale import FlashSaleListCreateView,check_flash_sale
from .services.product_view_history import ProductViewHistoryCreate
router = DefaultRouter()
router.register(r"products",ProductViewSet)
router.register(r"reviews",ReviewViewSet)
router.register(r"categories",CategoryViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('sale/',FlashSaleListCreateView.as_view(), name='sale'),
    path('check_sale/<int:product_id>/',check_flash_sale, name='product-view-history-create'),
    path('product-view/',ProductViewHistoryCreate.as_view(), name='product-view-history-create')
]
