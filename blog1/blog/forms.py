from django import forms


class Formulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefono = forms.CharField()
    mensaje = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(Formulario, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'sm-form-control required'
        self.fields['email'].widget.attrs['class'] = 'required email sm-form-control'
        self.fields['telefono'].widget.attrs['class'] = 'sm-form-control'
        self.fields['mensaje'].widget.attrs['class'] = 'required sm-form-control'

