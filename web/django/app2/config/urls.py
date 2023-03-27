from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("where/", include("where.urls")),
    path("users/", include("users.urls")),
    path("where/", include("where.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("apis/", include("apis.urls")),
]
