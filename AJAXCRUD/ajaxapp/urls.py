from django.contrib import admin
from django.urls import path
from ajaxapp import views
from django.conf import settings  
from django.conf.urls.static import static  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('insert/',views.insert_data,name='insert'),
    path('delete/',views.delete_user,name='delete'),
    path('update/',views.updatedata,name='update'),
    path('updateuser/',views.update_user,name='updateuser'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
