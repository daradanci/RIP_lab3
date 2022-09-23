from django.contrib import admin
from shop100 import views as shop_views
from django.urls import include, path
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'range', shop_views.RangeViewSet)
router.register(r'models', shop_views.ModelsViewSet, basename='models')
router.register(r'stock', shop_views.StockViewSet)

type_router=routers.DefaultRouter()
type_router.register(r'types', shop_views.RangeViewSet)

models_router=routers.NestedDefaultRouter(type_router, r'types', lookup='types')
models_router.register(r'models', shop_views.ModelsOfTypeViewSet, basename='models-of-type')

stock_router=routers.NestedDefaultRouter(models_router, r'models', lookup='models')
stock_router.register(r'stock', shop_views.StockOfModelViewSet, basename='stock-of-model')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(type_router.urls)),
    path('', include(models_router.urls)),
    path('', include(stock_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # path('types/', shop_views.RangeViewSet.as_view({'get': 'list'})),

    # path('types/<int:idrange>/', shop_views.ModelsViewSet.as_view({'post': 'add_models'})),

    # path('types/<int:idrange>/', shop_views.ModelsViewSet.as_view({'get': 'get_models'})),


]



