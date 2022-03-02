import time
import os

def fibo(n):
    f=1
    fm1=1
    fm2=0
    for i in range(n-1):
        f=fm1+fm2;fm2=fm1;fm1=f
    return f

n=1
log = open("log.txt", "a", encoding="utf-8")
while True:
    n*=10
    debut = time.time()
    fibonacci = str(fibo(n))
    fin = time.time()
    with open("Fibonacci "+str(n)+".txt", "w", encoding="utf-8") as f:
        f.write(fibonacci)
    txt = "Fibonacci de "+str(n)+" effectué en "+str(fin-debut)+" secondes. Nombre de caractères: "+str(len(fibonacci))+".\n"
    log.seek(os.SEEK_END)
    log.write(txt)
    print(txt)
