"""platform_enablement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from technicaltest.helper.application_response_handler import ApplicationResponseHandler

handler200 = ApplicationResponseHandler.response_handler_200
handler204 = ApplicationResponseHandler.response_handler_204
handler400 = ApplicationResponseHandler.response_handler_400
handler403 = ApplicationResponseHandler.response_handler_403
handler404 = ApplicationResponseHandler.response_handler_404
handler405 = ApplicationResponseHandler.response_handler_405
handler408 = ApplicationResponseHandler.response_handler_408
handler429 = ApplicationResponseHandler.response_handler_429
handler500 = ApplicationResponseHandler.response_handler_500
handler501 = ApplicationResponseHandler.response_handler_501
handler502 = ApplicationResponseHandler.response_handler_502
handler503 = ApplicationResponseHandler.response_handler_503
handler504 = ApplicationResponseHandler.response_handler_504


urlpatterns = [
    path('', include('technicaltest.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
