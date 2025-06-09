from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .models import Categoria
from .utils import calcula_imc
# Create your views here.

def home(request):
    if request.method == 'GET':    
        return render(request, 'home.html')
    else:
        nome = request.POST.get('nome')
        peso_str = request.POST.get('peso').replace(',', '.')
        altura_str = request.POST.get('altura').replace(',', '.')

        peso = float(peso_str)
        altura = float(altura_str)
        
        categoria = calcula_imc(peso, altura)  
        
        categoria_obj = Categoria.objects.get(pk=categoria)
        
        user = Usuario(
            nome=nome,
            peso=peso,
            altura=altura,
            categoria=categoria_obj           
        )
        
        user.save()
        
        return render(request, 'home.html')

def dashboard(request):
    if request.method == 'GET':    
        dados = Usuario.objects.select_related('categoria').all()  # ← busca todos os registros
        
        return render(request, 'dashboard.html', {'usuarios': dados})
    
from django.shortcuts import redirect, get_object_or_404
def delete_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('dashboard')

def update_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.peso = float(request.POST.get('peso'))
        usuario.altura = float(request.POST.get('altura'))
        # Atualize categoria se necessário
        usuario.save()
        return redirect('dashboard')
    return redirect('dashboard')
