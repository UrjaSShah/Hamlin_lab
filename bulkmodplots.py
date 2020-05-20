import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
#DEBYE PLOT
#loading data from excel and converting it to arrays
sheet = pd.read_excel("Bulk Moduli Data final (1).xlsx")
debye_avg=pd.DataFrame(sheet, columns= ['Debye Average'])
debye_avg = np.asarray(debye_avg)
mp_bulkmod=pd.DataFrame(sheet,columns= ['Bulk modulus (K_VRH) (GPA) Calculated from MP'])
mp_bulkmod = np.asarray(mp_bulkmod)
sg=pd.DataFrame(sheet, columns= ['Space group'])
sg=np.asarray(sg)
Tc=pd.DataFrame(sheet,columns=[' Avg Transition Temp'])
Tc = np.asarray(Tc)
#specifying range of space groups for cubic compounds
one=[]
two=[]
three=[]

for i in range(len(sg)):
    if sg[1]<230 and sg[i]>195 :
        one.append(debye_avg[i])
        two.append(mp_bulkmod[i])
    else:
        three.append(debye_avg[i])



#condensing the plot to make the correlation show better
debye_avg_9=[]
debye_avg_i=[]
mpf=[]

for i in range(len(one)):
    if one[i]<900:
        debye_avg_9.append(one[i])
        mpf.append(two[i])
    else:
        debye_avg_i.append(Tc[i])
        

mpf=np.asarray(mpf)
debye_avg_9=np.asarray(debye_avg_9)
#removing all zero/nan values
indice = debye_avg_9.nonzero()
#plotting
m, b = np.polyfit(mpf[indice],debye_avg_9[indice] , 1)
fig,axs = plt.subplots(constrained_layout=True)
axs.yaxis.set_ticks_position('both')
axs.xaxis.set_ticks_position('both')
axs.tick_params(axis='both', direction='in') 
#getting statistics for the plot - r value and p value
slope, intercept, r_value, p_value, std_err = stats.linregress(mpf[indice],debye_avg_9[indice])
print("P value is",p_value)
print("R squared value is", r_value**2)
axs.scatter(mpf[indice],debye_avg_9[indice],color = 'orange')
axs.plot(mpf[indice], m*mpf[indice] + b)
#shaping the plot to a square
axs.pbaspect = [1, 1, 1] 
axs.set_title('Debye from MPDS vs Bulk Mod from MP')
axs.set_ylabel('Debye (K)')
axs.set_xlabel('Bulk Modulus (GPa)')
print("Slope of this plot is",m)
plt.show()

#TC PLOT
Tc = Tc[~np.isnan(Tc)]
other=[]
point=[]
p=[]
m=[]
o=[]
#removing nan values and extremely high tc values that were a few outliers
for i in range(len(Tc)):
    if Tc[i] == 'nan':
        other.append(mp_bulkmod[i])
    else:
        point.append(mp_bulkmod[i])
    if Tc[i]>25:
        o.append(Tc[i])
    else:
        p.append(Tc[i])
        m.append(point[i])
        
p=np.asarray(p)
m=np.asarray(m)
m = np.concatenate(m,axis=0)
#plotting
c, h = np.polyfit(m,p,1)
fig,ax = plt.subplots(constrained_layout=True)

ax.plot(m, m*c + h)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.tick_params(axis='both', direction='in')
slope, intercept, r_value, p_value, std_err = stats.linregress(m,p)
print("P value is",p_value)
print("R squared value is", r_value**2)
ax.scatter(m,p,color = 'orange')
ax.pbaspect = [1, 1, 1]  
#secax = ax.secondary_xaxis('top')
#secax = ax.secondary_yaxis('right')
ax.set_title('Tc from MPDS vs Bulk Mod from MP')
ax.set_ylabel('Tc (K)')
ax.set_xlabel('Bulk Modulus (GPa)')

plt.show()
