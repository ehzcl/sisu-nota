# Comparador de Notas SISU
#### Requisitos
requests
pode ser instalado com o pip
```bash
pip install requests
```
#### Como Usar
##### Primeiros Passos (conseguir os links do curso)
execute o script e quando ele solicitar o codigo do curso abra o arquivo categories.json que foi gerado onde o script foi executado
![image](https://github.com/ehzcl/sisu-nota/assets/32335520/13012703-7a9b-4fb6-91ac-7c75af23942d)
A imagem abaixo mostra a visualizacao do JSON no Firefox, pode ser um pouco diferente em outro navegador
![image](https://github.com/ehzcl/sisu-nota/assets/32335520/307c93a9-a8e9-46a4-bc2f-226fdfa3f675)



##### Obter notas do usuario via api
1. Logue no SISU https://sisualuno.mec.gov.br/#/login
2. Abra as ferramentas de desenvolvedor (3 pontinhos > mais ferramentas > Ferramentas de desenvolvedor), isso sera usado para pegar o token de autenticacao
3. deixe a aba redes aberta e coloque o texto a seguir na barra de pesquisa assim como na imagem abaixo
   modalidades/candidato
   ![image](https://github.com/ehzcl/sisu-nota/assets/32335520/f5755167-fb31-4e0e-8cb6-b4c34def8e58)
5. Acesse alguma vaga em qualquer universidade
6. Copie o codigo como na imagem abaixo
![image](https://github.com/ehzcl/sisu-nota/assets/32335520/d5e0fe79-7eff-438a-8ba9-174eea96cd92)
7. Cole no terminal (neste caso estamos usando o codigo do curso de medicina)
   ![image](https://github.com/ehzcl/sisu-nota/assets/32335520/d6d18a03-ef44-453c-90f8-0db545a4b642)
8. Este codigo esta levando em consideracao apenas Escola Publica Baixa Renda/Independente de renda e um tipo de ampla concorrencia (o com codigo 0)
9. Entao sera gerado um arquivo chamado planilha.csv podendo ser jogado no Planilhas google ou qualquer outro visualizador de planilhas para uma melhor visualizacao e interacoes
10. Se quiser adicionar novas possibilidades basta descomentar a linha do For Loop de faculdades
11. e rodar o seguinte comando (se tiver o jq instalado claro)
```bash
jq '.modalidades[] | "\(.co_concorrencia) \(.no_concorrencia)"' * | uniq
```
que da como resultado algo similar a imagem abaixo
![image](https://github.com/ehzcl/sisu-nota/assets/32335520/82a53df6-f0db-4456-b405-1efb95666236)
ai basta adicionar uma condicao para os novos codigos e nao esquecer de adicionar na escrita do CSV
![image](https://github.com/ehzcl/sisu-nota/assets/32335520/ff6f0643-0ffa-4528-9a6d-335205a547f4)

