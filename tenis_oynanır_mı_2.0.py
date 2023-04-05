import pandas as pd
import numpy as np
# Kütüphanelerimizi ekledikten sonra dosyamızın bulunduğu dizini yazarak dosyamızı içeri aktarıyoruz

# pd = pandas demek , read_csv = dosya okumamızı sağlıyor
data = pd.read_csv("/Users/hseyi/Desktop/VSCode/Yapay Zeka/Btk-Yapay-Zeka/odev_tenis.csv")
# Verimizi gelip gelmediğini kontrol ediyoruz.
print(data)

# print(data.shape)
# .shape = verimizin kolon ve sütun sayısını gösteriyor

# Proje Multi Regression olduğundan verilerin sayısal formlarına ihtiyaçımız var
# Projemizdeki verilere baktığımızda LabelEncoder Kullanmamız gerektiğini anlıyoruz.
# Hemen Kütüphaneyi ekleyip verimizi bir başka değişkene LabelEncoder şeklinde kaydedelim.

from sklearn.preprocessing import LabelEncoder
data2 = data.apply(LabelEncoder().fit_transform)
# data2 adında bir LabelEncoder formatına getirdik ve bunu aynı zamanda transformunu yaptık.

# Şimdi verimizi parçalıyoruz. Ve kontrol ediyoruz.
play = data2.iloc[:,-1:].values
print(play)
windy = data2.iloc[:,-2:-1].values
print(windy)

# Outlook kolonunu OneHotEncoder tarzında yazacağız. Bu yüzden Kütüphanesini import ediyoruz.
outlook = data2.iloc[:,:1]
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categories="auto")
outlook=ohe.fit_transform(outlook).toarray()
print(outlook)

# Sonra bu outlook'u veriye aktarmadan önce DataFrame formatına dönüştürüyoruz.
# Veri olarak outlook, indexleri için 1-14'e kadar, kolon adları için ["o","r","s"] koyduk
hava_durumu = pd.DataFrame(data = outlook, index= range(14), columns=["o","r","s"] )

# Son işlem olarak hepsini bir yerde toplamak gerekiyor.
son_veri = pd.concat([hava_durumu,data.iloc[:,1:3]],axis=1)
print(son_veri)
son_veri = pd.concat([son_veri,data2.iloc[:,-2:]],axis=1)
print(son_veri)

# Şidmi modelimizin eğitimi için veri setini bölüyoruz. Bunu için train_test_split fonksiyonunu kullanıyoruz.
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(son_veri.iloc[:,:-1],son_veri.iloc[:,-1:],test_size=0.33,random_state=0)

# Linear Regression kütüphanesini import ettik
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
# Modelimizi tahmin modelini inşa ettik
regression.fit(x_train,y_train)
y_pred = regression.predict(x_test)
# Kontrollerimizi yapıyoruz. Burada da 4. hariç diğerlerini 1'e yakın tahmin ettiğini görüyoruz.
print(y_pred)
print(y_test)

# P value değerini hesaplayıp veriyi geriye doğru eleme yöntemini kullanarak eleme yapacağız.
import statsmodels.api as sm

X = np.append(arr= np.ones((14,1)).astype(float), values=son_veri.iloc[:,:-1],axis=1)

X_l = son_veri.iloc[:,[0,1,2,3,4,5]].values
X_l = np.array(X_l,dtype=float)
model = sm.OLS(son_veri.iloc[:,-1:],X_l).fit()
print(model.summary())
# Modelimizin hangi kolonu sıkıntılıymış onu konrtol edelim.
# print(son_veri.iloc[:,3:4])

# Burada baktığımız temperature kolonu sonuçu kötü etkilemekte bu yüzden o kolonu kaldırıp tekrarden deniyeceğiz.
X_l = son_veri.iloc[:,[0,1,2,4,5]].values
X_l = np.array(X_l,dtype=float)
model = sm.OLS(son_veri.iloc[:,-1:],X_l).fit()
print(model.summary())

# Modelimiz daha iyi hale geldi 

