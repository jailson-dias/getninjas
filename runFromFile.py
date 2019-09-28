import os

from plateau import Plateau
from rover import Rover

path = "./input"
files = []

# Salva todos os arquivos com extenção .txt que tem na pasta input
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(file)

# Executa cada arquivo em sequência
for f in files:
    test_case = open(os.path.join(path, f), 'r')

    # Cria o plateau
    plateuSize = test_case.readline().split("\n")[0].split(" ")
    plateau = Plateau(int(plateuSize[0]), int(plateuSize[1]))

    output = open(os.path.join("./output", f), 'w')

    while True:
        roverDetail = test_case.readline()
        if not roverDetail:
            break
        
        # Cria o Rover
        roverDetail = roverDetail.split("\n")[0].split(" ")
        rover = Rover(int(roverDetail[0]), int(roverDetail[1]), roverDetail[2], plateau)
        try:
            # Executa os camando do rover e salva a posição final no arquivo na pasta de output
            rover.runCommands(test_case.readline().split("\n")[0])
            output.write(str(rover))
        except:
            # Caso a sequência de comandos faça com que o rover saia do plateau,
            # Salva no arquivo de output que o rover saiu do plateau
            output.write("Rover left the Plateau\n")
            
    
    test_case.close()
    output.close()
