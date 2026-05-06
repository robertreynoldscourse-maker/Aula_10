# saldo = 1000.00
# try:
#     saque = float(input('Digite a quantidade do saque: '))
#     if saque > saldo: 
#         print('Saldo insuficiente!!')
#     else:
#         saldo = 1000.00 - saque
#         print(f'Saque com sucesso, seu novo saldo é {saldo:.2f}')
    
# except Exception as e:
#     print(f'Ops! Erro nos valores de entrada: {e}')
# except KeyboardInterrupt:
#     print('Operação cancelada pelo usuario.')
# finally:
#     print('Programa finalizado. Obrigado por utilizar nossos serviços.')

print('CAIXA ELETRÔNICO')

try:
    saldo = 1000
    saque = float(input('Informe o valor do saque: '))
except ValueError:
    print('Valor inválido')
except KeyboardInterrupt:
    print('Programa encerrado pelo usuario.')
else:
    if saque > saldo:
        print('Saldo insuficiente.')
    elif saque <= 0 or saque < 2:
        print('Saque precisa ser maior ou igual a R$ 2,00')
    else:
        saldo -= saque
        print('Saque realizado com sucesso!!')
        print(f'Su saldo restante é: {saldo}')
finally:
    print('Programa Finalizado. \nObrigado por usar nossos serviços. Volte quando quiser.')
