import numpy as np

N=np.array([10,100,1000])
#Primera funcion con distribucion discreta 
def sample_1 (N):
    a=[-10,-5,3,9]
    b=np.random.choice(a,N, p= [0.1,0.4,0.2,0.3])
    return b

#Secunda funcion con distribucion exponencial
def sample_2(N):
    a=np.random.exponential(0.5,N)
    return a

#Funcion que da m numero de promedios
def get_mean(sampling_fun,N,M):
    promedios=np.zeros(M)
    for i in range(M):
        promedios[i]= np.mean(sampling_fun(N))
    return promedios

M=1000
a=[sample_1,sample_2]
nombres=["sample_1","sample_2"]

#Se crean los archivos txt para cada uno de los txt y para las dos muestras 
for i in range(len(a)):
    for j in range(len(N)):
        prom= get_mean(a[i],N[j],M)
        np.savetxt(nombres[i]+"_"+str(j)+".txt", prom)
