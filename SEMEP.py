def SE(k,c,W,F):
    import numpy as np
    temp=[]
    for j in range(0,len(F)):
    	if F[j]==0:
    	   temp.append(0.00001)
    	else:
    	   temp.append(F[j])
    F=temp


    summse,summabe,summape,sumchi,sumWF,sumF,sumW,sumFF,sumWW=0,0,0,0,0,0,0,0,0
    for i in range(0,len(F)):
        summse=summse+(W[i]-F[i])**2
        summabe=summabe+abs(W[i]-F[i])
        summape=summape+abs((W[i]-F[i])/F[i])
        sumchi=sumchi+(W[i]-F[i])**2/F[i]
        sumWF=sumWF+F[i]*W[i]
        sumW=sumW+W[i]
        sumF=sumF+F[i]
        sumFF=sumFF+F[i]*F[i]
        sumWW=sumWW+W[i]*W[i]
    MSE=(summse/len(F))**0.5
    MABE=summabe/len(F)
    MAPE=summape/len(F)
    chi=sumchi
    R2=np.correlate(F,W)
    R2=round(((len(F)*sumWF-sumF*sumW)/((len(F)*sumFF-sumF**2)*(len(F)*sumWW-sumW**2))**0.5),4)  
    return (MSE,MABE,MAPE,chi,R2)