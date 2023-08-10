from django.shortcuts import render
from django.http import HttpResponse
from base.forms import ContatoForm

def inicio (request):
 return  render (request,'inicio.html')

def reserva (request):
 sucesso = False

 if request.method == 'GET':
        form = ContatoForm ()
 else :
        form = ContatoForm (request.POST)
        if form.is_valid ():
            sucesso = True
       
 contexto={
     
  'form': form ,
  'sucesso': sucesso ,
}
 if request.method =='POST':
  print (request.POST['nome '])
  print (request.POST['email'])
  print (request.POST['mensagem'])
  print (request.POST)(['data'])

 return render (request,'reserva.html',contexto)