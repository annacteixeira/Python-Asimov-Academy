from langchain.tools import BaseTool
from typing import Any, Dict, Optional
from repositories.meal_entry import MealEntryReppository
from repositories.user import UserRepository

class MealEntryTool(BaseTool):
    _user_repo = UserRepository
    _meal_entry_repo = MealEntryReppository
    name: str = "meal_entry_tool"
    description: str = (
        "Ferramenta para toda vez que o usuário quiser que você registre uma refeição que ele fez no dia. "
        "Se você nao tiver todos os dados para registrar uma refeição, pergunte ao usuário até que tenha todas as informações necessarias."
        "Use esta ferramenta para registrar uma refeição de um usuário. "
        "Entrada: como meal_description, calories, carbs, proteins, fats."
        "Você deve se basear nas informações que o usuário passou para gerar as informações de calories, carbs, proteins, fats"
    )

    def _run(
        self,
        telegram_id: int,
        meal_description: str,
        image_path: Optional[str] = None,
        calories: Optional[str] = None,
        carbs: Optional[str] = None,
        proteins: Optional[str] = None,
        fats: Optional[str] = None,
    ) -> str:
        
        try:
            user = self._user_repo.get_user_by_telegram_id(telegram_id)
            if not user:
                return 'Usuário não encontrado. Por favor, registre o usuário primeiro'
            
            self._meal_entry_repo.create_meal_entry(
                user_id=telegram_id,
                meal_description=meal_description,
                image_path=image_path,
                calories=calories,
                carbs=carbs,
                proteins=proteins,
                fats=fats,
            )
            
            return f'Refeição registrada com sucesso para {user.name}.'
        except Exception as err:
            return f'Erro no registro de refeição: {str(err)}.'
    
    async def _arun(self, telegram_id: int, meal_data: Dict[str, Any]) -> str:
        raise NotImplementedError('Execução assíncrona não suportada.')