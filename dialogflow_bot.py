import os
import logging
from google.cloud import dialogflow_v2 as dialogflow

# Configuração de Logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class DialogflowClient:
    def __init__(self, credentials_path: str, project_id: str, language_code: str = "pt-BR"):
        """
        Inicializa o cliente Dialogflow.

        Args:
            credentials_path (str): Caminho para o arquivo JSON de credenciais.
            project_id (str): ID do projeto no Google Cloud.
            language_code (str): Código do idioma (padrão: pt-BR).
        """
        self.project_id = project_id
        self.language_code = language_code
        self._setup_credentials(credentials_path)
        self.session_client = dialogflow.SessionsClient()

    @staticmethod
    def _setup_credentials(credentials_path: str):
        """Configura o ambiente para usar o arquivo de credenciais."""
        if not os.path.exists(credentials_path):
            logging.error(f"Arquivo de credenciais não encontrado: {credentials_path}")
            raise FileNotFoundError(f"Arquivo de credenciais não encontrado: {credentials_path}")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
        logging.info("Credenciais configuradas com sucesso.")

    def detect_intent(self, session_id: str, text: str):
        """
        Detecta a intenção de uma mensagem enviada ao Dialogflow.

        Args:
            session_id (str): ID da sessão do usuário.
            text (str): Texto enviado pelo usuário.

        Returns:
            dict: Dicionário contendo a pergunta, a intenção detectada e a resposta do bot.
        """
        try:
            session_path = self.session_client.session_path(self.project_id, session_id)
            text_input = dialogflow.TextInput(text=text, language_code=self.language_code)
            query_input = dialogflow.QueryInput(text=text_input)

            response = self.session_client.detect_intent(
                request={"session": session_path, "query_input": query_input}
            )

            return {
                "Pergunta": response.query_result.query_text,
                "Intenção": response.query_result.intent.display_name,
                "Confiança": response.query_result.intent_detection_confidence,
                "Resposta": response.query_result.fulfillment_text,
            }
        except Exception as e:
            logging.error(f"Erro ao detectar intenção: {e}")
            return {"Erro": str(e)}

    def detect_intent_batch(self, session_id: str, texts: list):
        """
        Processa múltiplas mensagens em sequência.

        Args:
            session_id (str): ID da sessão do usuário.
            texts (list): Lista de mensagens enviadas pelo usuário.

        Returns:
            list: Lista de respostas do bot para cada mensagem.
        """
        results = []
        for text in texts:
            result = self.detect_intent(session_id, text)
            results.append(result)
        return results


# Configurações do cliente Dialogflow
credentials_path = "projeto-fabiano/credenciais.json"
project_id = "projeto-fabiano"
language_code = "pt-BR"

# Inicializando o cliente
dialogflow_client = DialogflowClient(credentials_path, project_id, language_code)

# IDs e textos de exemplo
session_id = "Bruno 123 :D"
texts = ["Treinamento de LLMs?", "Desenvolvimento de chatbots de atendimento e autosserviço com inteligência artificial generativa humanizada?", "mecanismos de busca humanizada com IA?" "Automatização de processos, com ou sem o uso de IA, por meio de plataformas no-code/low-code e chatbots"]

# Processando múltiplas mensagens
responses = dialogflow_client.detect_intent_batch(session_id, texts)

# Exibindo resultados
for response in responses:
    logging.info("Resposta do Bot:")
    for key, value in response.items():
        logging.info(f"{key}: {value}")
