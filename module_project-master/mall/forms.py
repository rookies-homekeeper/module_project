from django import forms
from .models import Stuff

class StuffForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = ['name','price','detail','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'image':forms.FileInput(attrs = {"id" : "image_field",'class':'form-control'}),
        }


class StuffUpdateForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = ['price', 'quantity', 'detail','image']  # 수정하려는 필드만을 포함합니다.