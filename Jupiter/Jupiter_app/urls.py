
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='Home'),

    path('paciente_login/', views.paciente_login, name='paciente_login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('homePaciente/', views.homePaciente, name='homePaciente'),
    path('sucessoCadastro/', views.sucessoCadastroView, name='sucessoCadastro'),
    path('falhaCadastro/', views.falhaCadastroView, name='falhaCadastro'),
    path('homePaciente/exames/',views.exibir_exames, name='exibir_exames'),
    path('homePaciente/receituarios/', views.exibir_receituarios, name='exibir_receituarios'),
]
