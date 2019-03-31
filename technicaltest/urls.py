from django.urls import path

from technicaltest.views import ViewHome, ViewMetaData
from . import api_views


urlpatterns = [
    path('', ViewHome.view_home, name='Home View'),
    path('metadata/', ViewMetaData.view_meta_data, name='Meta Data View'),
    path('api/', api_views.HomeList.as_view(), name='API Home View'),
    path('api/metadata/', api_views.MetaDataList.as_view(), name='API Meta Data View'),
]
