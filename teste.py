arquivo = open('nomes.txt', 'r')
texto = arquivo.readlines()

leitos = {}

for linha in texto:
    separado = linha.split(";")
    numpaciente = separado[0]
    nomes = separado[1]
    visitas = separado[2]
    leitos[numpaciente] = nomes + visitas

while True:
    opcao = int(input("""
    Digite 1 para ver a lista de pacientes.
    Digite 2 para registrar visitas.
    Digite 3 para sair:"""))

    if opcao == 1:
        for linha in texto:
            separado = linha.split(";")
            numpaciente = separado[0]
            nomes = separado[1]
            visitas = separado[2]
            print(numpaciente + nomes + visitas)
        visitas = int(visitas)
        numpaciente = int(numpaciente)
        visitas = str(visitas)

    elif opcao == 2:
        numero_solicitado = input('Digite o número do paciente:')
        confirmar = int(input('Voce visitou{}. Digite 1 para confirmar ou 2 para cancelar:'.format(leitos[numero_solicitado])))
        if confirmar == 1:
            print('Obrigado pela visita!')

    elif opcao == 3:
        break
        
    else:
        print('Você precisa digitar 1, 2 ou 3')
