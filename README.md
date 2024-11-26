Apresenta-o_Fabiano
🚀 Chatbot com Google Dialogflow e Google Cloud
Um chatbot básico utilizando a API Dialogflow do Google Cloud para responder a perguntas em português.

<div align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Google%20Cloud-Dialogflow-orange?style=for-the-badge&logo=google-cloud&logoColor=white"> <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge"> </div>
📝 Descrição
Este projeto implementa um chatbot utilizando o serviço Dialogflow integrado à Google Cloud Platform (GCP). Ele processa mensagens enviadas pelo usuário e retorna respostas pré-configuradas baseadas em intenções e treinamento.

Principais Funcionalidades:
✅ Integração com a API Dialogflow.
✅ Processamento de perguntas em português (pt-BR).
✅ Fácil configuração e uso.
✅ Código organizado em classes para reutilização.
🛠️ Pré-requisitos
Antes de começar, verifique se você tem os seguintes itens instalados:

Python 3.10 ou superior
Conta na Google Cloud Platform com o serviço Dialogflow configurado.
Arquivo de credenciais JSON da GCP.
Instale as dependências:
No terminal, execute:

bash
Copiar código
pip install -r requirements.txt
🚀 Como Usar
Clone o repositório:
bash
Copiar código
git clone https://github.com/BrunoRbt/Apresenta-o_Fabiano
cd apresenta_o_fabiano
Configure as credenciais: Coloque o arquivo credenciais.json no diretório raiz do projeto.

Edite o arquivo main.py: Configure os parâmetros do seu projeto:

python
Copiar código
project_id = "seu-id-do-projeto"
session_id = "sua-sessao-id"
texts = ["Qual é o seu nome?", "O que você faz?"]
language_code = "pt-BR"
Execute o chatbot:
bash
Copiar código
python main.py
🌐 Integração com Interface Web
Para usar uma interface HTML, siga os seguintes passos:

Instale o Flask:
bash
Copiar código
pip install flask
Conecte o arquivo index.html ao Flask no script main.py.

Inicie o servidor:

bash
Copiar código
python main.py
Acesse o chatbot no navegador:
bash
Copiar código
http://127.0.0.1:5000
🛡️ Boas Práticas
Nunca inclua o arquivo credenciais.json no repositório GitHub! Utilize o arquivo .gitignore para proteger suas credenciais.
Use ambientes virtuais (venv) para isolar dependências.
Formate seu código com o Black:
bash
Copiar código
pip install black
black .
🧩 Tecnologias Utilizadas
<div align="center"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white"> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"> </div>
🗂️ To-Do
Melhorar a interface web.
Adicionar suporte para outras linguagens.
Implementar autenticação via OAuth 2.0.
🤝 Contribuindo
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

Faça um fork do repositório.
Crie sua branch de recurso (git checkout -b feature/nome-recurso).
Commit suas mudanças (git commit -m 'Adicionei um novo recurso').
Faça o push para sua branch (git push origin feature/nome-recurso).
Abra um Pull Request.
📜 Licença
Este projeto está licenciado sob a MIT License.

💬 Contato
E-mail: richard2oliver1@gmail.com
GitHub: https://github.com/BrunoRbt
LinkedIn: https://www.linkedin.com/in/bruno-roberto-devr/
