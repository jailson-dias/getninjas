#!/bin/sh
echo "Executando o algoritmo com os arquivos da pasta input"
python runFromFile.py
echo "A saída do algoritmo está na pasta output"
echo "O nome do arquivo de saída e o mesmo do arquivo que está na pasta input"
echo ""
echo ""
echo "Executando o arquivo de testes"
python tests.py -v
echo ""
echo ""

