from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from . import views

urlpatterns = [

	url(r'^$', views.home, name='home'),
    url(r'^table_list', views.table_list, name='table_list'),
    url(r'^information$', views.information, name='information'),
    url(r'^menu$', views.menu, name='menu'),
    url(r'^stock$', views.stock, name='stock'),
	url(r'^date_input$', views.date_input, name='date_input'),
	url(r'^send_mail$', views.send_mail, name='send_mail'),
    #url(r'^сancel$', views.cancel, name='cancel'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
