# 📋 Formulário de Confirmação de Presença

Projeto web desenvolvido em **Python com Flask** para coletar e gerenciar confirmações de presença em eventos (ex: casamento, aniversário, confraternizações).

O sistema permite que convidados confirmem presença através de um formulário simples, enquanto um **usuário administrador** pode visualizar a lista completa de confirmados de forma segura.

---

## 🚀 Funcionalidades

* ✅ Formulário de confirmação de presença
* ✅ Salvamento dos dados em arquivo **JSON** (sem banco de dados)
* ✅ Página administrativa protegida por senha
* ✅ Listagem de confirmados (somente admin)
* ✅ Mensagens de feedback com **Flash messages**
* ✅ Interface simples e responsiva

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Flask
* Flask-WTF
* HTML5
* CSS3
* Bootstrap
* JSON (persistência de dados)

---

## 📁 Estrutura do Projeto

```
FORM_PRESENCA/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   ├── utils.py
│   ├── confirmados.json
│   ├── templates/
│   │   ├── index.html
│   │   ├── admin.html
│   │   └── lista.html
│
├── static/
│   └── css/
│       └── style.css
│
├── venv/ (não versionado)
├── .gitignore
├── main.py
└── README.md
```

---

## ▶️ Como Executar o Projeto Localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd form_presenca
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install flask flask-wtf
```

### 4️⃣ Executar a aplicação

```bash
python main.py
```

Acesse no navegador:
👉 `http://127.0.0.1:5001`

---

## 🔐 Acesso Administrativo

* URL: `/admin`
* Apenas usuários com a senha configurada em `app.config['ADMIN_PASSWORD']` têm acesso à lista de confirmados.

Após autenticação, o administrador é redirecionado para:

* `/informacoes`

---

## 📄 Persistência de Dados

Os dados das confirmações são salvos em:

```
app/confirmados.json
```

Formato exemplo:

```json
[
  {
    "nome": "João",
    "telefone": "81999999999",
    "confirmacao": "Sim",
    "quantidade": 2,
    "observacao": "Sem restrições"
  }
]
```

---

## 🌐 Possível Publicação Online

O projeto pode ser facilmente publicado em plataformas como:

* Render
* Railway
* PythonAnywhere

Basta configurar:

* `requirements.txt`
* variável de ambiente para a senha do admin

---

## 👨‍💻 Autor

Projeto desenvolvido por **Pedro Barbosa**, como aplicação prática de Flask e persistência de dados sem banco de dados.

---

## 📌 Observações

* Projeto ideal para pequenos eventos
* Estrutura simples, organizada e fácil de manter
* Ótimo para portfólio e freelancing

---

✨ Fique à vontade para evoluir o projeto com autenticação completa, banco de dados ou deploy em produção.
