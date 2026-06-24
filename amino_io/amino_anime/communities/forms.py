from django import forms
from .models import Community

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description', 'icon', 'background_image', 'is_public', 'tags']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }