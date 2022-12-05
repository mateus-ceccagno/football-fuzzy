from django.forms import ModelForm
from nflscoreapp.models import Jogador

# Create the form class.
class JogadorForm(ModelForm):
     class Meta:
        model = Jogador
        fields = ['nome', 'vitorias', 'touchdowns', 'jardas', 'recepcoes', 'resultado']

