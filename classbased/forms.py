from django import forms
from crud.models import ClassRoom, Student


class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'class name'}))


class ClassRoomModelForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ["name"]   # "__all__" is used to add all fields


class StudentModelForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=14)
    bio = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))
    profile_picture = forms.FileField(required=False)

    class Meta:
        model = Student
        fields = ["name", "age", "email", "address", "classroom"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
