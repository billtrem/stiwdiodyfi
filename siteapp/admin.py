from django.contrib import admin
from django.utils.html import format_html
from .models import Project, InfoSection, Resource


# ---------------------------------------------------------
# HELPERS
# ---------------------------------------------------------

def image_preview(obj, field_name):
    """Creates a thumbnail preview in Django admin."""
    if not obj:
        return "(no image)"

    field = getattr(obj, field_name, None)
    if not field:
        return "(no image)"

    try:
        url = field.url
    except Exception:
        return "(no image)"

    return format_html(
        '<img src="{}" style="height:60px;border-radius:4px;object-fit:cover;">',
        url
    )


# ---------------------------------------------------------
# PROJECT ADMIN
# ---------------------------------------------------------

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title_en",
        "status",
        "published_at",
        "slug",
        "poster_preview",
    )

    list_filter = ("status", "published_at")
    search_fields = ("title_en", "title_cy", "description_en", "description_cy")
    ordering = ("-published_at",)

    readonly_fields = (
        "slug",
        "poster_preview",
        "leader1_preview",
        "leader2_preview",
        "leader3_preview",
    )

    fieldsets = (
        ("Basic Information", {
            "fields": ("status", "published_at", "slug")
        }),

        ("English Content", {
            "fields": ("title_en", "description_en", "link_en"),
        }),

        ("Welsh Content", {
            "fields": ("title_cy", "description_cy", "link_cy"),
        }),

        ("Poster Image", {
            "fields": ("poster_image", "poster_preview"),
        }),

        ("Leader 1", {
            "classes": ("collapse",),
            "fields": (
                "leader1_name",
                "leader1_role",
                "leader1_description",
                "leader1_photo",
                "leader1_preview",
            ),
        }),

        ("Leader 2", {
            "classes": ("collapse",),
            "fields": (
                "leader2_name",
                "leader2_role",
                "leader2_description",
                "leader2_photo",
                "leader2_preview",
            ),
        }),

        ("Leader 3", {
            "classes": ("collapse",),
            "fields": (
                "leader3_name",
                "leader3_role",
                "leader3_description",
                "leader3_photo",
                "leader3_preview",
            ),
        }),
    )

    # -----------------------------
    # Image preview methods
    # -----------------------------

    def poster_preview(self, obj):
        return image_preview(obj, "poster_image")
    poster_preview.short_description = "Poster Preview"

    def leader1_preview(self, obj):
        return image_preview(obj, "leader1_photo")
    leader1_preview.short_description = "Leader 1 Photo"

    def leader2_preview(self, obj):
        return image_preview(obj, "leader2_photo")
    leader2_preview.short_description = "Leader 2 Photo"

    def leader3_preview(self, obj):
        return image_preview(obj, "leader3_photo")
    leader3_preview.short_description = "Leader 3 Photo"


# ---------------------------------------------------------
# INFO SECTION ADMIN
# ---------------------------------------------------------

@admin.register(InfoSection)
class InfoSectionAdmin(admin.ModelAdmin):
    list_display = ("key", "title_en", "title_cy")
    list_filter = ("key",)
    search_fields = ("title_en", "title_cy")


# ---------------------------------------------------------
# RESOURCE ADMIN
# ---------------------------------------------------------

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title_en", "category", "published_at")
    list_filter = ("category", "published_at")
    search_fields = ("title_en", "title_cy", "description_en", "description_cy")
    ordering = ("-published_at",)
