from allauth.account.forms import SignupForm
from django import forms
from .models import Profile


class CustomSignupForm(SignupForm):
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea)
    favorite_anime = forms.CharField(max_length=100, required=False)

    def save(self, request):
        user = super().save(request)
        profile, created = Profile.objects.get_or_create(user=user)
        profile.bio = self.cleaned_data['bio']
        profile.favorite_anime = self.cleaned_data['favorite_anime']
        profile.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'favorite_anime']