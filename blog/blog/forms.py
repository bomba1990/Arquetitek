from django import forms


class Form(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'sm-form-control required'
        self.fields['email'].widget.attrs['class'] = 'required email sm-form-control'
        self.fields['phone'].widget.attrs['class'] = 'sm-form-control'
        self.fields['message'].widget.attrs['class'] = 'required sm-form-control'

