from django.urls import path, include
from profiles import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')


urlpatterns = [
    path('home/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
    #path('', views.HelloViewSet.as_view({'get': 'list'})),
]