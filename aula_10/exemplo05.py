#Cálculo da produtividade
#-------------------------------------
print('=== Cálculo de Produtividade ===')

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de funcionários: '))
    
    media_por_funcionario = total_produzido / funcionarios

#Exception contem todos os ERROS 
except Exception as e:
    print(f'Ops! Erro nos valores de entrada: {e}')
except KeyboardInterrupt:
    print('Operação cancelada pelo usuario.')
else:
    print(f'Média por funcionario: {media_por_funcionario:.2f}')
# O finally é executado mesmo se dar ou não dar erro.
finally:
    print('Programa encerrado!')