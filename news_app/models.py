from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    name_category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class News(models.Model):
    head = models.CharField(max_length=150)
    text = models.TextField()
    new_cat = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.head

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"