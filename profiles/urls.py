from django.urls import path, include
from profiles import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profiles', views.UserProfileViewSet)


urlpatterns = [
    path('home/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
    #path('', views.HelloViewSet.as_view({'get': 'list'})),
]