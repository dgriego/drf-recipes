from django.urls import path, include

# feature of DRF that generates appropriate urls for
# all the actions in a viewSet
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
