from datetime import date

saldo = 0
deposito = 0
HDdepositos = {}
HDsaques = {}
limite_saques_diarios = 3
saques_diarios = {}

while True:
    print('''
    Início 
    ''')
    menu = input('''Selecione a operação
[D] DEPÓSITO
[S] SAQUE
[E] EXTRATO
[Q] SAIR 
|''')

    if menu.lower() == 'q':
        print('Encerrando programa ...')
        break

    elif menu == 'd' or menu == 'D':
        print('Você selecionou a opção DEPÓSITO')
        resposta = 'n'
        while resposta.lower() == 'n':
            deposito = float(input('Qual valor gostaria de depositar R$ '))
            if deposito >= 1:
                resposta = input('O valor que deseja depositar é R${:.2f}? (S) para sim, (N) para não: '.format(deposito))
                if resposta.lower() == 's':
                    saldo = saldo + deposito
                    print('Depósito realizado com sucesso.')
                    HDdepositos[len(HDdepositos) + 1] = {'Valor Deposítado R$': deposito, 'saldo': saldo}
                elif resposta.lower() == 'n':
                    print('Operação de Depósito cancelada.')
                else:
                    print('Opção inválida. Por favor, digite S ou N.')
            else:
                print('VALOR DIGITADO DEVE SER MAIOR QUE R$ 01.00')

    elif menu == 's' or menu == 'S':
        print('Você selecionou a opção SAQUE')
        print('Valor de saque disponível somente até R$ 500')
        print('Seu saldo é de R$', saldo)
        saque = float(input('Qual valor gostaria de sacar R$ '))
        hoje = date.today()
        saques_realizados = saques_diarios.get(hoje, 0)

        if saques_realizados < limite_saques_diarios:
            if saque <= saldo and saque >= 1 and saque <= 500:
                saldo = saldo - saque
                print('Saque de R${:.2f} realizado com sucesso.'.format(saque))
                HDsaques[len(HDsaques) + 1] = {'Valor do saque R$': -saque, 'saldo': saldo}
                saques_diarios[hoje] = saques_realizados + 1
            elif saque > saldo:
                print('Saldo insuficiente para realizar o saque.')
            else:
                print('VALOR DIGITADO DEVE SER ATÉ R$ 500.00 E 3 SAQUES DIÁRIOS')
        else:
            print('Limite de saques diários atingido.')

    elif menu == 'e' or menu == 'E':
        print('Você selecionou a opção EXTRATO')
        print(HDdepositos)
        print(HDsaques)
        print('Seu saldo é de R${:.2f}'.format(saldo))
    else:
        print('Opção inválida. Por favor, selecione uma opção válida.')
