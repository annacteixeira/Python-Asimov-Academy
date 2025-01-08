from typing import Any, Dict, Type
from pydantic import BaseModel
from langchain.tools import BaseTool
from repositories.user import UserRepository
from models import User

class UserRegistrationTool(BaseTool):
    name: str = 'user_registration'
    
    description: str = (
    "Use esta ferramenta para registrar um novo usuário ou atualizar as informações de um usuário existente. "
    "Esta ferramenta requer os seguintes dados do usuário: "
    "telegram_id, name (nome), gender (gênero), age (idade como uma string), height_cm (altura em centímetros como uma string), weight_kg (peso em quilogramas como uma string), "
    "has_diabetes (se tem diabetes: sim/não) e goal (objetivo: perder peso, ganhar peso, ganhar massa muscular). "
    "Se algum dado estiver faltando, você deve primeiro coletar essas informações do usuário antes de usar esta ferramenta."
    )
    
    args_schema: Type[BaseModel] = User
    
    def __init__(self):
        super().__init__()
        self._user_repo = UserRepository()
        
    def _run(self,
        telegram_id: int,
        name: str,
        gender: str,
        age: str,
        height_cm: str,
        weight_kg: str,
        has_diabetes: str,
        goal: str        
    ) -> str:
        if not name:
            raise AttributeError('Os atributos inseridos na Tool UserRegistration não podem ser vazios')
        
        try:
            user_data = {
                'telegram_id': telegram_id,
                'name': name,
                'gender': gender,
                'age': age,
                'height_cm': height_cm,
                'weight_kg': weight_kg,
                'has_diabetes': has_diabetes,
                'goal': goal
            }
            
            user = self._user_repo.get_user_by_telegram_id(telegram_id)
            if user:
                updated_user = self._user_repo.update_user(**user_data)
                return f'Informações atualizadas com sucesso.'
            
            new_user = self._user_repo.create_user(**user_data)
            return f'Usuário registrado com sucesso.'
        
        except Exception as err:
            return f'Erro ao registrar o usuário: {str(err)}'
    
    async def _arun(self, user_data: Dict[str, Any]) -> str:
        raise NotImplementedError('Execução assíncrona não suportada.')
    