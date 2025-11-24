from django.contrib import admin
from django.urls import path
from siteapp import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Landing
    path("", views.language_landing, name="language_landing"),

    # Home pages
    path("en/", views.home_en, name="home_en"),
    path("cy/", views.home_cy, name="home_cy"),

    # English pages
    path("en/info/", views.info_en, name="info_en"),
    path("en/join/", views.join_en, name="join_en"),
    path("en/support/", views.support_en, name="support_en"),

    # Welsh pages
    path("cy/info/", views.info_cy, name="info_cy"),
    path("cy/join/", views.join_cy, name="join_cy"),
    path("cy/support/", views.support_cy, name="support_cy"),

    # Project listings
    path("en/projects/past/", views.projects_past, name="projects_past_en"),
    path("en/projects/present/", views.projects_present, name="projects_present_en"),
    path("en/projects/future/", views.projects_future, name="projects_future_en"),

    path("cy/projects/past/", views.projects_past, name="projects_past_cy"),
    path("cy/projects/present/", views.projects_present, name="projects_present_cy"),
    path("cy/projects/future/", views.projects_future, name="projects_future_cy"),
