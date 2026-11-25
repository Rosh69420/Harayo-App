from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [migrations.CreateModel(name="ItemPost",fields=[
        ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
        ("item_name",models.CharField(max_length=100)),
        ("post_type",models.CharField(choices=[("Lost","Lost"),("Found","Found")],max_length=5)),
        ("description",models.TextField()),("location",models.CharField(max_length=100)),
        ("date",models.DateField()),("photo",models.ImageField(blank=True,null=True,upload_to="item_photos/")),
        ("is_resolved",models.BooleanField(default=False)),("created_at",models.DateTimeField(auto_now_add=True)),
        ("posted_by",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,to=settings.AUTH_USER_MODEL))
    ],options={"ordering":["-created_at"]})]
