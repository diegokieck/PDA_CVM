from bs4 import BeautifulSoup as bs
import requests

#Contantes:
#Repositorio remoto dos dados
REPOSITORY = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/"
#Pasta para copias locais
LOCAL_FILES_FOLDER = "Tabelas_Locais/"
#Log para versionamento das copias locais
LOCAL_FILES_LOG = "local_files.txt"

#Carrega em memória o log de copias locais
def carregar_arquivos_locais(f):
	print('chamou_carregar')
	arquivos_locais = {}
	while (True):
		try:
			line = next(f)
			nome , data = line.split()
			arquivos_locais.update({nome:data})
        	# code
		except StopIteration:
			break
	return arquivos_locais

#Compara a nova copia dos dados com a copia local
#e atualiza a diferenca no banco 
def atualiza_banco():
	pass


#recebe dicionario com (nome, data) e grava em arquivo com nome
#LOCAL_FILES_LOG
def escreve_log_local(arquivos_locais_dict):
	with open(LOCAL_FILES_LOG, 'wt') as f:
		for key in arquivos_locais_dict:
			string = key + " " + arquivos_locais_dict[key] + "\n"
			f.write(string)


"""
recebe dicionario com (nome, data) dos arquivos locais e busca em
REPOSITORY os arquivos csv. Para cada arquivo, compara se existe
uma copia local atualizada. Quando nao estiver atualizada, recupera
o arquivo, salva, atualiza LOCAL_FILES_LOG e atualiza o banco. 
"""
def atualizar_arquivos_locais(arquivos_locais):
	page = requests.get(REPOSITORY)
	soup = bs(page.content, 'html.parser')
	rows = soup.find_all(True, {'class' :["even", 'odd']})
	#Para cada arquivo verificar se a versão local está atualizada
	for row in rows[2:]:
		row = list(row.children)[1:3]
		row_link = row[0].find('a', href=True)
		row_name = row[0].get_text()
		row_date = row[1].get_text()
		print("name ", row_name, "\n",
			"date", row_date, "\n"
			"link: ",row_link['href'])
		#SE ARQUIVO NOVO, ATUALIZA O DICIONARIO E SALVA LOCALMENTE
		if (row_name not in arquivos_locais.keys()):
			arquivos_locais.update({row_name:row_date})
			content = requests.get(REPOSITORY + row_link['href'])
			with open(LOCAL_FILES_FOLDER + row_name, 'wb') as f:
				f.write(content.content)
			print(content.status_code)

	escreve_log_local(arquivos_locais)
		#SE ARQUIVO DESATUALIZADO, ATUALIZA DATA E EFETUA 
		
	return 1

if __name__ == '__main__':
	print('chamou main')
	# verificar se o LOCAL_FILES_LOG existe
	try:
		f = open(LOCAL_FILES_LOG, 'r+')
		arquivos_locais = carregar_arquivos_locais(f)
	except Exception as e:
		f = open (LOCAL_FILES_LOG, 'wt')
		arquivos_locais={}
	atualizar_arquivos_locais(arquivos_locais)
	





