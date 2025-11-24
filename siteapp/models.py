from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# -----------------------------------------
# Stiwdio Dyfi Landing Page Content
# -----------------------------------------

class LandingPage(models.Model):
    title = models.CharField(max_length=200, default="Welcome to Stiwdio Dyfi")
    slug = models.SlugField(unique=True, blank=True, max_length=200)
    image = CloudinaryField('image')   # Cloudinary-hosted image
    subtitle = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Landing Page Section"
        verbose_name_plural = "Landing Page Sections"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate slug like Nadia's blog model (file cited above)
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while LandingPage.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)
