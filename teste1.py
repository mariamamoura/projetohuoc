import csv

arquivo = open('nomes.txt', 'r')
texto = arquivo.readlines()
dict = {}

##LE ARQUIVO TXT E SPLITA ELES##

for linha in texto:
    separado = linha.split(';')
    codigo = int(separado[0])
    nome = separado[1]
    #print(codigo)
    #print(nome)

    ##FAZER DICIONARIO DE CADA ATRIBUTO##
    dict[codigo] = nome
#print(dict)
#print(dict.get(155))  ##PEGAR CERTO NOME DO DICT DE ACORDO COM SEU CODIGO##

while True:
    opcao = int(input("""
Digite 1 para ver a lista de pacientes.
Digite 2 para registrar visitas.
Digite 3 para sair"""))

    if opcao == 1:
        for linha in texto:
            separado = linha.split(';')
            codigo = separado[0]  ##NAO É INT PRA NAO DAR ERRO##
            nome = separado[1]
            print(codigo + nome)

    elif opcao == 2:
        numero_solicitado = int(input('Digite o número do paciente'))
        confirmar = int(input('Você visitou {}. Digite 1 para confirmar ou 2 para cancelar'.format(dict[numero_solicitado])))
        if confirmar == 1:
            print('Obrigado pela visita!')

        if confirmar != 1 and 2:
            print('Você precisa digitar 1 ou 2')  #REPETIR INPUT DE CONFIRMAR

        #if numero_solicitado != :   ##DAR MENSAGEM DE ERRO QUANDO O ALUNO SOLICITA UM NUM QUE NAO SEJA DE PACIENTE##
            #print('Paciente não encontrado')

    elif opcao == 3:
        break

    else:
        print('Você precisa digitar 1, 2 ou 3')