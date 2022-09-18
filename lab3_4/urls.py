from django.contrib import admin
from shop100 import views as shop_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'range', shop_views.RangeViewSet)
router.register(r'models', shop_views.ModelsViewSet)
router.register(r'stock', shop_views.StockViewSet)

router1=routers.DefaultRouter()
# router1.register('types/<int:id>/', shop_views.RangeModelViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('types/', shop_views.RangeViewSet.as_view({'get': 'list'})),
    path('types/<int:idrange>/', shop_views.ModelsViewSet.as_view({'get':'get_models'})),
    path('types/<int:idrange>/', shop_views.ModelsViewSet.as_view({'post':'add_models'})),
]

