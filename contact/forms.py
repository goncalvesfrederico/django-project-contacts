from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*",
            }
        )
    )

    class Meta:
        model = Contact
        fields = (
            "first_name", "last_name", "phone", "email", "description", "category", "picture"
        )
        
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name == last_name:
            msg = "The First Name and Last Name could not be the same!!!"
            self.add_error("last_name", ValidationError(msg))


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        min_length=3,
        required=True,
    )
    last_name = forms.CharField(
        min_length=3,
        required=True,
    )
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "is_active", "username",)

    # validation if email already exists from created user.
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            msg = "This email already exists!"
            self.add_error(
                "email",
                ValidationError(msg, code="invalid")
            )
        return email