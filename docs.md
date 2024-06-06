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