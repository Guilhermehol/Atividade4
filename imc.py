import os
import pymysql

valor_imc = 0
valor_situacao = ""


def calc_imc(altura, peso):
    altura /= 100
    return peso / (altura * altura)


def calc_situacao(imc):
    if imc < 17:
        return 'Muito abaixo do peso'
    elif (imc >= 17) & (imc <= 18.49):
        return 'Abaixo do peso'
    elif (imc >= 18.50) & (imc <= 24.99):
        return 'Peso normal'
    elif (imc >= 25.00) & (imc <= 29.99):
        return 'Acima do peso'
    elif (imc >= 30.00) & (imc <= 34.99):
        return 'Obesidade I'
    elif (imc >= 35.000) & (imc <= 39.99):
        return 'Obesidade II (severa)'
    elif imc >= 40:
        return 'Obesidade III (mórbida)'


conexao = pymysql.connect(db='imc', user='root', passwd='guilherme')  # MUDAR SENHA E USUARIO
pont = conexao.cursor()

while True:
    print("Cálculo do imc!!!")
    print("\n\r")
    print("OPÇÕES")
    print("(1) Calcular IMC")
    print("(2) Exibir relatório")
    print("(3) Sair")
    op = input("Informe a opção desejada: ")
    os.system('cls') or None

    if op == '1':
        nome = input("Informe seu nome: ")
        endereco = input("Endereço: ")
        altura = int(input("Altura (cm): "))
        peso = float(input("Peso (Kg): "))
        os.system('cls') or None
        valor_imc = calc_imc(altura, peso)
        valor_situacao = calc_situacao(valor_imc)
        print("RESULTADO: ")
        print("IMC: %.2f -- %s" % (valor_imc, valor_situacao))
        os.system('pause')
        os.system('cls') or None

        sql = "INSERT INTO historico (nome, endereco, altura, peso, imc, situacao) VALUES (%s,%s,%s,%s,%s,%s)"
        pont.execute(sql,
                     (nome, endereco, altura, peso, valor_imc, str(valor_situacao)))
        conexao.commit()
    elif op == '2':
        tmp = ''
        sql = "SELECT nome, altura, peso, imc, situacao FROM historico"
        pont.execute(sql)
        for valor in pont.fetchall():
            tmp += "%s \nAltura: %d \nPeso: %.0f \nIMC: %.2f -- %s \n \n" % \
                  (valor[0], valor[1], valor[2], valor[3], valor[4])
        print(tmp)
        os.system('pause')
        os.system('cls') or None
    elif op == '3':
        exit()
