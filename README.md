# Rover

Lenda o enunciado da questão eu percebi que tem dois objetos, mesmo o plateau tendo apenas as coordenadas x e y que representa o tamanho dele, eu também considerei ele como um objeto.

No caso do rover, ele tem alguns atributos, como o próprio plateau, que ele só pode se mover naquela área, a posição inicial e a direção que a câmera dele está apontando. Além desses atributos ele também tem os métodos de mover e rotacionar, sendo que rotacionar é para direita e esquerda, enquanto que mover é apenas para frente. Com isso eu criei a classe do rover com esses atributos e métodos, e adicionei um outro método para facilitar na execução dos comandos.

## Objetos

#### Plateau

1. **Atributos**
   1.1. **size**: com as coordenadas x e y do limite do plateau

#### Rover

1. **Atributos**
   1.1. **position**: posição atual do rove no plateau
   1.2. **direction**: direção para onde a câmera está apontando
2. **Métodos**
   2.1. **rotate**: rotaciona o rover para direita ou esquerda em 90º
   2.2. **move**: move o rover uma casa para frente
   2.3. **runCommands**: executa a sequência de comandos fornecida

## Testes

Foi feito um arquivo de teste para testar o rover, nesse arquivo foram testados as seguintes coisas:

1. **test_rover_create**: se o rover está sendo criado corretamente.
2. **test_rover_rotate**: se a rotação do rover está sendo feita corretamente, foi testado com a fotação para a direita e para esquerda.
3. **test_move**: se o movimento do rover está sendo realizado corretamente, e no caso de o rover sair do plateau lançar uma exceção.
4. **test_path_12_N_LMLMLMLMM** e **test_path_33_E_MMRMMRMRRM**: testar se depois da execução de todos os comandos o rover está no local correto

## Input de arquivo

Foi criado o arquivo `runFromFile.py` para executar casos de teste a partir de um arquivo, no caso aqui ele ler todos os arquivos `.txt` da pasta input e executa o algoritmo do rover sobre eles, salvando a saída na pasta `output` em arquivos com o mesmo nome que estava na pasta `input`.

## Execução

### No computador

Para facilitar a execução eu criei dois arquivos shell script, em `menu.sh` é executado o arquivo de teste e o arquivo `runFromFile.py` para executar o algoritmo com os arquivos da pasta `input` como entrada.

No arquivo `selectFromRun.sh`, é executado um script com um menu, para escolher qual dos dois arquivos vai querer executar, o arquivo de testes ou o arquivo para executar o algoritmo com a entrada da pasta input.

Para executar esses dois arquivos shell script, é necessário está em um computador com Linux ou Mac OS e executar os seguintes comandos:

```shell
cd /path/to/project
bash ./main.sh
```

ou

```shell
cd /path/to/project
bash ./runFromFile.sh
```

### No docker

Para executar no docker foi utilizado apenas o script `main.sh`, que executa os dois arquivos python juntos.

Caso queira executar com o docker compose, ele vai executar o script e encerrar o container. E para executar precisa dos seguintes comandos:

```shell
cd /path/to/project
docker-compose build
docker-compose up
```

Já para executar apenas com o docker é necessário executar os seguintes comandos:

```shell
cd /path/to/project
docker build -t getninjas .
docker run --name getninjas-container getninjas
```

Depois de executar esses comandos, vai aparecer no terminal o resultado dos testes e os arquivos de saída já vão está na pasta output. E no caso de executar apenas com docker, para ter acesso aos arquivos de saída tem que acessar o container e ver os arquivos que estão na pasta `/app/output`.
