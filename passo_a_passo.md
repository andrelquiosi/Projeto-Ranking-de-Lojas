# Passo a passo do funcionamento do código

### Instalar o poetry e as bibliotecas

    pip install poetry
    poetry init
    poetry add pandas
    poetry add openpyxl
    poetry add yagmail
    poetry add dotenv

### Passo 1: pegar cada base de dados
### Passo 2: para cada base de dados:
    Calcular o faturamento total de cada loja
### Passo 3: Criar ranking com o faturamento total de todas as lojas
### Passo 4: Enviar por email esse ranking

    possibilidades:
        yagmail - direta e simples (gmail)
        smtplib - bem personalizado, mas complexo
        outlook - somente se usar gmail
        pyautogui - automação por RPA

### Adaptar o .VENV

```
EMAIL_USER=@gmail.com
EMAIL_PASSWORD='senha'
```
