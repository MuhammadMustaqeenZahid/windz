def mmlm(v,F):
    print(v)
    import numpy as np
    x1=[]
    for j in range(0,len(F)):
        if v[j]==0:
            x1.append(0.0001)
        else:
            x1.append(v[j])
    v=np.array(x1)
    x2=[]
    for j in range(0,len(F)):
        if F[j]==0:
            x2.append(0.0001)
        else:
            x2.append(F[j])
    F=np.array(x2)
    x=np.linspace(2,10,10000)
    temp=[]
    f=F/np.sum(F)
    
    for i in range(0,len(x)):
        k=x[i]
        temp.append(abs(k-(np.sum(np.power(v,k)*np.log(v)*f)/np.sum(np.power(v,k)*f)-np.sum(np.log(v)*f))**-1))
    n=temp.index(min(temp))
    k=x[n]
    c=(np.dot(F,np.power(v,k))**(1/k))
    return (k,c,temp)

def mlm(v,F):
    import numpy as np
    x1=[]
    if v[0]==0:
            x1.append(0.0001)
            for j in range(1,len(v)):
                x1.append(v[j])
            v=np.array(x1)
    x=np.linspace(1.5,14,2000)
    temp=[]
    for i in range(0,len(x)):
        k=x[i]
    
        temp.append(abs(k-(np.sum(F*np.power(v,k)*np.log(v))/np.sum(F*np.power(v,k))-np.sum(F*np.log(v)))**-1))
    n=temp.index(min(temp))
    k=x[n]
    c=(np.sum(F*np.power(v,k)))**(1/k)
    return (k,c,temp)
def mom(v,F):
	import numpy as np
	import math
	x=np.linspace(1,10,1000)
	temp=[]
	for i in range(0,len(x)):
    		k=x[i]
    		temp.append(abs(((np.sum(F*(v-np.dot(F,v))**2))**0.5/np.dot(v,F))-(math.gamma(1+2/k)-math.gamma(1+1/k)**2)**0.5/math.gamma(1+1/k)))
	n=temp.index(min(temp))
	k=x[n]
	c=np.dot(v,F)/math.gamma(1+1/k)
	return (k,c)
def epm(v,F):
	import numpy as np
	import math
	k=1+3.69/(np.dot(F,np.power(v,3))/np.dot(v,F)**3)**2
	c=np.dot(v,F)/math.gamma(1+1/k)
	return (k,c)

def em(v,F):

	import numpy as np
	import math
	k=((np.sum(F*(v-np.dot(F,v))**2))**0.5/np.sum(F*v))**-1.086
	c=np.dot(v,F)/math.gamma(1+1/k)
	return k,c

def mep(N,x,p):    
    import matplotlib.pyplot as pyplot
    import math
    import matplotlib.pyplot as plt 
    import numpy as np
    from numpy.linalg import inv
    from scipy import integrate
    a=np.zeros(N+1)
    #sum1=15
    for w in range(0,50):
        mew=[]    
        for i in range(0,N+1):
            temp=np.dot(np.array(x)**i,np.array(p))
            mew.append(temp)
        Gn=[]
        "************************Calculation of Gn********************************"   
        def f(x):
                sum=0
                for i in range(0,N+1):
                    sum=sum+a[i]*x**i
                return np.exp(-sum)*x**j
        for j in range(0,N+1):
            val, err =  integrate.quad(f, x[0],x[len(x)-1])
            Gn.append(val)
        v=[]
        for j in range(0,N+1):
            v.append(mew[j]-Gn[j])
        "************************' Calculation of Gnk '********************************"   
        
        def f(x):
            sum=0
            for i in range(0,N+1):
                sum=sum+a[i]*x**i
            return np.exp(-sum)*x**j*x**k
        Gnk=[]
        for j in range(0,N+1):
            row=[]
            for k in range(0,N+1):
                val, err =  integrate.quad(f, x[0],x[len(x)-1])
                row.append(-1*val)
            Gnk.append(row)
        ainv=inv(Gnk)
        delta=np.matmul(ainv,v)
        #print(delta)
        ef=[]
        anew=[]
        for i in range(0,N+1):
            anew.append(a[i]+delta[i])
        sum2=0
        for i in range(0,len(x)):
            sum=0
            for j in range(0,N+1):
                sum=sum+a[j]*x[i]**j
            ef.append(np.exp(-sum))
            sum2=(sum2+(ef[i]-p[i])**2)
            #print(ef[i],p[i])
        '========================='
        a=anew
        fact=np.max(p)/np.max(ef)
        fact1=[]
        for k in range(0,len(x)):
            fact1.append(max(p)*(ef[k])/max(ef))
    dx=(x[len(x)-1]-x[0])/100
    ynew=[]
    xnew=[]
    i=float(0)
    xtemp=x[0]-dx
    x3=np.linspace(x[0],x[len(x)-1],100)
    for i in range(0,100):
        xtemp=x3[i]
        sum=0
        for j in range(0,N+1):
            sum=sum+a[j]*xtemp**j
        ynew.append(np.exp(-sum))
        xnew.append(xtemp)
    ynew1=[]
    ymep=[]
    ynew2=[]
    for i in range(0,100):
        ynew1.append(ynew[i]*np.max(p)/np.max(ynew))
    ynew2=[]
    ymep=[]
    for i in range(0,len(x)):
     	    xtemp=x[i]
     	    sum=0       
     	    for j in range(0,N+1):
     	        sum=sum+a[j]*xtemp**j
     	    ynew2.append(np.exp(-sum))
    for i in range(0,len(x)):
        ymep.append(ynew2[i]*np.max(p)/np.max(ynew2))
    return (xnew,ynew,ymep)

 