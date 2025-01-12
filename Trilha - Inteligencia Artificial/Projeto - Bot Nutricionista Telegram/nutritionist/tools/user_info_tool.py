from langchain.tools import BaseTool
from repositories.user import UserRepository

class UserInfoTool(BaseTool):
    _user_repo = UserRepository
    name: str = 'user_info'
    description: str = (
        "Use esta ferramenta para buscar informações de um usuário existente. "
        "Ela requer o telegram_id do usuário como entrada para recuperar os dados."
    )
    
        
    def _run(self, telegram_id: int) -> str:
        try:
            user = self._user_repo.get_user_by_telegram_id(telegram_id)
            if not user:
                return f'Usuário não encontrado.'
            
            user_info = (
                f'Nome: {user.name}\n'
                f'Gênero: {user.gender}\n'
                f'Idade: {user.age}\n'
                f'Altura: {user.height_cm} cm\n'
                f'Peso: {user.weight_kg} kg\n'
                f'Diabético: {"Sim" if user.is_diabetic else "Não"}\n'
                f'Objetivo: {user.goal}\n'
            )
            
            return user_info
        except Exception as err:
            return f'Erro ao retornar informações do usuário: {str(err)}'
    
    async def _arun(self, telegram_id: int) -> str:
        raise NotImplementedError('Execução assíncrona não suportada.')
    
    
    