#!/usr/bin/env python3
import ccxt
from ccxt.base.exchange import Exchange
import matplotlib.pyplot as pl
import numpy as np
contatore = 0
exchange = ccxt.binance({
    "enableRateLimit" : True,
})
def crypto_price(crypto,quanto):
    return quanto/exchange.fetchTicker(crypto+"/USDT")["last"]

def perc(n, m):
    n1=exchange.fetchTicker(n)['open']
    n2=exchange.fetchTicker(n)['close']
    m1=exchange.fetchTicker(m)['open']
    m2=exchange.fetchTicker(m)['close']
    m=((m2-m1)/m1)*100
    n=((n2-n1)/n1)*100
    mx=np.zeros(100)
    my=np.zeros(100)
    nx=np.zeros(100)
    ny=np.zeros(100)
    for i in range(0, 100):
        nx[i]=(i-50)*(n/100)
        ny[i]=i
    for l in range(0, 100):
        mx[l]=(l-50)*(m/100)
        my[l]=l
    return ny, nx, mx, my, m, n

while contatore == 0:
    r1=str(input("\n Inserire la/le crypto:"))
    if not r1:
        contatore = 0
    else:
        contatore = 1

sol=int(input('Quanti soldi hai a disposizione: '))
if sol != 0:
    valut=str(input('In che valuta: '))
    valut=valut.upper()

nc=0
for i in r1:
    if i == " ":
        nc=1
    else:
        nc=nc

if nc==0:
    r1= r1.upper()
    rf1=(r1+"/USDT")
    v1=exchange.fetchTicker(rf1)['open']
    v2=exchange.fetchTicker(rf1)['close']
    va=float(exchange.fetchTicker(rf1)['last'])
    vs=str((sol/va))
    va=str(va)
    perce=((v2-v1)/v1)*100
    if perce < 0:
        print('\n'+r1+' è diminuito del '+ str(perce+(-1))+'% \n')
    else:
        print('\n'+r1+' è aumentato del '+ str(perce)+'% \n')
    if sol!=0:
        print('Ne puoi comprare '+vs)
    pl.title('Il valore attuale di '+ r1 +' è di '+ str(va) + 'USDT')
    pl.plot([0, 23],[v1, v2])
    pl.show()

if nc==1:
    r1,r2= r1.split(" ")
    r1= r1.upper()
    rf1=(r1+"/USDT")
    r2=r2.upper()
    rf2=(r2+"/USDT")
    po1=float(exchange.fetchTicker(rf1)['last'])
    po2=float(exchange.fetchTicker(rf2)['last'])
    nnx, nny, nmx, nmy, n, m= perc(rf1, rf2)
if sol != 0:
    sol=sol*exchange.fetchTicker(valut+"/USDT")['last']
    so1=(sol/po1)
    so1=str(so1)
    so2=(sol/po2)
    so2=str(so2)
    print('\n Ne puoi prendere al massimo: ' + so1 + " " +r1)
    print('Ne puoi prendere al massimo: '+so2 + " " +r2+"\n")
if n < 0:
        print('il valore di '+r1+' è diminuito del: '+ str(n*(-1)) +'%. Ora è a '+str(po1))   
else:
        print('il valore di '+r1+' è aumentato del: '+ str(n) +'%. Ora è a '+str(po1))
if m < 0:
        print('il valore di '+r2+' è diminuito del: '+ str(m*(-1)) +'%. Ora è a '+str(po2))   
else:
        print('il valore di '+r2+' è aumentato del: '+ str(m) +'% . Ora è a '+str(po2))

pl.title('Differenza percentuale tra: '+ r1+' e '+r2)
pl.xlabel("tempo")
pl.ylabel("%")
pl.plot(nnx, nny, label=r1)
pl.plot(nmy, nmx, label=r2)
pl.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
pl.show()
