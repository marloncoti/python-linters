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
line-length = 79  # Mantener compatibilidad con PEP 8
target-version = ['py312']

[tool.isort]
profile = "black"  # Asegurar que isort y black usen el mismo formato
line_length = 79  # Mantener compatibilidad con PEP 8


```