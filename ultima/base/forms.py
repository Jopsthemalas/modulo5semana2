from django import forms

class ContatoForm (forms.Form):
    nome_do_pet= forms.CharField ()
    email= forms.EmailField ()
    mensagem = forms.CharField (widget =forms.Textarea)
    data = forms.DateField  ()