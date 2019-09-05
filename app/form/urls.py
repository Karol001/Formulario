from django.conf.urls import url
from app.form.views import countries_view, countries_view1, countries_view2, countries_view3, countries_view4, countries_view5, datos

urlpatterns = [
    url(r'^form$',  datos, name='form'),
    url(r'^form1$', countries_view, name='form1'),
    url(r'^form2$', countries_view1, name='form2'),
    url(r'^form3$', countries_view2, name='form3'),
    url(r'^form4$', countries_view3, name='form4'),
    url(r'^form5$', countries_view4, name='form5'),
    url(r'^form6$', countries_view5, name='form6'),
]