#Cálculo da produtividade
#-------------------------------------
print('=== Cálculo de Produtividade ===')

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de funcionários: '))
    
    media_por_funcionario = total_produzido / funcionarios
    
except (ValueError, TypeError):
    print('Informe um número.')
except ZeroDivisionError:
    print('Funcionário não pode ser zero.')
#Se não dar erro é executado o else
else:
    print(f'Média por funcionario: {media_por_funcionario:.2f}')