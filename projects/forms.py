from django import forms
from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link',
                  'source_link', 'tags', 'vote_total', 'ratio']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Title'}
        )

        self.fields['description'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Description (optional)'}
        )

        self.fields['demo_link'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'link'}
        )

        self.fields['source_link'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'source link'}
        )
