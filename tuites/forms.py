from django import forms
from tuites.models import Tuite


class PostTuiteForm(forms.ModelForm):

    class Meta:
        model = Tuite
        fields = ('content', 'author')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = self.initial['user'].id
        self.fields['author'].widget = forms.HiddenInput()
        self.fields['content'].help_text = 'Digite o que está pensando'
        self.fields['content'].widget = forms.TextInput(attrs={'class':'post-tuite-input'})
        

    def clean(self):
        cleaned_data = super().clean()
        content = self.cleaned_data.get('content')
        if 'kpop' in content:
            raise forms.ValidationError('sai fedido')

        if not self.initial.get('user') == cleaned_data.get('author'):
            raise forms.ValidationError('Não burla o sistema')
        return cleaned_data