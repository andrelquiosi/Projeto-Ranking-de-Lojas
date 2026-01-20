# Passo 1: pegar cada base de dados
# Passo 2: para cada base de dados:
#     -vou calcular o faturamento total de cada loja
# Passo 3: Criar ranking com o faturamento total de todas as lojas
# Passo 4: Enviar por email esse ranking

import pandas as pd
import yagmail
from dotenv import load_dotenv, dotenv_values
load_dotenv()

lojas = ['BH', 'SP', 'Manaus', 'Rio', 'DF', 'Salvador']

faturamentos = {}
for loja in lojas:
    df = pd.read_excel(f"Lojas/Loja {loja}.xlsx")
    faturamentos[loja] = sum(df['Vendas'])

ranking_lojas = pd.DataFrame.from_dict(faturamentos, orient='index', columns=['Vendas'])
ranking_lojas = ranking_lojas.sort_values(by='Vendas', ascending=False)
ranking_lojas = ranking_lojas.map("R${:,.2f}".format)

mensagem = f"""Prezados, segue abaixo o ranking de vendas de cada loja:

{ranking_lojas.to_string().replace(' ', '-')}

Qualquer duvida sobre o ranking, favor entrar em contato com a equipe de vendas.

Att.
Equipe de Vendas"""

email = dotenv_values()['EMAIL_USER']
senha = dotenv_values()['EMAIL_PASSWORD']
usuario = yagmail.SMTP(user=email, password=senha)
usuario.send(to=email, subject='Ranking de Vendas', contents=mensagem)