import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 

#create figure
plt.figure()

ochl = pd.DataFrame({'o': [50, 45, 41, 48, 57, 63, 62, 68],
                       'c': [43, 40, 47, 58, 64, 60, 69, 64],
                       'h': [55, 46, 50, 62, 65, 70, 70, 71],
                       'l': [39, 38, 40, 43, 52, 50, 60, 60]},
                       index=range(0,8))

#define up and down ochl
up = ochl[ochl['c']>=ochl['o']]
down = ochl[ochl['c']<ochl['o']]

candle_width = .4
stick_width = .05

# o plot é dividido nas tres partes do pavio das candles, também divide os 
# de subida com descida para diferenciar as cores

plt.bar(up.index,up['c']-up['o'],candle_width,bottom=up['o'],color='green')
plt.bar(down.index,down['c']-down['o'],candle_width,bottom=down['o'],color='red')

plt.bar(up.index,up['h']-up['c'],stick_width,bottom=up['c'],color='green')
plt.bar(down.index,down['h']-down['o'],stick_width,bottom=down['o'],color='red')

plt.bar(up.index,up['l']-up['o'],stick_width,bottom=up['o'],color='green')
plt.bar(down.index,down['l']-down['c'],stick_width,bottom=down['c'],color='red')

# cria a normal com centro no último fechamento, usei um sigma arbitrario
normal_center = list(ochl['o'])[-1] # ultimo fechamento
sigma = normal_center/5 # modificar com dado correto

normal_x = np.arange(normal_center - 2*sigma, normal_center + 2*sigma)
normal_y = norm.pdf(normal_x, normal_center, sigma) * (-1) # cria a normal invertida 

# tem que ajustar a normal para o eixo do tempo, fiz aqui arbitrariamente
normal_y = (normal_y - min(normal_y))*100 + 7

plt.plot(normal_y, normal_x, color="blue") 

#display candlestick chart
plt.show()
