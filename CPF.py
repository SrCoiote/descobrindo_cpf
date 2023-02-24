"""
Calculo do primeiro e do segundo dígito do CPF.
A pessoa informa os 9 primeiros dígitos do CPF,
E então multiplicamos cada um dos valores por uma
contagem regressiva começando de 10,
logo após isso nós somamos os resultados
E Multiplicamos o resultado anterior por 10,
Obtemos o resto da divisão da conta anterior por 11 utilizando o módulo.
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""
import os

print('DESCUBRA OS 2 ÚLTIMOS DÍGITOS DO CPF')

while True:
    # Começamos pelo primeiro digito do CPF
    cpf_enviado = input('Digite os 9 digitos do CPF: ') # Coletamos a informação do usuário
    contador_regressivo_1 = 10 # multiplicaremos os valores por uma contagem regressiva, por isso dessa variavel.
    

    if cpf_enviado.isnumeric():
        os.system('cls')
        ...
        if len(cpf_enviado) > 9:
            print('Digite apenas 9 digitos.')
            continue
        elif len(cpf_enviado) < 9:
            print('Digite 9 digitos.')
            continue
    else:
        print('Digite apenas números.')
        os.system('cls')
        continue
        # Nessa etapa fizemos alguns bloqueios para que o programa não "quebre"

    resultado = 0
    for digito in cpf_enviado:
        contagem = int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
        resultado += contagem
        '''
        Aqui é feita multiplicação com o contador
        regressivo, utiliando o Laço de repetição.
        '''

    digito_1 = (resultado * 10) % 11 # multiplicamos e obtemos o resto da divisão com o módulo 
    digito_1 = digito_1 if digito_1 < 9 else 0 # temos uma condição necessária para que se
    # O resultado for maior que 9, ele devolva 0, caso contrário mantenha-se o numero obtido
    cpf_enviado += str(digito_1) # tranformamos em string porque não é possivel fazer "str + int"

    # Agora vamos descobrir o 2 digito do CPF. É o mesmo procedimento, a única coisa é que vamos
    # adicionar o ultimo digito descoberto, por isso o valor do contador regressivo agora é 11.

    contador_regressivo_2 = 11 

    resultado_digito_2 = 0
    for digito_2 in cpf_enviado:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    # repete-se o procedimento do primeiro digito.

    cpf_final = cpf_enviado + str(digito_2)
    print(f'Seu CPF é: {cpf_final}')
    # Pronto, dessa forma descobrimos os ultimos digitos! Vale ressaltar que é possivel
    # descobrir através desse mesmo sistema se o CPF indicado é válido ou não.