"""openai_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from iosl.views import script_view
from stocks.views import screen_dropdown, low_pe_view, low_pb_view
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", script_view, name="scripts"),
    path("screens/low_pe", low_pe_view, name="low_pe_view"),
    path("screens/low_pb", low_pb_view, name="low_pb_view"),
    path("", screen_dropdown, name="screen_dropdown"),
    path("tinymce/", include("tinymce.urls")),
    # path("markdownx/", include("markdownx.urls")),
    # path("_nested_admin/", include("nested_admin.urls")),
]

admin.site.site_header = "Diligence Database"
admin.site.site_title = "Diligence"
admin.site.index_title = "Members Only"
# admin.site.site_url = os.environ["CHATPR_SITE_URL"]

# if not os.name == "posix":
if not settings.ON_PYTHONANYWHERE:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

##########################
# For Django Debug Toolbar
if not settings.ON_PYTHONANYWHERE:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)),] + urlpatterns
# urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
##########################
