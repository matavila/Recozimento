# Recozimento

Código desenvolvido com o intuito de transformar uma atividade criada a partir de um arquivo excel, 
em um único arquivo, de forma mais tranquila e intuitiva.

Passo 1: O primeiro passo para a utilização desse código é definir uma matriz tempo e dureza. Uma vez que a partir destas é que vai ser possível a determinação de parâmetros como variação de dureza, dureza máxima e até o recozimento.

Passo 2: A partir da deternminação da recristalização da amostra, torna-se possível a adequação dos dados pelo método de linearização da seguinte formu-la:

                                    𝑉v = 1 − 𝑒 ^−𝑘(𝑡^𝑛)
Vv: fração transformada 
t: tempo de reação (t) 

Esta equação é comumente utilizada em sua forma linearizada, permitindo o cálculo de seus coeficientes, k e n, para um procedimento experimental.

                                ln [ln (1/(1-Vv)) = ln 𝑘 + 𝑛 ln(𝑡)

Passo 3: A partir então da determinação dos coeficientes, temos então a possibilidade de determinar a fração recristalizada da amostra. E também a possibilidade do próprio usuário fazer uma pre-determinação da fração a partir do tempo de recozimento desejádo.


