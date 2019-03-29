from django.urls import path

from . import views
from . import api_views


urlpatterns = [
    path('', views.view_home, name='Home View'),
    path('about/', views.view_meta_data, name='Meta Data View'),
    path('api/home/', api_views.HomeList.as_view(), name='API Home View'),
    path('api/metadata/', api_views.MetaDataList.as_view(), name='Meta Data View'),
]
