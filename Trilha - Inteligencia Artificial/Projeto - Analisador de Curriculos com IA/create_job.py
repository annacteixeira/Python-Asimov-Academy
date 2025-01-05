from database import AnalyzeDatabase
from models.job import Job
import uuid

database = AnalyzeDatabase()

# Vaga encontrada no LinkedIn https://www.linkedin.com/jobs/search/?currentJobId=4108476401&geoId=106057199&keywords=Estagiário%20de%20engenharia%20de%20software&origin=JOB_SEARCH_PAGE_LOCATION_HISTORY&refresh=true


name = 'Estágio em Engenharia de Software (Front-end)'

main_activities = '''
Responsável em apoiar o time de LTV na construção e manutenção das plataformas de software da Pier, majoritariamente na camada de front-end.
Trabalhar na construção e manutenção dos softwares da Pier (app, backoffice, site) majoritariamente na camada de front-end;
Auxiliar a equipe na elaboração de novas soluções, participando de discussões de arquitetura, etc;
Colaborar no desenvolvimento novas funcionalidades e componentes front-end, seguindo as melhores práticas de desenvolvimento;
Apoiar nos testes unitários e de integração, identificando e corrigindo bugs.
'''

pre_requisites ='''
Ensino superior cursando em Análise e Desenvolvimento de Sistema, Engenharia de Software, Ciência da Computação ou áreas relacionadas;
Formação prevista entre 2026/1 e 2027/1
Conhecimento sobre boas práticas de programação;
Conhecimento básico de linguagens como Javascript.
'''

differentials ='''
Conhecimento básico de ReactJS;
Conhecimento básico em React Native. 
'''

job = Job(
    id=str(uuid.uuid4()), 
    name=name, 
    main_activities=main_activities, 
    pre_requisites=pre_requisites, 
    differentials=differentials
)

database.jobs.insert(job.model_dump())