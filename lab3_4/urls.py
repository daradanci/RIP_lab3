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
    # path('types/', include(router1.urls), name='type_url'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]