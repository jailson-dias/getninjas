#!/bin/sh
command="start"
menu ()
{
while true $command != "start"
do
    clear
    echo "================================================"
    echo "Escolha o comando para executar"
    echo "1) Executar algoritmo com arquivos da pasta input"
    echo "2) Executar arquivo de testes"
    echo "3) Sair"
    echo "================================================"

    echo "Digite o número correspondente a sua opção:"
    read command
    echo "Opção informada ($command)"
    echo "================================================"

case "$command" in


    1)
        echo "Executando o algoritmo com os arquivos da pasta input"
        python runFromFile.py
        echo "A saída do algoritmo está na pasta output"
        echo "O nome do arquivo de saída e o mesmo do arquivo que está na pasta input"
        echo ""
        echo "Para continuar aperte qualquer tecla..."
        read -n 1
;;
    2)
        echo "Executando o arquivo de testes"
        python tests.py -v
        echo ""
        echo "Para continuar aperte qualquer tecla..."
        read -n 1
;;
   3)
        echo "Saindo..."
        sleep 3;
        clear;
        exit;
;;
    *)
        echo "Opção inválida!"
        sleep 2;
esac
done

}

menu