from django.shortcuts import render,redirect
from .form import *
from .models import Imoveis
from django.views.generic.list import ListView
from finxi_teste.settings import MEDIA_URL


# Create your views here.

def criar_imovel (request):

    request.method =="POST"
    imovel_form = ImovelForm(request.POST)
    endereco_form = EnderecoForm(request.POST)
    imagens_form = ImagensForm(request.POST,request.FILES)
    
    if imovel_form.is_valid() and endereco_form.is_valid() and imagens_form.is_valid():
        imovel= imovel_form.save(commit=False)
        endereco = endereco_form.save() 
        imagem = imagens_form.save()
        imovel.endereco = endereco
        imovel.imagens = imagem
        imovel.save()
        
        return redirect('lista_imovel')
    return render(request,'cadastro_imoveis/imovel_add.html',{
        'form_imovel':imovel_form ,
        'endereco_form':endereco_form,
        'imagens_form':imagens_form
    })

class ImovelListView(ListView):
     template_name = "cadastro_imoveis/imovel_list.html"

     model = Imoveis

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media'] = MEDIA_URL

        return context


def lista_imoveis(request):
    pesquisa = request.GET.get('pesquisa')
    imovel=Imoveis.objects.all()
    if pesquisa is not None:
        imoveis = imovel.filter(endereco__rua__icontains=pesquisa)
    if not imoveis:
        imoveis = imovel.filter(endereco__bairro__icontains=pesquisa)
    if not imoveis:
        imoveis = imovel.filter(endereco__cidade__icontains=pesquisa)
    return render(request, 'cadastro_imoveis/imovel_busca.html', {'imoveis': imoveis,'media':MEDIA_URL})
    