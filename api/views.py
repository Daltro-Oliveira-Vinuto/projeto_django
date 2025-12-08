from django.shortcuts import render, redirect

from rest_framework import generics
from drf_spectacular.utils import extend_schema

from .models import Aluno, Professor, Turma, Matriculas, Presenca 

from .serializers import AlunoSerializer, ProfessorSerializer
from .serializers import TurmaSerializer, MatriculasSerializer
from .serializers import PresencaSerializer


# Create your views here.


class AlunoCreate(generics.ListCreateAPIView):
	queryset = Aluno.objects.all()
	serializer_class = AlunoSerializer 

	@extend_schema(summary="", description="")
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@extend_schema(summary="", description="")
	def pos(tself, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)


class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Aluno.objects.all()
	serializer_class = AlunoSerializer


	@extend_schema(summary="", description="")
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

class ProfessorCreate(generics.ListCreateAPIView):
	queryset = Professor.objects.all()
	serializer_class = ProfessorSerializer 

	@extend_schema(summary="", description="")
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@extend_schema(summary="", description="")
	def pos(tself, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)

class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Professor.objects.all()
	serializer_class = ProfessorSerializer 

	@extend_schema(summary="", description="")
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)


class TurmaCreate(generics.ListCreateAPIView):
	queryset = Turma.objects.all()
	serializer_class = TurmaSerializer 

	@extend_schema(summary="", description="")
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@extend_schema(summary="", description="")
	def pos(tself, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)



class TurmaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Turma.objects.all()
	serializer_class = TurmaSerializer 

	@extend_schema(summary="", description="")
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

class MatriculasCreate(generics.ListCreateAPIView):
	
	queryset = Matriculas.objects.all()
	serializer_class = MatriculasSerializer 

	@extend_schema(summary="", description="")
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@extend_schema(summary="", description="")
	def pos(tself, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)
	
	

class MatriculasDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Matriculas.objects.all()
	serializer_class = MatriculasSerializer 

	@extend_schema(summary="", description="")
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)


class PresencaCreate(generics.ListCreateAPIView):
	
	queryset = Presenca.objects.all()
	serializer_class = PresencaSerializer 

	@extend_schema(summary="", description="")
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@extend_schema(summary="", description="")
	def pos(tself, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)
	
	

class PresencaDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Presenca.objects.all()
	serializer_class = PresencaSerializer 

	@extend_schema(summary="", description="")
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)
