# Passo 1: pegar cada base de dados
# Passo 2: para cada base de dados:
#           calcular o faturamento total de cada loja
#           Calcular o ranking dos 3 maiores vendedores por loja
# Passo 3: Criar ranking com o faturamento total de todas as lojas
# Passo 4: Enviar por email esse ranking

import pandas as pd
import yagmail
from dotenv import load_dotenv, dotenv_values

load_dotenv()

lojas = ["BH", "SP", "Manaus", "Rio", "DF", "Salvador"]


def calcular_faturamentos_e_melhores_vendedores():
    faturamentos = {}
    melhores_vendedores_por_loja = {}
    for loja in lojas:
        df = pd.read_excel(f"Lojas/Loja {loja}.xlsx")
        faturamentos[loja] = sum(df["Vendas"])
        melhores_vendedores_por_loja[loja] = df.sort_values(
            by="Vendas", ascending=False
        ).head(3)
    return faturamentos, melhores_vendedores_por_loja


def ranking_lojas(faturamentos):
    ranking_lojas = pd.DataFrame.from_dict(
        faturamentos, orient="index", columns=["Vendas"]
    )
    ranking_lojas = ranking_lojas.sort_values(by="Vendas", ascending=False)
    ranking_lojas = ranking_lojas.map("R${:,.2f}".format)
    return ranking_lojas.to_html(index=False, border=1, justify="center")


def ranking_vendedores(melhores_vendedores_por_loja):
    email_html = ""

    for cidade, df in melhores_vendedores_por_loja.items():
        email_html += f"<h3>{cidade}</h3>"
        df["Vendas"] = df["Vendas"].map("R${:,.2f}".format)
        email_html += df.to_html(index=False, border=1, justify="center")

    return email_html


def enviar_email(faturamentos: dict, melhores_vendedores_por_loja: dict):
    mensagem = f"""<html><body>
    <h3>Prezados, segue abaixo o ranking de vendas de cada loja:</h3>
    {ranking_lojas(faturamentos)}
    <h3>Ranking de vendedores por loja:</h3>
    {ranking_vendedores(melhores_vendedores_por_loja)}
    <h3>Qualquer duvida sobre o ranking, favor entrar em contato com a equipe de vendas.</h3>
    <h5>Att.</h5>
    <h5>Equipe de Vendas</h5>
    </body></html>
    """

    mensagem = mensagem.encode("utf-8")
    email = dotenv_values()["EMAIL_USER"]
    senha = dotenv_values()["EMAIL_PASSWORD"]
    usuario = yagmail.SMTP(user=email, password=senha)
    usuario.send(to=email, subject="Ranking de Vendas", contents=mensagem)


if __name__ == "__main__":
    faturamentos, melhores_vendedores_por_loja = (
        calcular_faturamentos_e_melhores_vendedores()
    )
    enviar_email(faturamentos, melhores_vendedores_por_loja)
