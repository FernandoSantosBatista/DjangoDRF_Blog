from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.slug

    def get_image(self):
        if self.image:
            return 'https://vue-blog-backend.herokuapp.com' + self.image.url
        return ''


