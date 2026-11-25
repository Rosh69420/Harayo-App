from django.db import models
from django.contrib.auth.models import User


class ItemPost(models.Model):
    TYPE_CHOICES = [("Lost", "Lost"), ("Found", "Found")]
    CATEGORY_CHOICES = [
        ("Electronics", "Electronics"), ("Documents", "Documents"),
        ("Accessories", "Accessories"), ("Clothing", "Clothing"),
        ("Bags", "Bags"), ("Keys", "Keys"), ("Other", "Other"),
    ]

    item_name = models.CharField(max_length=100)
    post_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="Other")
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    photo = models.ImageField(upload_to="item_photos/", blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.item_name


class Comment(models.Model):
    post = models.ForeignKey(ItemPost, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return "Comment by " + self.user.username
