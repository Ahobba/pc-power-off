from os import system #Biblioteca nativo do python para usar comandos de cmd no script.
from time import sleep


while True:

    system('cls')
    
    print('''[ 1 ] Agendar desligamento
[ 2 ] Cancelar desligamento agendado''')

    while True:
        
        #Try para impedir caracteres diferentes de "int" na escolha das opções.
        try:
            menu = int(input('Escolha: '))
            break
        except:
            print('Opção inválida!')
            sleep(2)
            system('cls')
        
    if menu == 1:

        while True:

            print('\n===TEMPORIZADOR===')
            
            #Definir hora, minuto e segundo do tempo. Além de impedir
            #que o usuário defina algum valor diferente de "int".
            try:
                hora = int(input('Hora(s): '))
                minuto = int(input('Minuto(s): '))
                segundo = int(input('Segundo(s): '))
                break
            except:
                print('Apenas números são permitidos!')
                sleep(2)
                system('cls')

        #Sistema para evitar que possa existir minutos ou segundos acima de 60.
        #Embora possa ser possível definir valores maiores nos minutos e segundos acima.
                
        while True:
            if minuto >= 60:
                hora += 1
                minuto -= 60
            elif segundo >= 60:
                minuto += 1
                segundo -= 60
            elif minuto < 60 or segundo < 60:
                break

        #mostra o tempo em que o pc vai desligar nesse formato. Exemplo: 1h 20m 30s.
        print(f'{hora}h {minuto}min {segundo}s')
        sleep(2)

        #tranformação de tudo para segundos, já que o cmd só aceita segundos.
        hora = hora * 60 * 60 #Tranformação de horas para segundos.
        minuto = minuto * 60  #Tranformação de minutos para segundos.

        segundos = segundo + minuto + hora

        #System: função da biblioteca "os"
        system(f'shutdown -s -t {segundos}') #shutdown -s -t xxxx <-- formato para desligar o pc via cmd.
        
    elif menu == 2:
        #System: função da biblioteca "os".
        system('shutdown -a') #shutdown -a <-- formato para cancelar o desligamento agendado pelo cmd.
        print('Cancelamento feito!')
        sleep(2)

    elif menu > 2 or menu < 1:
        print('Opção inválida!')
        sleep(2)
