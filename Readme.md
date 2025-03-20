1. Instalar linters y herramientas de validación para python

```bash 
pip install flake8 black isort
```
o agregarlas al archivo reqquirements.txt

```bash

fastapi
uvicorn
flake8
black
isort

```

2. Configurar `flake`, `black` e `isort` con reglas personalizadas

flake8 usa un archivo .flake8
```ini
[flake8]
max-line-length = 88
ignore = E203, E266, E501, W503
exclude = .git, __pycache__, venv

```

black e isort pueden configurarse en un archvio pyproject.toml

```toml

[tool.black]
line-length = 79  
target-version = ['py312']

[tool.isort]
profile = "black"  
line_length = 79  


```


3. Para asegurar que no analicen los archivos de .git, __pycache__ y venv, u otras carpetas 
agregamos la exclusiones en el archivo de configuración


`pyproject.toml` Para black e isort

```toml


[tool.black]
line-length = 79
target-version = ['py312']
exclude = '''
/(
    \.git
  | __pycache__
  | venv
)/
'''

[tool.isort]
profile = "black"
line_length = 79
skip = [".git", "__pycache__", "venv"]


```


`.flake8`  Para Flake

```ini
[flake8]
max-line-length = 79
exclude = .git, __pycache__, venv
ignore = E203, W503
```


4. Ejecutar Linters

flake8 .
black --check .
isort --check-only .


5.  Para Corregir automaticamente con black e isort. ejecutamos el comando

```bash

black .
isort .


```


6.  Se puede  ejecutar un hook de precomit para ejecutar los linters antes de hacer el push al servidor remoto

6.1  Instalar Precomit

```bash
pip install pre-commit
```
o agregarla en el archivo requierements.txt y volver a instalar `pip install -r requirements.txt`

7. definir un archivo de configuración de precomit con los comandos a ejecutar
`.pre-commit-config.yml`

```yaml

repos:
  - repo: local
    hooks:
      - id: flake8
        name: Flake8 Linter
        entry: flake8
        language: system
        types: [python]
        args: ["--config=.flake8"]

      - id: black
        name: Black Formatter
        entry: black
        language: system
        types: [python]
        args: ["--config=pyproject.toml"]

      - id: isort
        name: Isort Import Sorter
        entry: isort
        language: system
        types: [python]
        args: ["--settings=pyproject.toml"]


```

8. instalar el hook de git en la configuración local de git

```bash

pre-commit install
```

9. editar archivos y ejecutar el commit.


10. se puede ejecutar manualmente con el comando

```bash
pre-commit run --all-files

```