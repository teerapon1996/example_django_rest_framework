from rest_framework import routers
from django.conf.urls import include,url
from rest_framework.routers import DefaultRouter
from student import views

router = routers.DefaultRouter()
router.register('student', views.StudentViewSet)
router.register('school', views.SchoolViewSet)

urlpatterns = router.urls