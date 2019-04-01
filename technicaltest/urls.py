"""
This module redirects the request to corrosponding view.
"""


from django.urls import path

from technicaltest.views import ViewHome, ViewMetaData
from . import api_views


urlpatterns = [
    path('', ViewHome.view_home, name='Home View'),
    path('metadata/', ViewMetaData.view_meta_data, name='Meta Data View'),
    path('api/', api_views.HomeApiView.as_view(), name='Home API View'),
    path('api/metadata/', api_views.MetaDataApiView.as_view(), name='Meta Data API View'),
]
