from django import forms


class JogoForm(forms.Form):
    nome = forms.CharField(max_length=50, min_length=3, label="Nome do Jogo")
    valor = forms.DecimalField(max_digits=9, decimal_places=2, label="Valor do jogo")
    data_lancamento = forms.DateField(label="Data de lançamento")
    desenvolvedora = forms.CharField(label="Desenvolvedora", min_length=2, max_length=100, required=False)
    descricao = forms.CharField(widget=forms.Textarea, label="Descrição", required=False)
    foto_capa = forms.ImageField(label="Foto de capa")
