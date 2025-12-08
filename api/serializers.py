from rest_framework import serializers

from .models import Aluno, Professor, Turma, Matriculas

class AlunoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Aluno
		fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Professor
		fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Turma
		fields = '__all__'

class MatriculasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Matriculas 
		fields = '__all__'

