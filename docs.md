# Passo a passo

- Vamos instalar o python e o PIP
  - `sudo apt install software-properties-common`
  - `sudo add-apt-repository ppa:deadsnakes/ppa`
  - `sudo apt-get install python3.11`
  - `sudo apt install -y python3-pip`
  - `sudo apt install -y build-essential libssl-dev libffi-dev python3-dev`
- Instalaremos o venv para criar um ambiente virtual e jogar nossas coisas lá
  - `sudo apt install -y python3.11-venv`
  - `python3.11 -m venv .venv` para criar o ambiente virtual
  - E então `source .venv/bin/activate`
- Vamos usar o poetry como nosso gestor de dependências
  - `curl -sSL https://install.python-poetry.org | python3 -`
  - Ou pip install poetry
- Daí é só inicializar o projeto
  - `poetry init`

## Parte dois

- Rode o projeto
`uvicorn sql_app.main:app --reload` ou `fastapi dev main.py`

E vamos construir alguma coisa :D

Criamos o básico para comunicar com o BD
Criamos Modelos SQL
Criamos Schemas (Objetos de input e output)

E então melhoramos o código

## Parte 3

Queremos agora crar uma base única para que o nosso time possa trabalhar

Como?

- Docker
- Git
- Docker Compose

### Criando a imagem docker

Criamos um arquivo Dockerfile, colocando passo a passo de como queremos nosso container

- `docker build -t myimage .`

### Subindo outros services com Docker Compose

- `docker compose up`


## Referências

### FastAPI

[FastAPI Full Stack Template](https://github.com/tiangolo/full-stack-fastapi-template/tree/master)
[Full Tutorial - FastAPI](https://www.youtube.com/watch?v=XnYYwcOfcn8&list=PLqAmigZvYxIL9dnYeZEhMoHcoP4zop8-p)
[FastAPI com Docker](https://fastapi.tiangolo.com/deployment/docker)

### Docker
[Get Started - Docker](https://docs.docker.com/get-started/)
[Cheatsheet Docker](https://docs.docker.com/get-started/docker_cheatsheet.pdf)

### Docker Compose 
[Cheatsheet Docker Compose](https://devhints.io/docker-compose)
[Docker Compose - QuickStart](https://docs.docker.com/compose/gettingstarted/)

### Git
[OH MY GIT](https://ohmygit.org/)
[Aprenda o básico de Git em menos de 10 minutos](https://www.freecodecamp.org/portuguese/news/aprenda-o-basico-de-git-em-menos-de-10-minutos/)