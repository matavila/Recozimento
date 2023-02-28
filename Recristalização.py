import numpy
import scipy.stats
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)
import math

#Primeiro Passo: Determinar a variação da dureza vickers e estabelecer o máximo de dureza

Time = [0,300,480,600,780,900,1200,1800]
Dureza = [250,225,181,172,142,133,129,128] 

def Varicao():
    Menor = min(Dureza)
    Maior = max(Dureza)

    Delta = Maior - Menor

    return Delta,Maior

Delta ,Maior= Varicao()
print("=========================Primeiro Passo:========================================")
print(f"Varição de dureza: {Delta}")
print(f"Dureza máxima: {Maior} HV")
print()

# Segundo Passo: Determinar a concentração de grãos recristalinizados

print("=========================Segundo Passo:========================================")
print(">> (2.0) Determinado a porcentagem de recristalização:")
Concentracao = []

def Determinacao():
    for Dados in Dureza:
        Grau = (Maior-Dados) / Delta
        Concentracao.append(Grau)
        print(f"{(Grau*100):0.2f}%")
    return Concentracao

Concentracao = Determinacao()
Eixo_Y= []
Eixo_X = []

# Terceiro Passo: Determinar os valores do eixo x(tempo) e y(grão) para depois fazer achar a eq. linear da reta

def CalculoY_Grafico():
    for Dado in Concentracao:
        Denominador = 1-Dado
        if Denominador !=0 and Denominador != 1:
            Primeiro = numpy.log((1/Denominador))
            Segundo = numpy.log(Primeiro)   
            Eixo_Y.append(Segundo)
    return Eixo_Y
        
def CalculoX_Grafico():
    for Tempo in Time:
        if Tempo != 0:
            Final = numpy.log(Tempo)
            Eixo_X.append(Final)
    return Eixo_X

Eixo_Y = CalculoY_Grafico()
Eixo_X= CalculoX_Grafico()
Eixo_X.pop()

# Quarto Passo: Vamos importar a metodologia matematica que vai nos ajudar a fazer a regressão linear dos dados. E achar o valor das constantes

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(Eixo_X, Eixo_Y)
def Constante_K():
    b= intercept
    constante = math.e ** b
    return constante

k = Constante_K()
n = slope
print()

print("=========================Dados da Equação:========================================")
# Imprimir a equação de tendência
print("Equação de tendência: y = {:.2f}x  {:.2f}".format(slope, intercept))
print(f'O valor da constante n = {n:.2f}')
print(f'O valor da constante K = {k}')
print()

# Quinto Passo: Agora iremos calcular a fração Recristalizada
print("=========================Fração Recristalizada:========================================")

def Fracao(k,n):
    for Tempo in Time:
        Dado = (1-(math.e ** (-k*(Tempo ** n))))
        print(Dado)
Fracao(k,n)
print()

# Sexto Passo: Agora iremos calcular a fração Recristalizada a partir do input de tempo do usuário:
Valor_Desejado = int(input("Digite o tempo recozimento(s): "))
print("=============Fração Recristalizada==============")

def Calculo_Desejado(tempo,k,n):
    Teorico = (1-(math.e ** (-k*(tempo ** n))))
    return Teorico
Calculado = Calculo_Desejado(Valor_Desejado,k,n)
print(Calculado)
print("================================================")