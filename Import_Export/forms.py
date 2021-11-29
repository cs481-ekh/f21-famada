from .models import FilesModel
from django import forms


# class UploadFileForm(forms.Form):
#     file = forms.FileField(label='Your file')

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FilesModel
        fields = ('csv',)
