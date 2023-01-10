from django import forms
from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link',
                  'source_link', 'featured_image', 'tags', 'vote_total', 'ratio']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Title'}
        )

        self.fields['description'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Description (Optional)'}
        )

        self.fields['demo_link'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Demo link'}
        )

        self.fields['source_link'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Source link'}
        )

        self.fields['tags'].widget.attrs.update(
            {'class': 'form-select', }
        )
