## FastAPI

Alguns benefícios do FastAPI se comparado ao Djando e Flask
- Assíncrono
- Documentação simplificada
- Desenvolvimento simplificado


requisitos
```sh
pip install fastapi uvicorn
```

execução
```sh
uvicorn name_file:name_app
uvicorn main:app

# reaload ativo
uvicorn main:app --reload
```

documentação
```sh
# /docs já documenta automaticamente com swagger
http://127.0.0.1:8000/docs
```