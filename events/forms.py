from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Create a form for users to add reviews
    """

    class Meta:
        model = Post
        exclude = (
            "slug",
            "updated_on",
            "created_on",
            "status",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)

        # Add placeholders and classes to input fields
        self.fields["title"].widget.attrs["autofocus"] = True
        # for field in self.fields:
        #     if field != "rating":
        #         placeholder = placeholders[field]
        #         self.fields[field].widget.attrs["placeholder"] = placeholder
        #         self.fields[field].label = False

        #     self.fields[field].widget.attrs["class"] = "mb-3 rounded-0 profile-form"
