from langchain.tools import BaseTool
from nutritionist.repositories.user import UserRepository
from nutritionist.repositories.weight_history import WeightHistoryRepository

class WeightUpdateTool(BaseTool):
    name: str = 'weight_update'
    description: str = (
        "Use esta ferramenta para registrar o peso de um usuário. "
        "Entrada: telegram_id do usuário e weight_kg."
    )
    
    def __init__(self):
        super().__init__()
        self._user_repo = UserRepository()
        self._weight_history_repo = WeightHistoryRepository()
        
    def _run(self, telegram_id: int, weight_kg: str) -> str:
        try:
            user = self._user_repo.get_user_by_telegram_id(telegram_id)
            if not user:
                return 'Usuário não encontrado. Por favor, registre o usuário antes de atualizar o peso.'
            
            self._weight_history_repo.add_weight_history(telegram_id, weight_kg)
            return f'Peso atualizado com sucesso para {user.name}.'
        except Exception as err:
            return f'Erro na ferramenta de atualização de peso: {str(err)}'
        
    async def _arun(self, weight_kg: float) -> str:
        raise NotImplementedError('Execução assíncrona não suportada.')