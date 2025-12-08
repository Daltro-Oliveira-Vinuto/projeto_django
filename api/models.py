from django.db import models

# Create your models here.

class Aluno(models.Model):
	nome = models.CharField(max_length=255)
	matricula = models.BigIntegerField(null=True, blank=True)
	curso = models.CharField(max_length=255, null=True, blank=True)
	data_nascimento = models.DateField(null=True, blank=True)
	genero = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.nome

	class Meta:
		ordering = ['nome']

class Professor(models.Model):
	nome = models.CharField(max_length=255)
	departamento = models.CharField(max_length=255, null=True, blank=True)
	ativo = models.BooleanField(null=True, blank=True)
	data_cadastro = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.nome 

	class Meta:
		ordering = ['nome']

class Turma(models.Model):
	nome = models.CharField(max_length=255)
	descricao = models.TextField(null=True, blank=True)
	data_inicio = models.DateField(null=True, blank=True)
	data_fim = models.DateField(null=True, blank=True)
	status = models.CharField(max_length=255, null=True, blank=True)

	professor_id =  models.ForeignKey(Professor, 
		on_delete=models.CASCADE)

	aluno_representante = models.OneToOneField(Aluno, 
		on_delete=models.CASCADE,
		primary_key=False,)

	alunos = models.ManyToManyField(Aluno,
	 through="Matriculas", related_name="alunos")

	def __str__(self):
		return self.nome


	class Meta:
		ordering = ['nome']

class Matriculas(models.Model):
	aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
	turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
	begin_date = models.DateField(null=True, blank=True)
	presenca_acumulada = models.FloatField(null=True, blank=True)

	def __str__(self):
		return (self.aluno, self.turma)

	class Meta:
		ordering = ["aluno"]


class Presenca(models.Model):
	matricula_id = models.ForeignKey(Matriculas, on_delete=models.CASCADE)
	data = models.DateField(null=True, blank=True)
	status = models.CharField(max_length=255,null=True, blank=True)

	def __str__(self):
		return self.matricula_id 


	class Meta:
		ordering = ['data']

