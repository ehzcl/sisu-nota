import requests
import json

# gerar lista de categorias
r = requests.get('https://sisu-api.sisu.mec.gov.br/api/v1/oferta/categoria')
with open('categorias.json', 'wb') as file:
  file.write(r.content)
print('O codigo do curso pode ser encontrado no arquivo categorias.json que foi gerado (pode ser aberto em um navegador)')

# para conseguir o curso
codigo = input("por favor digite o codigo do curso:\n")
j = requests.get(f"https://sisu-api.sisu.mec.gov.br/api/v1/oferta/curso/{codigo}").json()

faculdades = []
for i in range(len(j)-1):
# como as chaves sao strings usaremos f-strings
  faculdades.append(j[f"{i}"]['co_oferta'])

# adicao do token para a requisicao
print("faca o processo de obtencao do token descrito no repositorio e cole o texto a partir do Bearer aqui")
token = input()

# informacoes das vagas
vagas = []
for vaga in faculdades:
  v = requests.get(f"https://sisualuno-api.sisualuno.mec.gov.br/api/v1/oferta/{vaga}/modalidades/candidato",headers={'Authorization':f"{token}"}).json()
  vagas.append(v)
  #### ****DESCOMENTE A LINHA ABAIXO SE QUISER VERIFICAR OS CODIGOS DAS MODALIDADES**** ####
  # f = open(f"{vaga}",'w'); f.write(v); f.close()

# criacao do arquivo do arquivo de planilha
# o modo esta como append para ser possivel salvar resultados das execucoes anteriores para comparacao
pl = open('planilha.csv','a')

# Aqui sao as colunas da planilha
pl.write('SIGLA, UNIVERSIDADE, CAMPUS, UF, AMPLA CONC, ESCOLA PUB BR, ESCOLA PUB,AMPLA CONC USUARIO, ESCOLA PUB BR USUARIO, ESCOLA PUB USUARIO,\n')

for vaga in vagas:
  j = vaga
  # informacoes universidade
  sigla = j['oferta']['sg_ies']
  nome_uni = j['oferta']['no_ies']
  campus = j['oferta']['no_municipio_campus']
  uf = j['oferta']['sg_uf_ies']
  ac = 0;ep_br =0;ep = 0;acu = 0;ep_bru =0;epu = 0
  for i in range(len(j['modalidades'])):
    # checar a modalidade
    # ampla concorrencia
    if j['modalidades'][i]['co_concorrencia'] == '0':
      ac = j['modalidades'][i]['nu_nota_corte']
      acu = j['modalidades'][i]['nu_nota_candidato']
    # baixa renda
    # Escola Publica
    elif j['modalidades'][i]['co_concorrencia'] == '9028':
      ep_br = j['modalidades'][i]['nu_nota_corte']
      ep_bru = j['modalidades'][i]['nu_nota_candidato']
    # independente de renda
    # Escola Publica
    elif j['modalidades'][i]['co_concorrencia'] == '9029':
      ep = j['modalidades'][i]['nu_nota_corte']
      epu = j['modalidades'][i]['nu_nota_candidato']
    qtvaga = j['modalidades'][i]['qt_vagas']
  pl.write(f"{sigla},{nome_uni},{campus},{uf},{ac},{ep_br},{ep},{acu},{ep_bru},{epu}\n")
pl.close()
