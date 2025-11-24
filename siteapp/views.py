from django.shortcuts import render
from .models import Project, InfoSection, Resource


def language_landing(request):
    return render(request, "siteapp/landing.html")


def _get_info_sections():
    """
    Helper to fetch Info / Join / Support in one go.
    """
    sections = {obj.key: obj for obj in InfoSection.objects.all()}
    return (
        sections.get("info"),
        sections.get("join"),
        sections.get("support"),
    )


# -----------------------------
# HOME PAGES
# -----------------------------

def home_en(request):
    info_section, join_section, support_section = _get_info_sections()

    context = {
        "language": "en",
        "past_projects": Project.objects.filter(status="past"),
        "present_projects": Project.objects.filter(status="present"),
        "future_projects": Project.objects.filter(status="future"),
        "info_section": info_section,
        "join_section": join_section,
        "support_section": support_section,
        "resources": Resource.objects.all(),
    }
    return render(request, "siteapp/home_en.html", context)


def home_cy(request):
    info_section, join_section, support_section = _get_info_sections()

    context = {
        "language": "cy",
        "past_projects": Project.objects.filter(status="past"),
        "present_projects": Project.objects.filter(status="present"),
        "future_projects": Project.objects.filter(status="future"),
        "info_section": info_section,
        "join_section": join_section,
        "support_section": support_section,
        "resources": Resource.objects.all(),
    }
    return render(request, "siteapp/home_cy.html", context)


# -----------------------------
# PROJECT LIST PAGES (ENGLISH)
# -----------------------------

def projects_past_en(request):
    return render(request, "siteapp/projects_past_en.html", {
        "language": "en",
        "projects": Project.objects.filter(status="past")
    })


def projects_present_en(request):
    return render(request, "siteapp/projects_present_en.html", {
        "language": "en",
        "projects": Project.objects.filter(status="present")
    })


def projects_future_en(request):
    return render(request, "siteapp/projects_future_en.html", {
        "language": "en",
        "projects": Project.objects.filter(status="future")
    })


# -----------------------------
# PROJECT LIST PAGES (WELSH)
# -----------------------------

def projects_past_cy(request):
    return render(request, "siteapp/projects_past_cy.html", {
        "language": "cy",
        "projects": Project.objects.filter(status="past")
    })


def projects_present_cy(request):
    return render(request, "siteapp/projects_present_cy.html", {
        "language": "cy",
        "projects": Project.objects.filter(status="present")
    })


def projects_future_cy(request):
    return render(request, "siteapp/projects_future_cy.html", {
        "language": "cy",
        "projects": Project.objects.filter(status="future")
    })


# -----------------------------
# INFO PAGES
# -----------------------------

def info_en(request):
    info, join, support = _get_info_sections()
    return render(request, "siteapp/info_en.html", {
        "language": "en",
        "title": info.get_title("en") if info else "Info",
        "body": info.get_body("en") if info else "",
    })


def info_cy(request):
    info, join, support = _get_info_sections()
    return render(request, "siteapp/info_cy.html", {
        "language": "cy",
        "title": info.get_title("cy") if info else "Gwybodaeth",
        "body": info.get_body("cy") if info else "",
    })


# -----------------------------
# JOIN PAGES
# -----------------------------

def join_en(request):
    info, join, support = _get_info_sections()
    return render(request, "siteapp/join_en.html", {
        "language": "en",
        "title": join.get_title("en") if join else "Join Us",
        "body": join.get_body("en") if join else "",
    })


def join_cy(request):
    info, join, support = _get_info_sections()
    return render(request, "siteapp/join_cy.html", {
        "language": "cy",
        "title": join.get_title("cy") if join else "Ymuno",
        "body": join.get_body("cy") if join else "",
    })


# -----------------------------
# SUPPORT PAGES
# -----------------------------

def support_en(request):
    info, join, support = _get_info_sections()
    return render(request, "siteapp/support_en.html", {
        "language": "en",
        "title": support.get_title("en") if support else "Support",
        "body": support.get_body("en") if support else "",
        "resources": Resource.objects.all(),
    })


def support_cy(request):
    info, join, support = _get_info_sections()
    return render(request, "siteapp/support_cy.html", {
        "language": "cy",
        "title": support.get_title("cy") if support else "Cefnogi",
        "body": support.get_body("cy") if support else "",
        "resources": Resource.objects.all(),
    })
