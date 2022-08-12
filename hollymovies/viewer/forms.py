from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username']

    def save(self, commit=True):
        self.instance.is_active = True
        saved_user = super().save(commit)

        saved_user.save()
        profile = Profile(user=saved_user)
        profile.user = saved_user
        profile.save()
        return saved_user


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20, required=False)
    content = forms.CharField(max_length=500, widget=forms.Textarea)
