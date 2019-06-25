from django.conf.urls import url, include

from rest_framework import routers

from api.views import UserViewSet, PizzaViewSet, ToppingViewSet, PizzaToppingViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'pizza', PizzaViewSet)
router.register(r'toppings', ToppingViewSet)
router.register(r'pizzatoppings', PizzaViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'auth/', include('rest_framework.urls'))
]
