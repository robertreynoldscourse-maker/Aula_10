#Cálculo da produtividade
#-------------------------------------
print('=== Cálculo de Produtividade ===')

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de funcionários: '))
    media_por_funcionario = total_produzido / funcionarios
    print(f'Média por funcionario: {media_por_funcionario:.2f}')
except ValueError:
    print('Informe um número.')
except ZeroDivisionError:
    print('Funcionário não pode ser zero.')
