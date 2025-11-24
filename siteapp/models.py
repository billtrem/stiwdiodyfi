from django.db import models
from django.utils.text import slugify
from datetime import date
from cloudinary_storage.storage import MediaCloudinaryStorage


# ---------------------------------------------------------
# CHOICES
# ---------------------------------------------------------

STATUS_CHOICES = [
    ("past", "Past"),
    ("present", "Present"),
    ("future", "Future"),
]

INFO_SECTION_CHOICES = [
    ("info", "Info"),
    ("join", "Join"),
    ("support", "Support"),
]

RESOURCE_CATEGORY_CHOICES = [
    ("manual", "Manual / Guide"),
    ("manifesto", "Manifesto"),
    ("policy", "Policy / Framework"),
    ("other", "Other"),
]


# ---------------------------------------------------------
# PROJECT MODEL (Project + Leadership)
# ---------------------------------------------------------

class Project(models.Model):
    """
    A single bilingual project with optional poster & leadership.
    """

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    published_at = models.DateField(default=date.today)

    slug = models.SlugField(unique=True, blank=True)

    # English
    title_en = models.CharField(max_length=255)
    description_en = models.TextField()
    link_en = models.URLField(blank=True)

    # Welsh
    title_cy = models.CharField(max_length=255)
    description_cy = models.TextField()
    link_cy = models.URLField(blank=True)

    # Shared media (CLOUDINARY)
    poster_image = models.ImageField(
        storage=MediaCloudinaryStorage(),
        upload_to="projects/",
        blank=True,
        null=True
    )

    # Leadership – up to 3 people (CLOUDINARY)
    leader1_name = models.CharField(max_length=200, blank=True)
    leader1_role = models.CharField(max_length=200, blank=True)
    leader1_description = models.TextField(blank=True)
    leader1_photo = models.ImageField(
        storage=MediaCloudinaryStorage(),
        upload_to="leaders/",
        blank=True,
        null=True
    )

    leader2_name = models.CharField(max_length=200, blank=True)
    leader2_role = models.CharField(max_length=200, blank=True)
    leader2_description = models.TextField(blank=True)
    leader2_photo = models.ImageField(
        storage=MediaCloudinaryStorage(),
        upload_to="leaders/",
        blank=True,
        null=True
    )

    leader3_name = models.CharField(max_length=200, blank=True)
    leader3_role = models.CharField(max_length=200, blank=True)
    leader3_description = models.TextField(blank=True)
    leader3_photo = models.ImageField(
        storage=MediaCloudinaryStorage(),
        upload_to="leaders/",
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title_en

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    # Helpers for templates
    def get_title(self, lang):
        return self.title_cy if lang == "cy" else self.title_en

    def get_description(self, lang):
        return self.description_cy if lang == "cy" else self.description_en

    def get_link(self, lang):
        return self.link_cy if lang == "cy" else self.link_en


# ---------------------------------------------------------
# INFO SECTIONS
# ---------------------------------------------------------

class InfoSection(models.Model):

    key = models.CharField(
        max_length=20,
        choices=INFO_SECTION_CHOICES,
        unique=True,
        help_text="Which section this belongs to",
    )

    title_en = models.CharField(max_length=255)
    body_en = models.TextField()

    title_cy = models.CharField(max_length=255)
    body_cy = models.TextField()

    def __str__(self):
        return f"{self.get_key_display()} section"

    def get_title(self, lang):
        return self.title_cy if lang == "cy" else self.title_en

    def get_body(self, lang):
        return self.body_cy if lang == "cy" else self.body_en


# ---------------------------------------------------------
# RESOURCES
# ---------------------------------------------------------

class Resource(models.Model):

    category = models.CharField(
        max_length=20,
        choices=RESOURCE_CATEGORY_CHOICES,
        default="other",
    )

    published_at = models.DateField(default=date.today)

    title_en = models.CharField(max_length=255)
    description_en = models.TextField(blank=True)

    title_cy = models.CharField(max_length=255)
    description_cy = models.TextField(blank=True)

    # CLOUDINARY FILE
    file = models.FileField(
        storage=MediaCloudinaryStorage(),
        upload_to="resources/",
        blank=True,
        null=True
    )

    link = models.URLField(blank=True, help_text="Optional external link")

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title_en

    def get_title(self, lang):
        return self.title_cy if lang == "cy" else self.title_en

    def get_description(self, lang):
        return self.description_cy if lang == "cy" else self.description_en
