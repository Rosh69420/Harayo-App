from django import forms
from .models import ItemPost, Comment


class ItemPostForm(forms.ModelForm):
    class Meta:
        model = ItemPost
        fields = ["item_name", "post_type", "category", "description", "location", "date", "photo"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_item_name(self):
        item_name = self.cleaned_data["item_name"].strip()
        if len(item_name) < 2:
            raise forms.ValidationError("Please enter an item name with at least 2 characters.")
        return item_name

    def clean_description(self):
        description = self.cleaned_data["description"].strip()
        if len(description) < 10:
            raise forms.ValidationError("Please write at least 10 characters about the item.")
        return description


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 3, "placeholder": "Write a message about this item..."})}

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if not message:
            raise forms.ValidationError("Message cannot be empty.")
        return message
