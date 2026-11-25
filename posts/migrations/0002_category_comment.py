from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="itempost",
            name="category",
            field=models.CharField(
                choices=[("Electronics", "Electronics"), ("Documents", "Documents"), ("Accessories", "Accessories"), ("Clothing", "Clothing"), ("Bags", "Bags"), ("Keys", "Keys"), ("Other", "Other")],
                default="Other", max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("message", models.CharField(max_length=500)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("post", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="posts.itempost")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["date"]},
        ),
    ]
