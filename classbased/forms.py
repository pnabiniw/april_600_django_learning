from django import forms
from crud.models import ClassRoom


class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'class name'}))


class ClassRoomModelForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ["name"]   # "__all__" is used to add all fields
