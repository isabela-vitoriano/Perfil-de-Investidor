# Importando função da biblioteca para deixar o programa mais dinâmico ao informar um erro.

from time import sleep 

# Definindo as variáveis

con = 0
mod = 0
ous = 0
q = 0

# Realizando o questionário

print('='*150)
print('''Você sabe qual o seu perfil de investidor?

Bancos e corretoras geralmente classificam o investidor em um dos três perfis: Conversador, Moderado e Agressivo. Dessa forma, recomendam a aplicação mais adequada. Assim, é de suma importância ter o autoconhecimento sobre seu perfil.
Importante salientar que há uma limitação desse tipo de teste em definir precisamente o perfil real de um investidor, porém é um bom guia inicial.''')
print('='*150)

print('Vamos iniciar o questionário!')

sleep(3)

while q != 1 and q != 2 and q !=3:
  q = int(input('''
Qual é a sua idade?

  [ 1 ] Até 30 anos
  [ 2 ] Entre 30 e 50 anos
  [ 3 ] Acima de 50 anos

Resposta: '''))
  if q == 1:
    ous += 1
  elif q == 2:
    mod += 1
  elif q == 3:
    con += 1
  else:
    print('\nDigite apenas o número "1", "2" ou "3", sem aspas.')
    sleep(2)

q = 0
while q != 1 and q != 2 and q !=3:
  q = int(input('''
O quanto você acompanha e sabe sobre o mercado financeiro?

  [ 1 ] Não acompanho as notícias 
  [ 2 ] Acompanho de vez em quando o mercado, ou somente as notícias mais comentadas e de maior destaque
  [ 3 ] Acompanho com frequência as notícias e mudanças do mercado

Resposta: '''))
  if q == 1:
    con += 1
  elif q == 2:
    mod += 1
  elif q == 3:
    ous += 1
  else:
    print('\nDigite apenas o número "1", "2" ou "3", sem aspas.')
    sleep(2)

q = 0
while q != 1 and q != 2 and q !=3:
  q = int(input('''
Qual a sua renda?

  [ 1 ] Até 2 mil reais
  [ 2 ] Entre 2 e 5 mil reais
  [ 3 ] Acima de 5 mil reais

Resposta: '''))
  if q == 1:
    con += 1
  elif q == 2:
    mod += 1
  elif q == 3:
    ous += 1
  else:
    print('\nDigite apenas o número "1", "2" ou "3", sem aspas.')
    sleep(2)

q = 0
while q != 1 and q != 2 and q !=3:
  q = int(input('''
Dentro de sua renda, qual % você deseja investir?

  [ 1 ] Até 20% da renda
  [ 2 ] Entre 20% e 40% da renda
  [ 3 ] Acima de 40%

Resposta: '''))
  if q == 1:
    con += 1
  elif q == 2:
    mod += 1
  elif q == 3:
    ous += 1
  else:
    print('\nDigite apenas o número "1", "2" ou "3", sem aspas.')
    sleep(2)

q = 0
while q != 1 and q != 2 and q !=3:
  q = int(input('''
Qual o prazo que você deseja manter o seu investimento?

  [ 1 ] Curto prazo [menos de 2 anos]
  [ 2 ] Médio prazo [entre 2 e 5 anos]
  [ 3 ] Longo prazo [acima de 5 anos]

  Resposta: '''))
  if q == 1:
    con += 1
  elif q == 2:
    mod += 1
  elif q == 3:
    ous += 1
  else:
    print('\nDigite apenas o número "1", "2" ou "3", sem aspas.')
    sleep(2)

q = 0
while q != 1 and q != 2 and q !=3:
  q = int(input('''
Qual o seu objetivo ao investir?

  [ 1 ] Especular, ter alta valorização, correndo riscos maiores, se necessário
  [ 2 ] Acumular recursos, obter rentabilidade acima da inflação
  [ 3 ] Preservar meu patrimônio, corrigir os investimentos pela variação da inflação

  Resposta: '''))
  if q == 1:
    ous += 1
  elif q == 2:
    mod += 1
  elif q == 3:
    con += 1
  else:
    print('\nDigite apenas o número "1", "2" ou "3", sem aspas.')
    sleep(2)

