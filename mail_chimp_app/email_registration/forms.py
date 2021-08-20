from django import forms
from email_registration.models import InfoModel


class Form1(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Form1, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Type your email address",
    }))

    class Meta:
        model = InfoModel
        fields = ('fullname', 'company_name', 'phone_number', 'email', 'note')


class Form2(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Form2, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Type your email address",
    }))

    class Meta:
        model = InfoModel
        fields = ('company_name', 'total_employees', 'phone_number', 'email')

