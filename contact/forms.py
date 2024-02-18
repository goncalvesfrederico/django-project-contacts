from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "class-a class-b",
                "placeholder": "First Name",
            }
        ),
        label="First Name",
        help_text="Input your first name",
    )

    class Meta:
        model = Contact
        fields = (
            "first_name", "last_name", "phone",
        )
        
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name == last_name:
            msg = "The First Name and Last Name could not be the same!!!"
            self.add_error("last_name", ValidationError(msg))