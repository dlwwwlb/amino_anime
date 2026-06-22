from allauth.account.forms import SignupForm
from django import forms
from .models import Profile

class CustomSignupForm(SignupForm):
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea)
    favorite_anime = forms.CharField(max_length=100, required=False)
    # avatar можно добавить, но с файлами сложнее — обычно отдельная страница редактирования

    def save(self, request):
        user = super().save(request)
        user.profile.bio = self.cleaned_data['bio']
        user.profile.favorite_anime = self.cleaned_data['favorite_anime']
        user.profile.save()
        return user