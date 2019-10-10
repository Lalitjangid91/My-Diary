from django import forms
from .models import Diary
class DiaryForm(forms.ModelForm):
    class Meta():
        model=Diary
        fields=('Text',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Text'].widget.attrs.update({'class':'textarea','placeholder':"What's on your Mind"})
