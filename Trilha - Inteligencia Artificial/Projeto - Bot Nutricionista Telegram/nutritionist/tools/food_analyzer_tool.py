import base64
from io import BytesIO
from langchain.tools import BaseTool
from PIL import Image
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

class FoodImageAnalyzerTool(BaseTool):
    name: str = 'food_image_analyzer'
    description: str = '''
        Utilize esta ferramenta para analisar imagens de pratos de comida que o usuário enviar.
        Descreva os alimentos presentes e crie uma tabela nutricional da refeição.
        
        O agente deve usar esta ferramenta sempre que um caminho de imagem for fornecido, mas somente
        quando o input for um caminho de imagem.
    '''
    
    def _run(self, image_path: str) -> str:
        image = Image.open(image_path)
        buffered = BytesIO()
        image.save(buffered, format='JPEG')
        img_b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        instructions = '''
            Você deve analisar a imagem enviada e verificar se ela contém um prato de comida.
            Caso seja um prato de comida, descreva os itens visíveis no prato e crie uma descrição nutricional
            detalhada e estimada incluindo calorias, carboidratos, proteínas e gorduras. Forneça uma descrição
            nutricional completa da refeição.
        '''
        
        llm=ChatOpenAI(
            model='gpt-4o-mini'
        )
        
        message = [HumanMessage(
            content=[
                {'type': 'text', 'text': instructions},
                {'type': 'image_url', 'image_url': {'url': f'data:image/jpeg;base64,{img_b64}'}}
            ]
        )]
        
        response = llm.invoke(message)
        
        return response        
        
    async def _arun(self, image_path: str) -> str:
        raise NotImplementedError('Execução assíncrona não suportada.')