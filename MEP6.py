# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 08:31:52 2024

@author: Zaheer
"""

import matplotlib.pyplot as plt
import numpy as np
import windz.Weibull as w1

# import windz.SEMEP as semep
import xlsxwriter 
from windz.MEP import mep,em, epm, mlm, mmlm, mom 
import windz.SE as se
import windz.SEMEP as semep
workbook   = xlsxwriter.Workbook("C:\P\wind_out.xlsx")
wsheet = workbook.add_worksheet()
"================ Data===================================="
import xlrd 

"************************Data Reading*********************************"
file_location="C:/P/Polyfit.xls"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
heet1=workbook.sheet_by_index(1)
x=[]
y=[]
p=[]
  
    
"************************Data Reading*********************************"
a=np.zeros(N+1)
for row in range(sheet.nrows):
    if(sheet.cell_value(row,0)!=""):
         x.append(sheet.cell_value(row,0))
         y.append(sheet.cell_value(row,1))
v=np.array(x)
F=np.array(y/sum(y)

def output(n,k,c,MSE,MABE,MAPE,chi,R2):
	wsheet.write(1,n,k)
	wsheet.write(2,n,c)
	wsheet.write(3,n,MSE)
	wsheet.write(4,n,MABE)
	wsheet.write(5,n,MAPE)
	wsheet.write(6,n,chi)
	wsheet.write(7,n,R2)
	#wsheet.write(8,n,A(k,c,2))
	#wsheet.write(9,n,AIC(k,c))
	#wsheet.write(10,n,A(k,c,1))

	return
output(0,'k','c','MSE','MABE','MAPE','chi','R')
"=========== Maximum Entropy Principal============"
N=int(input("Enter number of moments "))
x,y,ymep=mep(N)
y=np.array(y)*max(F)/max(y)
plt.bar(v,F,color="green",edgecolor='blue', width=0.55)
plt.plot(x,y,label='MEP')
plt.xlabel("v (m/s)")
plt.ylabel("Probability")
MSE,MABE,MAPE,chi,R2,F1=semep.SE(0,0,ymep,F)
output(1,1,1,MSE,MABE,MAPE,chi,R2)
"=========== Empirical Method============"
k,c=(em(v,F))
v1=np.linspace(min(v),max(v))
y1=w1.W(k,c,v1)
y1=y1*max(F)/max(y1)
plt.plot(v1,y1,label='EM')
MSE,MABE,MAPE,chi,R2=se.SE(k,c,v,F)
output(2,k,c,MSE,MABE,MAPE,chi,R2)
"=========== Method of Moment============"
k,c=(mom(v,F))
y2=w1.W(k,c,v1)
y2=y2*max(F)/max(y2)
plt.plot(v1,y2,label='MoM')
MSE,MABE,MAPE,chi,R2=se.SE(k,c,v,F)
output(3,k,c,MSE,MABE,MAPE,chi,R2)

"==========='energy pattern factor method'========================"
k,c=(epm(v,F))
y3=w1.W(k,c,v1)
y3=y3*max(F)/max(y3)
plt.plot(v1,y3,label='EPFM')
MSE,MABE,MAPE,chi,R2=se.SE(k,c,v,F)
output(4,k,c,MSE,MABE,MAPE,chi,R2)

"=========== Maximum Likelihood Method========================"
k,c,temp=(mlm(v,F))
y4=w1.W(k,c,v1)
y4=y4*max(F)/max(y4)
plt.plot(v1,y4,label='MoM')
plt.legend()

MSE,MABE,MAPE,chi,R2=se.SE(k,c,v,F)
output(5,k,c,MSE,MABE,MAPE,chi,R2)
 
"=========== Modified Maximum Likelihood Method========================"
k,c,temp=(mmlm(v,F))
y5=w1.W(k,c,v1)
y5=y5*max(F)/max(y5)
plt.plot(v1,y5,label='MoM')
plt.legend()
MSE,MABE,MAPE,chi,R2=se.SE(k,c,v,F)
output(6,k,c,MSE,MABE,MAPE,chi,R2)
workbook.close()