q = 0
while q != 1 and q != 2 and q !=3:
  q = int(input('''
Qual a sua opinião sobre a segurança?

  [ 1 ] Poderia aceitar perdas na tentativa de obter retornos elevados
  [ 2 ] Poderia aceitar perdas ocasionais em busca de retornos maiores, desde que não signifiquem perdas muito altas em relação ao total investido
  [ 3 ] Não gostaria de perder dinheiro, mesmo que isso signifique menor rentabilidade

  Resposta: '''))
  if q == 1:
    ous += 1
  elif q == 2:
    mod += 1
  elif q == 3:
    con += 1
  else:
    print('\nDigite apenas o número "1", "2" ou "3", sem aspas.')
    sleep(2)

# Resultado do teste

if  mod>con and mod>ous or ous==con>mod:
  print('\nVocê é moderado.')
  print('''O investidor com perfil moderado gosta de segurança, mas aceita algum tipo de risco para obter retornos acima da média, além de já possuir um certo conhecimento sobre investimentos. Com isso, busca uma rentabilidade que supere a inflação, obtendo ganhos para o seu patrimônio. Por isso, aceita assumir um pouco de risco, diversificando seu portfólio de investimentos entre renda fixa e variável.
#Dica → Experimente investir em:
- Investimentos mesclados: títulos de baixo risco e fundos de investimentos, como os cambiais.''')

elif con>mod and con>ous:
  print('\nVocê é conservador.')
  print('''O investidor com perfil conversador é avesso ao risco, e se guia pela vontade de preservação do capital que investiu. Dessa forma, busca produtos de investimentos que objetivam a preservação do patrimônio e garantam segurança.
#Dica → Experimente investir em:
- Caderneta de poupança e títulos de baixo risco, públicos (Tesouro Nacional) ou privados (LCA, LCI e CDB).''')

elif ous>mod and ous>con:
  print('\nVocê é ousado.')
  print('''O investidor com perfil ousado possui grande conhecimento e domínio sobre investimentos, e busca retornos grande, mesmo que isso envolva riscos. Busca retornos expressivos, com rentabilidade para o seu patrimônio. Para isso, lidam com naturalidade com prejuízos, suportando os riscos. Assim, costumam a aplicar mais da metade de seus recursos em produtos de renda variável.
#Dica → Experimente investir em:
- Bolsa de Valores e mercados de futuros, e derivativos.''')

elif mod==con>ous:
  print('\nVocê é um misto de moderado com conservador.')
  print('''O investidor com perfil conversador é avesso ao risco, e se guia pela vontade de preservação do capital que investiu. Dessa forma, busca produtos de investimentos que objetivam a preservação do patrimônio e garantam segurança.
Já o investidor com perfil conversador é avesso ao risco, e se guia pela vontade de preservação do capital que investiu. Dessa forma, busca produtos de investimentos que objetivam a preservação do patrimônio e garantam segurança.
#Dica → Experimente investir em:
- Caderneta de poupança e títulos de baixo risco, públicos (Tesouro Nacional) ou privados (LCA, LCI e CDB).''')

elif mod==ous>con:
  print('\nVocê é um misto de moderado com ousado.')
  print('''O investidor com perfil conversador é avesso ao risco, e se guia pela vontade de preservação do capital que investiu. Dessa forma, busca produtos de investimentos que objetivam a preservação do patrimônio e garantam segurança.
Já o investidor com perfil ousado possui grande conhecimento e domínio sobre investimentos, e busca retornos grande, mesmo que isso envolva riscos. Busca retornos expressivos, com rentabilidade para o seu patrimônio. Para isso, lidam com naturalidade com prejuízos, suportando os riscos. Assim, costumam a aplicar mais da metade de seus recursos em produtos de renda variável.
#Dica → Experimente investir em:
- Investimentos mesclados: títulos de baixo risco e fundos de investimentos, como os cambiais.''')