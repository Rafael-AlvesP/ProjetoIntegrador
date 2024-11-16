from django import forms
from django.contrib.auth.hashers import make_password

class UsuarioForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome")
    sobrenome = forms.CharField(max_length=100, label="Sobrenome")
    municipio = forms.CharField(max_length=100, required=False, label="Município")
    estado = forms.CharField(max_length=50, required=False, label="Estado")
    nome_usuario = forms.CharField(max_length=50, label="Nome de Usuário")
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirmacao_senha = forms.CharField(widget=forms.PasswordInput, label="Confirmação de Senha")
    email = forms.EmailField(label="Email")
    telefone = forms.CharField(max_length=20, required=False, label="Telefone")

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmacao_senha = cleaned_data.get("confirmacao_senha")

        if senha and confirmacao_senha and senha != confirmacao_senha:
            raise forms.ValidationError("As senhas não correspondem.")

        # Criptografa a senha antes de salvar no banco de dados
        cleaned_data["senha"] = make_password(senha)
        return cleaned_data
