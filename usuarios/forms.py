from django import forms

class LoginForms(forms.Form):
        nome_login=forms.CharField(
                label='Nome de Login', 
                required=True, 
                max_length=100,
                widget=forms.TextInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Nome de Login"
                    }
                )
        )
        senha=forms.CharField(
                label='Senha', 
                required=True, 
                max_length=70,
                widget=forms.PasswordInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Digite sua senha"
                    }
                )
    )
class CadastroForms(forms.Form):
        nome_cadastro=forms.CharField(
                label='Nome', 
                required=True, 
                max_length=100,
                widget=forms.TextInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Digite seu nome"
                    }
                )
        )
        email=forms.EmailField(
                label='E-mail', 
                required=True, 
                max_length=100,
                widget=forms.EmailInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Digite seu e-mail"
                    }
                )
        )
        senha_1=forms.CharField(
                label='Senha', 
                required=True, 
                max_length=70,
                widget=forms.PasswordInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Digite sua senha"
                    }
                )
        )
        senha_2=forms.CharField(
                label='Confirme sua Senha', 
                required=True, 
                max_length=70,
                widget=forms.PasswordInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Confirme sua senha"
                    }
                )
        )
        def clean(self):
                cleaned_data = super().clean()
                senha_1 = cleaned_data.get("senha_1")
                senha_2 = cleaned_data.get("senha_2")
                if senha_1 != senha_2:
                        raise forms.ValidationError("As senhas não conferem")
                return cleaned_data