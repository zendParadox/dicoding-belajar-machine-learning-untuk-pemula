# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t3zhvoTeGeGTvEy6mvOGsUlkhwlu5OgZ
"""

# Mencoba membuat model menggunakan metode SVM (Support Vector Machine)

# Dataset berisi 8 kolom atribut dan 1 kolom label yang berisi 2 kelas yaitu
# 1 dan 0. Angka 1 menandakan bahwa orang tersebut positif diabetes dan 0
# menandakan sebaliknya. Terdapat 768 sampel yang merupakan 768 pasien perempuan
# keturunan suku Indian Pima.

# Model machine learning yang akan kita buat bertujuan untuk mengklasifikasikan
# apakah seorang pasien positif diabetes atau tidak.

# Tahapan :
# 1. Ubah data ke dalam DataFrame
# 2. Bagi dataset
# 3. Lakukan standarisasi
# 4. Buat dan latih model
# 5. Evaluasi model

import pandas as pd

df = pd.read_csv('diabetes.csv')
df.head()

df.info()

# memisahkan atribut pada dataset dan menyimpan nya pada sebuah variabel
X = df[df.columns[:8]]
y = df['Outcome']
X.head()

from sklearn.preprocessing import StandardScaler

# standarisasi nilai-nilai dari dataset
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

from sklearn.model_selection import train_test_split

# memisahkan data untuk training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.33, random_state=42)

from sklearn.svm import SVC

# membuat objek SVC dan memanggil fungsi fit untuk melatih model
clf = SVC()
clf.fit(X_train, y_train)

# menampilkan skor akurasi prediksi

clf.score(X_test, y_test)

