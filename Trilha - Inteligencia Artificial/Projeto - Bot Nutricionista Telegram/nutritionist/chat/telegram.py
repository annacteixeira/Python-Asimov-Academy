import logging
import asyncio
import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyrogram.enums import ChatAction
from agents.nutritionist import NutritionistAgent

load_dotenv()

class TelegramBot:
    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        
        self.logger = logging.getLogger(__name__)
        
        self.app = Client(
            api_id=os.getenv('TELEGRAM_API_ID'),
            api_hash=os.getenv('TELEGRAM_API_HASH'),
            bot_token=os.getenv('TELEGRAM_TOKEN'),
            name='NutriIntelligenceBot'
        )
        
        self._setup_handlers()
        
    def _setup_handlers(self):
        start_handler = MessageHandler(
            self.start,
            filters.command('start') & filters.private
        )
        self.app.add_handler(start_handler)
        
        text_filter = filters.text & filters.private
        message_handler = MessageHandler(
            self.handle_message,
            text_filter
        )
        self.app.add_handler(message_handler)
        
        photo_filter = filters.photo & filters.private
        photo_handler = MessageHandler(
            self.handle_photo,
            photo_filter
        )
        self.app.add_handler(photo_handler)
    
    async def start(self, client: Client, message: Message):
        await message.reply_text(
            'Olá! Eu sou sua IA Nutricionista. Envie uma mensagem ou uma foto de um prato de comida para começar.'
        )
        self.logger.info(f'Usuário {message.from_user.id} iniciou uma conversa.')
        
    async def handle_message(self, client: Client, message: Message):
        user_id = message.from_user.id
        user_input = message.text
        
        await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        
        agent = NutritionistAgent(session_id=str(user_id))
        
        try:
            response = agent.run(f'telegram_id: {user_id} ' + f'mensagem: {user_input}')
        except Exception as e:
            self.logger.error(f'Erro ao processar a mensagem do usuário {user_id}: {e}', exc_info=True)
            response = 'Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente.'
            
        await message.reply_text(response)
        self.logger.info(f'Resposta enviada para o usuário {user_id}.')
        
    async def handle_photo(self, client: Client, message: Message):
        user_id = message.from_user.id
        
        await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        
        storage_dir = os.path.join(os.getcwd(), 'storage')
        os.makedirs(storage_dir, exist_ok=True)
        
        photo_file_name = f'{user_id}_{message.photo.file_id}.jpg'
        photo_path = os.path.join(storage_dir, photo_file_name)
        
        await message.download(file_name=photo_path)
        
        agent = NutritionistAgent(session_id=str(user_id))
        
        try:
            response = agent.run(photo_path)
        except Exception as e:
            self.logger.error(f'Erro ao processar a mensagem do usuário {user_id}: {e}', exc_info=True)
            response = 'Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente.'
            
        await message.reply_text(response)
        self.logger.info(f'Resposta enviada para o usuário {user_id}.')

    def run(self):
        self.logger.info('Bot iniciado.')
        self.app.run()