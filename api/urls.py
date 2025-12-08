from django.urls import path

from .views import AlunoCreate, AlunoDetail
from .views import ProfessorCreate, ProfessorDetail
from .views import TurmaCreate, TurmaDetail
from .views import MatriculasCreate, MatriculasDetail

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
	path('alunos/', AlunoCreate.as_view(), name='alunos'),
	path('alunos/<int:pk>/', AlunoDetail.as_view(), name='aluno-detail'),

	path('professores/', ProfessorCreate.as_view(), name='professores'),
	path('professores/<int:pk>/', ProfessorDetail.as_view(), name='professor-detail'),

	path('turmas/', TurmaCreate.as_view(), name='turmas'),
	path('turmas/<int:pk>/', TurmaDetail.as_view(), name='turma-detail'),

	path('matriculas/', MatriculasCreate.as_view(), name='matriculas'),
	path('matriculas/<int:pk>/', MatriculasDetail.as_view(), name='matriculas-detail'),

	path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
	path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
	path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


]