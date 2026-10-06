# API de Tarefas com FastAPI, SQLite e Docker

Projeto desenvolvido para praticar a containerização de uma aplicação FastAPI utilizando Docker, Docker Compose e Poetry.

## Tecnologias utilizadas

- Python
- FastAPI
- SQLite
- Docker
- Docker Compose
- Poetry
- Uvicorn

## Estrutura do projeto

- `main.py` - código principal da API
- `livros.db` - banco de dados SQLite
- `Dockerfile` - configuração da imagem Docker
- `docker-compose.yml` - configuração dos serviços e do container
- `pyproject.toml` - dependências gerenciadas pelo Poetry
- `poetry.lock` - arquivo que fixa as versões das dependências utilizadas
- `README.md` - instruções para execução do projeto

## Clonar o repositório

Para baixar o projeto, execute:

```bash
git clone LINK_DO_REPOSITORIO
```

Depois, acesse a pasta do projeto:

```bash
cd api-tarefas-sqlite
```

> O link de clonagem será substituído pelo endereço do repositório após a publicação no GitHub.

## Como executar

É necessário ter o Docker Desktop instalado e em execução.

Para construir a imagem e iniciar o container, execute:

```bash
docker compose up --build -d
```

Também pode ser utilizado, em instalações que usam o comando legado:

```bash
docker-compose up --build -d
```

Após iniciar, a documentação interativa da API estará disponível em:

`http://localhost:8000/docs`

## Encerrar a aplicação

Execute:

```bash
docker compose down
```

ou:

```bash
docker-compose down
```

## Desenvolvimento

O diretório do projeto é montado como volume no container e o Uvicorn utiliza a opção `--reload`. Dessa forma, alterações realizadas no código são detectadas automaticamente durante o desenvolvimento.