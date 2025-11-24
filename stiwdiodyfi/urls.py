from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from siteapp import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Landing
    path("", views.language_landing, name="language_landing"),

    # ENGLISH
    path("en/", views.home_en, name="home_en"),
    path("en/info/", views.info_en, name="info_en"),
    path("en/join/", views.join_en, name="join_en"),
    path("en/support/", views.support_en, name="support_en"),

    # PROJECT LISTS (EN)
    path("en/projects/past/", views.projects_past_en, name="projects_past_en"),
    path("en/projects/present/", views.projects_present_en, name="projects_present_en"),
    path("en/projects/future/", views.projects_future_en, name="projects_future_en"),

    # WELSH
    path("cy/", views.home_cy, name="home_cy"),
    path("cy/info/", views.info_cy, name="info_cy"),
    path("cy/join/", views.join_cy, name="join_cy"),
    path("cy/support/", views.support_cy, name="support_cy"),

    # PROJECT LISTS (CY)
    path("cy/projects/past/", views.projects_past_cy, name="projects_past_cy"),
    path("cy/projects/present/", views.projects_present_cy, name="projects_present_cy"),
    path("cy/projects/future/", views.projects_future_cy, name="projects_future_cy"),
]

# MEDIA (needed for development only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
