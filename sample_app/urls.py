from django.conf.urls import url
from django.contrib import admin

# import views
from . import views

urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexTemplateView.as_view(), name='index'),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#     url(r'^articles/([0-9]{4})/$', views.year_archive),
#     url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
#     url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]

