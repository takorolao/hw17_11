
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from appname.views import CreateStudent, ListStudents,RetieveStudent, DeleteStudent, UpdateStudent, CourseViewSet

router = DefaultRouter()
router.register('course', CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CreateStudent.as_view(), name = 'students'),
    path('students/', ListStudents.as_view(), name = 'list_students'),
    path('students/<int:pk>', RetieveStudent.as_view(), name = 'list_students'),
    path('delete/<int:pk>', DeleteStudent.as_view(), name = 'delete_students'),
    path('update/<int:pk>', UpdateStudent.as_view(), name = 'update_students'),
    path('api/', include(router.urls))
]
