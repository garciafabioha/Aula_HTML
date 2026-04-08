"""
print('ola')

velocidade_internet = 400

print(velocidade_internet)

print(type(velocidade_internet))


salario_mensal = float(input('Qual é seu salário mensal: '))
horas_trabalhadas = float(input('Qual a quantidade de horas trabalhada mensalmente: '))

resultado = salario_mensal / horas_trabalhadas

print(f"Valor por hora de trabalho: R$ {resultado:.2f}")

trabalho_terminado = input('Terminou o trabalho ? Verdadeiro ou Falso: False ou True: ')

if trabalho_terminado == True: 
    print('Bora!')
else: 
    print('Vou Trabalhar até mais tarde!')

    estou_livre = False
if estou_livre == True:
    print('ok, bora mover as caixas!')  
else:
    print('Pede ajuda pro meu irmão')

atrasos = int(input('Quantas Faltas você tem: '))

if atrasos >= 3:
    print('Você está suspenso!')
elif atrasos == 2:
    print('Mais uma falta e estará suspenso!')
elif atrasos == 1:    
    print('Mais duas faltas e estará suspenso!')
else:    print('Você está em dia com as faltas.') 


primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))      

if primeiro_valor > segundo_valor:
    print(f'O maior valor é o Primeiro Vsalor: {primeiro_valor}')         
elif segundo_valor > primeiro_valor:
    print(f'O maior valor é o Segundo Valor: {segundo_valor}')
"""    