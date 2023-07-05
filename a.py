#Inicio da função cachorro_peso()
def cachorro_peso():
    print('             Menu 1 de 3 - Peso do cachorro                ')
    print('-----------------------------------------------------------')
    print('|                 PESO        |  VALOR                    |')
    print('-----------------------------------------------------------')
    print('|               ATÉ 3KG       |  40,00                    |')
    print('-----------------------------------------------------------')
    print('|             DE 3KG ATÉ 10KG |  50,00                    |')
    print('-----------------------------------------------------------')
    print('|            DE 10KG ATÉ 30KG |  60,00                    |')
    print('-----------------------------------------------------------')
    print('|            DE 30KG ATÉ 50KG |  70,00                    |')
    print('-----------------------------------------------------------')
    while True:
        try:
            peso= int(input('Digite o peso do cachorro (kg): '))
            if (peso < 3):
               return 40
            elif (peso >=3) and (peso <10):
                return 50
            elif (peso >=10) and (peso<30):
                return 60
            elif (peso >= 30) and (peso  <50):
                return 70
            else:
                print('Não aceitamos cachorros tão grandes.')
                continue #retorna para a pergunta
        except ValueError: #caso o usúario digite um valor não numerico:
            print('Você digitou um valor não numérico.')   
#Fim da função cachorro_peso()

#Inicio da função cachorro_pelo()
def cachorro_pelo():
    print('--------------Menu 2 de 3 - Pelo do cachorro-------------')
    while True:
        pelo=(input('Digite o tamanho do pelo do cachorro \n' +
                    'c - pelo curto \n' +
                    'm - pelo médio \n' +
                    'l - pelo longo \n'+
                    ' >>'))
                    
        pelo= pelo.lower()
        pelo= pelo.strip()
        if pelo =='c':
            return 1.0
        elif pelo =='m':
            return 1.5
        elif pelo=='l':
            return 2.0
        else:
            print('Pare de digitar tamanhos diferentes de c/m/l.')
            continue #retorna para a pergunta

#Fim da função cachorro_pelo()

#Inicio da função cachorro_extra()
def cachorro_extra():
    print('---------------Menu 3 de 3 - Extra----------------')
    acumulador= 0
    while True:
        extra= (input('Deseja adicionar mais algum serviço? \n' +
                      '1 - Cortar unhas \n' +
                      '2 - Escovar os dentes \n' +
                      '3 - Limpar as orelhas \n' +
                      '0 - Não quero mais nada \n ' +
                      '>>'))
        if extra =='0':
            return acumulador
        elif extra =='1':
            acumulador= acumulador + 10
            continue #volta ao inicio do while true
        elif extra =='2':
            acumulador= acumulador + 12
            continue #volta ao inicio do while true
        elif extra =='3':
            acumulador= acumulador + 15
            continue #volta ao inicio do while true
        else:
            print('Pare de digitar opções que não seja 0/1/2/3.')
#Fim da função cachorro_extra()

#Mensagem de boas vindas e ínicio da main
print('-----------------------------------------------------------')
print('    Olá, seja bem vindo(a) ao petshop da Maria Eduarda!    ')
print('-----------------------------------------------------------')
peso= cachorro_peso()
print(peso)
pelo= cachorro_pelo()
print(pelo)
extra= cachorro_extra()
print(extra)
total= (peso * pelo) + extra
print('O total ficou: R$ {:.2f} (Peso: {:.2f} * Pelo:  {:.2f} + Extra:  {:.2f})' .format (total, peso, pelo, extra)) #total a pagar






