from django.contrib import admin
from django.urls import path, include

#from course.views import course_list
	
urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('user/', include('login.urls')), #login앱
    path('profile/', include('userinfo.urls')), #userinfo앱
    path('mycollections/', include('mycollections.urls')), #콜렉션
    path('runrecord/', include('runrecord.urls')), 
]

