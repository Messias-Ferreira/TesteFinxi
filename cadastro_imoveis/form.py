from django import forms
from .models import *
from django.forms import modelformset_factory


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imoveis
        fields = [
            'valor_aluguel',
            'quartos',
            'suites',
            'iptu',
            'condominio',
            'descricao',
        ]
        labels  = {
            'imagens':'Escolha suas imagens'
            
        }
        widgets = {
            'valor_aluguel': forms.TextInput(attrs={
                'placeholder': 'ex: 2000,00',
                'class': 'form-control' 
                }),
            'quartos': forms.TextInput(attrs={
                'placeholder': 'ex: 1',
                'class': 'form-control' 
                }),
            'suites': forms.TextInput(attrs={
                'placeholder': 'ex: 1',
                'class': 'form-control' 
                }),
            'iptu': forms.TextInput(attrs={
                'placeholder': 'ex: 2000',
                'class': 'form-control' 
                }),
            'condominio': forms.TextInput(attrs={
                'placeholder': 'ex: 100,00',
                'class': 'form-control' 
                }),
            'descricao': forms.Textarea(attrs={
                'placeholder': 'descriçao',
                'class': 'form-control' 
                }), 
        }

class ImagensForm(forms.ModelForm):
    class Meta:
        model = Imagens

        fields = [
            'imagem1',
            'imagem2',
            'imagem3',
            'imagem4',
        ]
        widgets = {
                'imagem1': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input' 
                }),
                'imagem2': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input'
                }),
                'imagem3': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input'
                
                }),
                'imagem4': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input'
                }),
        }

        
        
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = [
            'cep',
            'rua',
            'bairro',
            'cidade',
            'uf',
        ]
        widgets = {
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu cep para completar os campos',
                }),
            'rua': forms.TextInput(attrs={
                'class': 'form-control' 
                }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control' 
                }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control' 
                }),
            'uf': forms.TextInput(attrs={
                'class': 'form-control' 
                }),
        }
        labels  = {
            'cep' : 'CEP',
            'rua' : 'Rua',
            'bairro' : 'Bairro',
            'cidade': 'Cidade',
            'uf' : 'UF',
        }
