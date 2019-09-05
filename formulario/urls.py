from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from app.form import views
from django.conf import settings 


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.datos, name='datos'),
    url(r'^form/', include(('app.form.urls', 'form1'), namespace="form1")),
    url(r'^form1/', include(('app.form.urls', 'form2'), namespace="form2")),
    url(r'^form2/', include(('app.form.urls', 'form3'), namespace="form3")),
    url(r'^form3/', include(('app.form.urls', 'form4'), namespace="form4")),
    url(r'^form4/', include(('app.form.urls', 'form5'), namespace="form5")),
    url(r'^form5/', include(('app.form.urls', 'form6'), namespace="form6")),
   
]