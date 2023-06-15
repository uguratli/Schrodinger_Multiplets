from sympy import I
from sympy.physics.quantum import TensorProduct
import sympy as sym
import numpy as np
#gamma matrices
sigma1=sym.Matrix([[0,1],[1,0]])
sigma2=sym.Matrix([[0,-I],[I,0]])
sigma3=sym.Matrix([[1,0],[0,-1]])
gamma0=I*sigma3
gamma1=sigma1
gamma2=sigma2
gamma=[gamma0,gamma1,gamma2]
#Gamma matrices
Gamma0=TensorProduct(I*sigma2,sym.eye(sigma1.shape[0]))
Gamma1=TensorProduct(sigma1,sigma1)
Gamma2=TensorProduct(sigma1,sigma2)
Gamma3=TensorProduct(sigma1,sigma3)
Gamma=[Gamma0,Gamma1,Gamma2,Gamma3]
#Projection
Gamma_p=(Gamma0+Gamma3)
Gamma_m=(Gamma0-Gamma3)
P_p=(sym.eye(Gamma0.shape[0])+Gamma0*Gamma3)/2
P_m=(sym.eye(Gamma0.shape[0])-Gamma0*Gamma3)/2
#Gamma_=[Gamma_p,Gamma1,Gamma2,Gamma_m]
#Metrics
Eta_mn=sym.Matrix([[0,-1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
eta_mn=sym.Matrix([[-1,0,0],[0,1,0],[0,0,1]])
#Functions
def GammaStar(Gamma):
    C=Gamma[0]
    for i in range(1,len(Gamma)):
        C=C*Gamma[i]
    return C*(-I)**int(len(Gamma)/2 +1)
Gamma5=GammaStar(Gamma)
def symbol_isupper(x):
    x_string=str(x)
    return x_string.isupper()
def symbol_upper(x):
    x_string=str(x).upper()
    return sym.symbols(x_string)
def symbol_lower(x):
    x_string=str(x).lower()
    return sym.symbols(x_string)
def Bar_4(V):
    V=V.transpose()
    return I*V*(Gamma3*Gamma1)
def Bar_3(V):
    V=V.transpose()
    return I*V*sigma2
def Parser(x):
    if x.shape==(4,1):
        x_out=sym.Matrix.zeros(2,1)
        i=0
        for j in range(len(x)):
            if x[j]!=0:
                x_out[i]=x[j]
                i+=1
    elif x.shape==(1,4):
        x_out=sym.Matrix.zeros(1,2)
        i=0
        for j in range(len(x)):
            if x[j]!=0:
                x_out[i]=x[j]
                i+=1
    return x_out
def Gamma_ij(A,B):
    return (A*B-B*A)/2
#def Gamma_ij(i,j):
    ##2\eta^{\mu \nu}=\gamma^{\mu}\gamma^{\nu}+\gamma^{\nu}\gamma^{\mu}
    ##2\gamma^{\mu \nu}=\gamma^{\mu}\gamma^{\nu}-\gamma^{\nu}\gamma^{\mu}
    #Gamma_ij=Gamma[i]*Gamma[j]-Eta_mn[i,j]*sym.eye(4)
    #return Gamma_ij
#def gamma_ij(i,j):
    ##2\eta^{\mu \nu}=\gamma^{\mu}\gamma^{\nu}+\gamma^{\nu}\gamma^{\mu}
    ##2\gamma^{\mu \nu}=\gamma^{\mu}\gamma^{\nu}-\gamma^{\nu}\gamma^{\mu}
    #gamma_ij=gamma[i]*gamma[j]-eta_mn[i,j]*sym.eye(2)
    #return gamma_ij