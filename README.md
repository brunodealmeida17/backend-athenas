
# 🖥️ Backend - Django API (Gerenciamento de Pessoas)

Este projeto é uma API desenvolvida em **Django** para o gerenciamento de pessoas, permitindo operações **CRUD** e o cálculo do **peso ideal**.

## 📂 Estrutura do Projeto

```
backend/
│── pessoas/                 # Aplicação principal do Django
│   ├── migrations/          # Arquivos de migração do banco de dados
│   ├── models.py            # Modelagem da entidade Pessoa
│   ├── views.py             # Controladores (Controllers) que expõem a API REST
│   ├── services.py          # Regras de negócio
│   ├── tasks.py             # Execução das operações CRUD
│   ├── serializers.py       # Serialização dos dados para JSON
│── api/                     # Configuração da API Django Rest Framework
│── manage.py                # Arquivo principal para execução do Django
│── requirements.txt         # Dependências do projeto
│── settings.py              # Configurações do projeto
│── urls.py                  # Rotas da API
```

## 🚀 Como Rodar o Projeto

### **1️⃣ Instalar o Python e Criar um Ambiente Virtual**
```bash
python -m venv venv
# Ativar o ambiente virtual
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### **2️⃣ Instalar Dependências**
```bash
pip install -r requirements.txt
```

### **3️⃣ Configurar o Banco de Dados**
Rode as migrações:
```bash
python manage.py migrate
```

### **4️⃣ Rodar o Servidor Django**
```bash
python manage.py runserver
```
A API estará disponível em:  
🔗 `http://127.0.0.1:8000/api/pessoas/`

## 🔥 Endpoints da API

| Método | Endpoint               | Descrição                         |
|--------|------------------------|-----------------------------------|
| GET    | `/api/pessoas/`        | Listar todas as pessoas          |
| POST   | `/api/pessoas/`        | Criar uma nova pessoa            |
| PUT    | `/api/pessoas/{id}/`   | Atualizar uma pessoa existente   |
| DELETE | `/api/pessoas/{id}/`   | Remover uma pessoa               |
| GET    | `/api/pessoas/{id}/peso-ideal/` | Calcular peso ideal |

## 🎯 Tecnologias Utilizadas
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **CORS Headers**