# DataScience_Python_Practices
EN

This repository contains the practices I have done while learning data science using Python. It includes various studies on data analysis, data visualization, and statistics.

## Python Libraries:

**-NumPy:** Mathematical operations and multi-dimensional arrays

**-Pandas:** Data analysis and manipulation

**-Matplotlib & Seaborn:** Data visualization


### NumPy (Numerical Python)

NumPy is a library used for multi-dimensional arrays and scientific computations.

  -Performs fast and efficient matrix operations.

  -Provides optimized data storage and processing capabilities compared to lists using np.array.

  -Includes linear algebra, Fourier transforms, and statistical functions.

Example:
```
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.mean())  # Calculates the average
```

### Pandas (Python Data Analysis Library)
Pandas is a library used for data analysis and manipulation.

  -Processes data in tabular format using DataFrame and Series structures.
  
  -Easily reads/writes files such as CSV, Excel, and SQL.
  
  -Offers powerful features like filtering, grouping, and handling missing data.

Example:
```
import pandas as pd
df = pd.DataFrame({"Ad": ["Ahmet", "Zeynep"], "Yaş": [25, 30]})
print(df.head())  # Shows first 5 rows
```

### Matplotlib (Mathematical Plotting Library)
Matplotlib is one of the fundamental libraries used for graphs and data visualization.

  -Can create line plots, histograms, bar charts, etc.

  -Provides customization options such as axis labeling, adding titles, and changing colors and styles.

  -Supports 2D and 3D visualizations.

Example:
```
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, marker='o', linestyle='--')
plt.title("Sample Chart")
plt.show()
```

### Seaborn

Seaborn is an advanced data visualization library built on top of Matplotlib.

  -Produces more elegant and detailed graphs.

  -Offers support for statistical visualizations (e.g., correlation, distribution).

  -Works seamlessly with Pandas DataFrames.

Example:
```
import seaborn as sns
import pandas as pd
df = pd.DataFrame({"Category": ["A", "B", "C"], "Value": [10, 30, 20]})
sns.barplot(x="Category", y="Value", data=df)
```

TR

Bu repo, Python kullanarak veri bilimi (Data Science) öğrenirken yaptığım pratikleri içerir. İçerisinde veri analizi, veri görselleştirme, ve istatistik konularına dair çeşitli çalışmalar bulunmaktadır.


##Python Kütüphaneleri:

  **NumPy:** Matematiksel işlemler ve çok boyutlu diziler (arrays)

  **Pandas:** Veri analizi ve manipülasyonu

  **Matplotlib & Seaborn:** Veri görselleştirme


### NumPy (Numerical Python)

NumPy, çok boyutlu diziler (arrays) ve bilimsel hesaplamalar için kullanılan bir kütüphanedir.

  -Hızlı ve verimli matris işlemleri yapar.

  -np.array ile listelere kıyasla daha optimize veri saklama ve işlem imkanı sunar.

  -Lineer cebir, Fourier dönüşümü ve istatistiksel fonksiyonlar içerir.

 Örnek:
```
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.mean())  # Ortalamayı hesaplar
```

### Pandas (Python Data Analysis Library)

Pandas, veri analizi ve manipülasyonu için kullanılan bir kütüphanedir.

  -DataFrame ve Series yapılarıyla verileri tablo formatında işler.

  -CSV, Excel, SQL gibi dosyaları kolayca okuma/yazma işlemleri yapar.

  -Filtreleme, gruplama ve eksik veri işlemleri gibi güçlü özelliklere sahiptir.

Örnek:
```
import pandas as pd
df = pd.DataFrame({"Ad": ["Ahmet", "Zeynep"], "Yaş": [25, 30]})
print(df.head())  # İlk 5 satırı gösterir
```

### Matplotlib (Mathematical Plotting Library)

Matplotlib, grafik ve veri görselleştirme için kullanılan temel kütüphanelerden biridir.

  -Çizgi grafikleri, histogramlar, çubuk grafikleri vb. oluşturabilir.

  -Ekseni etiketleme, başlık ekleme, renk ve stil değiştirme gibi özelleştirmeler sağlar.

  -2D ve 3D görselleştirmeler yapılabilir.


Örnek:
```
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, marker='o', linestyle='--')
plt.title("Örnek Grafik")
plt.show()
```

### Seaborn

Seaborn, Matplotlib üzerine inşa edilmiş gelişmiş bir veri görselleştirme kütüphanesidir.

  -Daha şık ve detaylı grafikler üretir.

  -İstatistiksel görselleştirme desteği sunar (korelasyon, dağılım vb.).

  -Pandas DataFrame ile kolayca çalışır.


Örnek:
```
import seaborn as sns
import pandas as pd
df = pd.DataFrame({"Kategori": ["A", "B", "C"], "Değer": [10, 30, 20]})
sns.barplot(x="Kategori", y="Değer", data=df)
```

