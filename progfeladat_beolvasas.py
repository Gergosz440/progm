#FONTOS: töltsd le ami kell!
#írd be konzolba egyenként: pip install pandas
#                           pip install scipy
#                           pip install numpy
#                           pip install matplotlib
#ami ki van kommentelve (ezt beleértve) törölheted ha már nincs rá szükség, ezek tesztelések meg jegyzetek neked
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
excel_file = pd.ExcelFile('progfeladat_adatok_excel.xlsx')
#print("A következő munkalapok szerepelnek az Excel fileban: ", excel_file.sheet_names)

df = excel_file.parse('Információk')
df = excel_file.parse(excel_file.sheet_names[0])

#minden oszlop kivéve a kategóriák el rakva egy tömbbe
cols_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
excel = pd.read_excel('progfeladat_adatok_excel.xlsx', usecols=cols_index)

#print(excel.loc[19])

#a 19. sor az összesített adatokat tartalmazza a táblázatban
#most csak ez a sor van ábrázolva
oszzesadatok = excel.loc[19]

#ind = excel.index[4]
#print(ind)
#print(oszzesadatok[0])

#print(df.loc[4])

#plot diagram
xpoints = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
ypoints = np.array([oszzesadatok[0],oszzesadatok[1],oszzesadatok[2],oszzesadatok[3],oszzesadatok[4],oszzesadatok[5],oszzesadatok[6],oszzesadatok[7],oszzesadatok[8],oszzesadatok[9],oszzesadatok[10],oszzesadatok[11],oszzesadatok[12],oszzesadatok[13],oszzesadatok[14],oszzesadatok[15],oszzesadatok[16],oszzesadatok[17],oszzesadatok[18],oszzesadatok[19],oszzesadatok[20],oszzesadatok[21]])
#marker a jobb láthatóságért
plt.plot(xpoints, ypoints, marker = 'o')
plt.show()

#lineáris regresszió
#mint ez előző ez is csak az "összes" adatokat használja
from scipy import stats
x = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
y = [oszzesadatok[0],oszzesadatok[1],oszzesadatok[2],oszzesadatok[3],oszzesadatok[4],oszzesadatok[5],oszzesadatok[6],oszzesadatok[7],oszzesadatok[8],oszzesadatok[9],oszzesadatok[10],oszzesadatok[11],oszzesadatok[12],oszzesadatok[13],oszzesadatok[14],oszzesadatok[15],oszzesadatok[16],oszzesadatok[17],oszzesadatok[18],oszzesadatok[19],oszzesadatok[20],oszzesadatok[21]]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

#bro ezt rák volt mind megérteni és használni