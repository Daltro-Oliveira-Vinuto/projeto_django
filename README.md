# API Projeto Django

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?logo=python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.0%2B-green.svg?logo=Django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Instituições de Fomento e Parceria

[![Website IFB](https://img.shields.io/badge/Website-IFB-%23508C3C.svg?labelColor=%23C8102E)](https://www.ifb.edu.br/) 
[![Website ihwbr](https://img.shields.io/badge/Website-ihwbr-%23DAA520.svg?labelColor=%232E2E2E)](https://hardware.org.br/)

## Colaborador - Daltro Oliveira Vinuto

[![LinkedIn Daltro Oliveira Vinuto](https://img.shields.io/badge/LinkedIn-Daltro_Oliveira_Vinuto-%230077B5.svg?labelColor=%23FFFFFF&logo=linkedin)]( https://www.linkedin.com/in/daltro-oliveira-vinuto-520485145/ )
[![GitHub Daltro Oliveira Vinuto](https://img.shields.io/badge/GitHub-Daltro_Oliveira_Vinuto_(Daltro_Oliveira_Vinuto)-%23181717.svg?logo=github&logoColor=white)]( https://github.com/Daltro-Oliveira-Vinuto )
[![Lattes Daltro Oliveira Vinuto](https://img.shields.io/badge/Lattes-Daltro_Oliveira_Vinuto-green.svg?logo=cnpq&logoColor=white)]( https://www.linkedin.com/in/daltro-oliveira-vinuto-520485145/)

## Colaborador - Kyara Esteves de Sousa

[![LinkedIn Kyara Esteves de Sousa](https://img.shields.io/badge/LinkedIn-Kyara_Esteves_de_Sousa-%230077B5.svg?labelColor=%23FFFFFF&logo=linkedin)]( https://www.linkedin.com/in/kyara-esteves-de-sousa-2144219b/?originalSubdomain=br  )
[![GitHub Kyara Esteves de Sousa](https://img.shields.io/badge/GitHub-Kyara2(Kyara_Esteves_de_Sousa)-%23181717.svg?logo=github&logoColor=white)](https://github.com/Kyara2)
[![Lattes Kyara Esteves de Sousa](https://img.shields.io/badge/Lattes-Kyara_Esteves_de_Sousa-green.svg?logo=cnpq&logoColor=white)](https://lattes.cnpq.br/4642913082106691 )


## Orientador - Prof. Claudio Ulisse

[![LinkedIn Claudio Ulisse](https://img.shields.io/badge/LinkedIn-Claudio_Ulisse-%230077B5.svg?labelColor=%23FFFFFF&logo=linkedin)](https://www.linkedin.com/in/claudioulisse/)
[![GitHub claulis](https://img.shields.io/badge/GitHub-claulis_(Claudio_Ulisse)-%23181717.svg?logo=github&logoColor=white)](https://github.com/claulis)
[![Lattes Claudio Ulisse](https://img.shields.io/badge/Lattes-Claudio_Ulisse-green.svg?logo=cnpq&logoColor=white)](http://lattes.cnpq.br/4607303092740768)

## Sumário

- [Visão Geral](#visão-geral)
- [Pacotes Utilizados](#pacotes-utilizados)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Diagrama de Banco de Dados](#diagrama-de-banco-de-dados)
- [Documentação da API](#documentação-da-api)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Deploy](#deploy)

## Visão Geral

Esta API implementa um **Sistema de Chamada de Alunos** voltado ao contexto de **instituições públicas de ensino superior**, com o objetivo de **modernizar o processo de registro de presença** e **viabilizar análises estatísticas institucionais** sobre frequência, absenteísmo e desempenho acadêmico.

O sistema está inserido no domínio da **gestão educacional**, oferecendo uma camada **backend RESTful** para o gerenciamento de **professores**, **turmas**, **alunos**, **matrículas** e **registros de presença**. A API foi projetada para ser consumida por **aplicações front-end utilizadas por docentes**, além de **dashboards de Business Intelligence (BI)** e **ferramentas de auditoria educacional**.

O principal problema abordado é a **ineficiência e a baixa confiabilidade dos métodos tradicionais de chamada**, que dificultam o acompanhamento sistemático da presença e a geração de **indicadores acadêmicos consolidados**. Ao centralizar e estruturar esses dados, a API possibilita análises como **frequência média por turma**, **histórico de presença por aluno**, **carga docente** e **identificação de padrões de absenteísmo**, apoiando a **tomada de decisão institucional baseada em dados**.

O público-alvo da solução inclui **administradores acadêmicos**, **professores** e **alunos**, cada um com **níveis de acesso distintos**. Em alto nível, a API disponibiliza funcionalidades de **cadastro**, **consulta** e **relacionamento de entidades acadêmicas**, **matrícula de alunos em turmas**, **marcação de presença** e **exposição de dados consolidados**, seguindo boas práticas de **arquitetura REST**, **segurança de acesso** e **manutenibilidade**.


## Pacotes Utilizados

## Pacotes Utilizados


| **Pacote** | **Versão** | **Descrição** |
|------------|------------|---------------|
| **Django** | >=6.0,<7.0 | Framework web principal para desenvolvimento do backend. |
| **djangorestframework** | >=3.16.1,<4.0.0 | Framework para construção de APIs RESTful com Django. |
| **drf-spectacular** | >=0.29.0,<0.30.0 | Geração automática do schema OpenAPI da API. |
| **drf-spectacular[swagger]** | >=0.29.0,<0.30.0 | Interface Swagger UI para visualização e testes da API. |
| **drf-spectacular[redoc]** | >=0.29.0,<0.30.0 | Interface ReDoc para documentação alternativa da API. |
| **djangorestframework-simplejwt** | >=5.5.1,<6.0.0 | Autenticação baseada em JSON Web Tokens (JWT). |
| **python-dotenv** | >=1.2.1,<2.0.0 | Carregamento de variáveis de ambiente a partir de arquivos `.env`. |
| **psycopg** | >=3.3.2,<4.0.0 | Driver PostgreSQL para acesso ao banco de dados em produção. |
| **dj-database-url** | >=3.0.1,<4.0.0 | Configuração do banco de dados via URL (deploy em nuvem). |
| **gunicorn** | >=23.0.0,<24.0.0 | Servidor WSGI para execução da aplicação em produção. |
| **uvicorn** | >=0.38.0,<0.39.0 | Servidor ASGI para execução assíncrona quando aplicável. |
| **django-debug-toolbar** | >=6.1.0,<7.0.0 | Ferramenta de depuração utilizada em ambiente de desenvolvimento. |
| **django-extensions** | >=4.1,<5.0 | Extensões utilitárias para desenvolvimento e manutenção do projeto. |

> **Nota:** Esses pacotes se encontram na variável `dependencies`  do arquivo `pyproject.toml` 

## Estrutura do Projeto

Abaixo podemos observar a organização dos diretórios e arquivos do projeto no formato de árvore de diretórios(comando tree) para uma clara visualização.

```
$ tree
.
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-312.pyc
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-312.pyc
│   │   ├── apps.cpython-312.pyc
│   │   ├── __init__.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── serializers.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── views.cpython-312.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── build.sh
├── docs
│   └── database_diagram.png
├── manage.py
├── poetry.lock
├── projeto_django
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── wsgi.cpython-312.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pyproject.toml
├── README.md
└── render.yaml

8 directories, 35 files

```

## Estrutura do Projeto


A seguir está a descrição dos diretórios e módulos que compõem o projeto.


### Diretórios Principais


- **api/** 
 Contém a aplicação principal da API, responsável pela lógica de negócio, modelos de dados, serialização e endpoints REST.


- **projeto_django/** 
 Diretório de configuração global do projeto Django, incluindo definições de URLs, settings e interfaces WSGI/ASGI.


- **migrations/** 
 Armazena os arquivos de migração do banco de dados, responsáveis por versionar a estrutura das tabelas.


- **__pycache__/** 
 Diretórios gerados automaticamente pelo Python para armazenar bytecode compilado (`.pyc`).


### Arquivos e Módulos Relevantes


#### Diretório `api/`


- **admin.py** 
 Registro dos modelos da aplicação para gerenciamento via Django Admin.


- **apps.py** 
 Configuração da aplicação `api`, incluindo metadados e inicialização.


- **models.py** 
 Definição das entidades do domínio e mapeamento objeto-relacional (ORM).


- **serializers.py** 
 Serialização e desserialização dos modelos para comunicação via API REST.


- **views.py** 
 Implementação das views da API, contendo a lógica dos endpoints.


- **urls.py** 
 Mapeamento das rotas da aplicação `api` para suas respectivas views.


- **tests.py** 
 Estrutura para testes automatizados da aplicação.


#### Diretório `projeto_django/`


- **settings.py** 
 Configurações globais do projeto, incluindo banco de dados, apps instalados, middlewares e variáveis de ambiente.


- **urls.py** 
 Arquivo central de roteamento do projeto, agregando as URLs das aplicações.


- **asgi.py** 
 Ponto de entrada ASGI para execução assíncrona da aplicação.


- **wsgi.py** 
 Ponto de entrada WSGI utilizado por servidores de produção como o Gunicorn.


### Arquivos na Raiz do Projeto


- **manage.py** 
 Utilitário de linha de comando do Django para execução de tarefas administrativas.


- **pyproject.toml** 
 Arquivo de configuração do Poetry, contendo dependências, versões e metadados do projeto.


- **poetry.lock** 
 Lockfile que garante a reprodutibilidade das dependências instaladas.


- **render.yaml** 
 Arquivo de configuração do Render para provisionamento de recursos e deploy automatizado via Docker.


- **build.sh** 
 Script executado durante o processo de build no deploy, responsável por instalar dependências e preparar o ambiente.


- **README.md** 
 Documentação principal do projeto, contendo descrição, instruções e referências.


## Diagrama ER (Entidade-Relacionamento) do Banco de Dados

![Diagrama de Banco de Dados](./docs/database_diagram.png)


> **Detalhes:** Diagrama ER gerado pelo pgAdmin4 para o banco de dados Postgres.

# Modelo Lógico do Banco de Dados


Este documento descreve o modelo lógico do banco de dados utilizado pela API de Chamada de Alunos.
O diagrama entidade-relacionamento (ER) encontra-se documentado em imagem separada e serve como referência visual para as estruturas aqui descritas.

---

## Entidades Principais

### 1. Aluno

A entidade **Aluno** representa os estudantes matriculados na instituição e contém informações acadêmicas e cadastrais necessárias para identificação e análise estatística.

**Principais atributos:**

* `id`: Identificador único do aluno (chave primária).
* `nome`: Nome completo do aluno.
* `matricula`: Número de matrícula institucional.
* `email`: Endereço de e-mail do aluno.
* `curso`: Curso de graduação ao qual o aluno pertence.
* `data_nascimento`: Data de nascimento.
* `genero`: Informação utilizada para análises estatísticas institucionais.

---

### 2. Professor

A entidade **Professor** representa os docentes responsáveis pelas turmas oferecidas pela instituição.

**Principais atributos:**

* `id`: Identificador único do professor (chave primária).
* `nome`: Nome completo do professor.
* `email`: E-mail institucional.
* `departamento`: Departamento acadêmico ao qual o professor está vinculado.
* `ativo`: Indica se o professor está em exercício.
* `data_cadastro`: Data e hora do registro no sistema.

---

### 3. Turma

A entidade **Turma** representa as disciplinas ou classes oferecidas em um determinado período letivo.

**Principais atributos:**

* `id`: Identificador único da turma (chave primária).
* `nome`: Nome da disciplina ou turma.
* `descricao`: Descrição complementar da turma.
* `data_inicio`: Data de início das atividades.
* `data_fim`: Data de encerramento.
* `status`: Situação da turma (Ativa, Concluída ou Cancelada).
* `professor_id`: Referência ao professor responsável.
* `aluno_representante_id`: Referência ao aluno representante da turma.

---

## Entidades de Relacionamento

### 4. Matrícula

A entidade **Matrícula** atua como tabela de junção, viabilizando o relacionamento muitos-para-muitos entre alunos e turmas.

**Principais atributos:**

* `id`: Identificador único da matrícula.
* `data_matricula`: Data em que o aluno foi matriculado na turma.
* `presenca_acumulada`: Contador utilizado para estatísticas de presença.
* `aluno_id`: Referência ao aluno matriculado.
* `turma_id`: Referência à turma associada.

---

### 5. Presença

A entidade **Presença** registra a participação do aluno em cada aula, permitindo análises detalhadas de frequência.

**Principais atributos:**


* `id`: Identificador único do registro de presença.
* `data`: Data da aula.
* `status`: Situação do aluno na aula (Presente, Ausente ou Justificado).
* `matricula_id`: Referência à matrícula correspondente.

---

## Relacionamentos entre Entidades

### Professor ↔ Turma (1:N)

* Um **professor** pode lecionar **várias turmas**.
* Cada **turma** possui **apenas um professor responsável**.
* Esse relacionamento permite análises como carga horária docente e distribuição de turmas.

---

### Turma ↔ Aluno (N:N)

* Uma **turma** pode ter **vários alunos matriculados**.
* Um **aluno** pode se matricular em **várias turmas**.
* Esse relacionamento é implementado por meio da entidade **Matrícula**, que armazena informações adicionais relevantes.

---

### Turma ↔ Aluno (Representante) (1:1)

* Cada **turma** possui **um único aluno representante**.
* Um **aluno** pode ser representante de **no máximo uma turma**.
* Esse relacionamento adiciona governança estudantil e suporte à gestão acadêmica.

---

### Matrícula ↔ Presença (1:N)

* Uma **matrícula** pode possuir **vários registros de presença**.
* Cada **registro de presença** está associado a **uma única matrícula**.
* Esse relacionamento permite cálculos estatísticos como média de presença por turma e por aluno.

---

## Considerações Finais

O modelo foi projetado para garantir:

* Integridade referencial entre entidades.
* Flexibilidade para análises estatísticas institucionais.
* Suporte a relatórios acadêmicos e dashboards de presença.
* Aderência aos princípios RESTful e boas práticas de modelagem relacional.


Este modelo serve como base para a implementação dos **models do Django**, **serializers do DRF** e **consultas analíticas** futuras.


## Documentação da API

A documentação interativa está disponível em `/api/docs/` (Swagger UI) ou `/api/redoc/` (ReDoc) no ambiente de desenvolvimento.

### Endpoints Principais

# Documentação dos Endpoints da API


A tabela abaixo descreve os principais endpoints da API RESTful de Chamada de Alunos, incluindo métodos HTTP, descrição funcional e requisitos de autenticação, conforme definido no escopo do projeto.


| Campos Afetados               | Método HTTP | Endpoint                                  | Descrição                                                    | Autenticação Requerida             |
| ----------------------------- | ----------- | ----------------------------------------- | ------------------------------------------------------------ | ---------------------------------- |
| Professor                     | GET         | `/api/professores/`                       | Lista todos os professores cadastrados (dados públicos).     | ❌ Não                              |
| Professor                     | GET         | `/api/professores/{id}/`                  | Retorna os detalhes de um professor específico.              | ❌ Não                              |
| Professor                     | POST        | `/api/professores/`                       | Cadastra um novo professor no sistema.                       | ✅ Sim (Administrador)              |
| Professor                     | PUT         | `/api/professores/{id}/`                  | Atualiza os dados de um professor existente.                 | ✅ Sim (Administrador)              |
| Professor                     | DELETE      | `/api/professores/{id}/`                  | Remove um professor do sistema.                              | ✅ Sim (Administrador)              |
| Turma                         | GET         | `/api/turmas/`                            | Lista todas as turmas ativas (sem dados pessoais sensíveis). | ❌ Não                              |
| Turma                         | GET         | `/api/turmas/{id}/`                       | Retorna os detalhes completos de uma turma.                  | ❌ Não                              |
| Turma                         | POST        | `/api/turmas/`                            | Cria uma nova turma.                                         | ✅ Sim (Administrador)              |
| Turma                         | PUT         | `/api/turmas/{id}/`                       | Atualiza informações de uma turma.                           | ✅ Sim (Administrador)              |
| Turma                         | DELETE      | `/api/turmas/{id}/`                       | Remove uma turma do sistema.                                 | ✅ Sim (Administrador)              |
| Aluno                         | GET         | `/api/alunos/`                            | Lista alunos cadastrados.                                    | ❌ Não                              |
| Aluno                         | GET         | `/api/alunos/{id}/`                       | Retorna os dados de um aluno específico.                     | ✅ Sim (Aluno ou Administrador)     |
| Aluno                         | POST        | `/api/alunos/`                            | Cadastra um novo aluno.                                      | ✅ Sim (Administrador)              |
| Aluno                         | PUT         | `/api/alunos/{id}/`                       | Atualiza os dados de um aluno.                               | ✅ Sim (Administrador)              |
| Aluno                         | DELETE      | `/api/alunos/{id}/`                       | Remove um aluno do sistema.                                  | ✅ Sim (Administrador)              |
| Matrícula                     | POST        | `/api/turmas/{id}/matricular-aluno/`      | Matricula um aluno em uma turma.                             | ✅ Sim (Administrador)              |
| Matrícula                     | GET         | `/api/turmas/{id}/alunos/`                | Lista alunos matriculados em uma turma.                      | ❌ Não                              |
| Professor ↔ Turma             | GET         | `/api/professores/{id}/turmas/`           | Lista as turmas lecionadas por um professor.                 | ❌ Não                              |
| Professor ↔ Turma             | POST        | `/api/turmas/{id}/atribuir-professor/`    | Atribui um professor responsável à turma.                    | ✅ Sim (Administrador)              |
| Turma ↔ Aluno (Representante) | PUT         | `/api/turmas/{id}/definir-representante/` | Define um aluno como representante da turma.                 | ✅ Sim (Administrador)              |
| Turma ↔ Aluno (Representante) | GET         | `/api/turmas/{id}/representante/`         | Retorna o aluno representante da turma.                      | ❌ Não                              |
| Presença                      | POST        | `/api/presencas/`                         | Registra a presença de alunos em uma aula.                   | ✅ Sim (Professor)                  |
| Presença                      | GET         | `/api/alunos/{id}/presencas/`             | Consulta as presenças de um aluno específico.                | ✅ Sim (Aluno)                      |
| Dashboard                     | GET         | `/api/turmas/{id}/dashboard/`             | Retorna dados consolidados da turma, professor e presenças.  | ✅ Sim (Professor ou Administrador) |

---

### Observações sobre Autenticação

* **Administrador:** Acesso total (CRUD completo).
* **Professor:** Pode gerenciar presenças e visualizar suas turmas.
* **Aluno:** Acesso apenas às próprias presenças.
* **Rotas públicas:** Disponíveis para transparência institucional, sem exposição de dados sensíveis.


A autenticação é baseada em **tokens** (ex.: JWT ou Token Authentication do Django Rest Framework).


> **Detalhes:** Consulte a interface Swagger para schemas de request/response, parâmetros e exemplos.

## Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente local.

# Configuração do Ambiente Local


Este guia descreve o passo a passo para configurar e executar o projeto localmente em ambiente de desenvolvimento.

---

## Pré-requisitos

Certifique-se de que os seguintes itens estejam instalados na sua máquina:

* Python 3.10 ou superior
* Poetry
* PostgreSQL
* Git

---

## 1. Clonar o Repositório

```bas
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
---

## 2. Ativar o Ambiente Virtual com Poetry

Antes de qualquer comando, é necessário **ativar o ambiente virtual** gerenciado pelo Poetry:

```bash
poetry env activate
```

> ⚠️ Todos os comandos seguintes devem ser executados **com o ambiente virtual ativo**.

---

## 3. Instalar as Dependências do Projeto

Com o ambiente ativado, instale todas as dependências definidas no `pyproject.toml`:

```bash
poetry install
```
---

## 4. Criar o Arquivo `.env`

Na raiz do projeto, crie um arquivo chamado `.env` contendo as variáveis de ambiente necessárias para a configuração do banco de dados, utilizadas em `settings.DATABASES`.

### Exemplo de `.env`:

```env
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui


DB_NAME=chamada_alunos
DB_USER=postgres
DB_PASSWORD=senha_do_banco
DB_HOST=localhost
DB_PORT=5432
```

> 🔒 **Importante:** Nunca versionar o arquivo `.env` no repositório.

---

## 5. Verificar o SQL Gerado pelas Migrações (Recomendado)

Antes de aplicar as migrações no banco de dados, recomenda-se verificar o SQL que será executado:

```bash
python manage.py sqlmigrate database_diagram 0001
```

Substitua `0001` pelo número da migração desejada, caso existam outras.

---

## 6. Aplicar as Migrações


Após a verificação do SQL, execute as migrações para criar as tabelas no banco de dados:


```bash
python manage.py migrate
```
---

## 7. Criar Superusuário (Opcional, Recomendado)

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

---

## 8. Executar o Servidor de Desenvolvimento

Inicie o servidor local do Django:

```bash
python manage.py runserver
```

O projeto estará disponível em:

```
http://127.0.0.1:8000/
```
---

## Considerações Finais

* Certifique-se de que o serviço do PostgreSQL esteja em execução.
* Caso altere models, gere novas migrações com:

 ```bash
 python manage.py makemigrations
 ```
* Sempre valide o SQL com `sqlmigrate` antes de aplicar mudanças em ambientes controlados.

Este procedimento garante um ambiente local consistente e alinhado às boas práticas de desenvolvimento com Django e Poetry.

## Deploy

# Deploy no Render

Este projeto está configurado para deploy automático na plataforma **Render**, utilizando **Blueprints**, com os arquivos `render.yaml` e `build.sh`, garantindo padronização e reprodutibilidade do ambiente de produção.

🔗 **Aplicação em produção:**
[https://projeto-django-kpbx.onrender.com/api/docs/swagger/](https://projeto-django-kpbx.onrender.com/api/docs/swagger/)

---

## Visão Geral da Estratégia de Deploy

O deploy é realizado a partir de um **Blueprint do Render**, que descreve toda a infraestrutura necessária (serviço web, variáveis de ambiente e comandos de build) em um único arquivo declarativo (`render.yaml`).

O processo de build e inicialização da aplicação é controlado por um script (`build.sh`), garantindo consistência entre ambientes.

---

## Passo a Passo do Deploy

### 1. Criar Conta e Conectar o Repositório

1. Acesse [https://render.com](https://render.com)
2. Crie uma conta ou faça login.
3. Conecte sua conta ao repositório GitHub que contém o projeto.
4. Garanta que o repositório possua os arquivos:


  * `render.yaml`
  * `build.sh`
  * `pyproject.toml`

---

### 2. Configurar o Blueprint (`render.yaml`)

O arquivo `render.yaml` define os serviços necessários para a aplicação, incluindo o serviço web Django e suas variáveis de ambiente.

Principais responsabilidades do `render.yaml`:

* Definir o tipo de serviço (`web`)
* Configurar o comando de build
* Configurar o comando de start
* Declarar variáveis de ambiente sensíveis
* Associar o serviço ao repositório

---

### 3. Script de Build (`build.sh`)

O arquivo `build.sh` é executado automaticamente durante o processo de build no Render e é responsável por:

* Instalar dependências via Poetry
* Coletar arquivos estáticos
* Executar migrações do banco de dados

Fluxo típico executado pelo script:

1. Instalação das dependências
2. Coleta de arquivos estáticos
3. Aplicação das migrações (`migrate`)

---

### 4. Criação do Serviço via Blueprint

1. No painel do Render, selecione **New + → Blueprint**.
2. Escolha o repositório do projeto.
3. O Render detectará automaticamente o arquivo `render.yaml`.
4. Revise as configurações exibidas.
5. Confirme a criação do serviço.

Após a confirmação, o Render iniciará automaticamente o processo de build e deploy.

---

### 5. Configuração das Variáveis de Ambiente

As variáveis de ambiente definidas no `render.yaml` ou no painel do Render incluem:

* `DEBUG`
* `SECRET_KEY`
* `DATABASE_URL`
* Variáveis relacionadas ao Django e PostgreSQL

Essas variáveis são injetadas automaticamente no ambiente de produção e utilizadas pelo `settings.py`.

---

### 6. Execução Automática do Deploy

Sempre que um novo commit é enviado para a branch principal do repositório:

* O Render inicia um novo build
* Executa o `build.sh`
* Reinicia o serviço automaticamente

Esse fluxo garante **deploy contínuo (CI/CD)**.

---

## Verificação do Deploy

Após a conclusão do deploy, a aplicação pode ser acessada pelo seguinte endereço:

🔗 [https://projeto-django-kpbx.onrender.com/api/docs/swagger/](https://projeto-django-kpbx.onrender.com/api/docs/swagger/)

Neste endpoint é possível:

* Visualizar a documentação da API (Swagger)
* Testar requisições diretamente no navegador
* Validar autenticação e endpoints

---

## Considerações Finais

* O uso de **Blueprints** garante versionamento da infraestrutura.
* O `render.yaml` centraliza a configuração do ambiente.
* O `build.sh` assegura consistência no processo de build.
* O deploy é automatizado e reprodutível.

Esse modelo segue boas práticas de **DevOps**, **infraestrutura como código** e **deploy contínuo**.
