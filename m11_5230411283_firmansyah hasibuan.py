import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import os

def preprocessing_data(nama_file):
    print("\n[1] Proses Preprocessing Data")
    if not os.path.exists(nama_file):
        print("File tidak ditemukan!")
        return None
    
  
    try:
        df = pd.read_excel(nama_file)
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
        return None

    print("Data Awal:\n", df.head())
    
 
    print("Jumlah missing values sebelum preprocessing:\n", df.isnull().sum())
    
    df = df.dropna().drop_duplicates()
    print("Data setelah preprocessing:\n", df.head())
    print("Jumlah missing values setelah preprocessing:\n", df.isnull().sum())
    print("Shape data:", df.shape)
    
   
    if df.empty:
        print("Data kosong setelah preprocessing. Harap periksa file xlsx!")
        return None
    
    print("Kolom yang tersedia dalam data:", df.columns)
    return df

def analisis_data(df, parameter, target, algoritma):
    print("\n[2] Proses Analisis Data")
    
    
    if parameter not in df.columns or target not in df.columns:
        print(f"Kolom '{parameter}' atau '{target}' tidak ditemukan dalam data.")
        return
    
  
    df[parameter] = pd.to_numeric(df[parameter], errors='coerce')
    df[target] = pd.to_numeric(df[target], errors='coerce')
    df = df.dropna()  
    
    
    X = df[[parameter]]
    y = df[target]
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    
    if algoritma.lower() == 'linearregression':
        model = LinearRegression()
    elif algoritma.lower() == 'decisiontree':
        model = DecisionTreeRegressor()
    else:
        print("Algoritma tidak dikenal! Pilih 'LinearRegression' atau 'DecisionTree'.")
        return
    
    
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Prediksi Model:", predictions[:5])  
    
    
    print("Akurasi Training Score:", model.score(X_train, y_train))
    print("Akurasi Testing Score:", model.score(X_test, y_test))

def main():
    while True:
        print("\n===== PROGRAM ANALISIS DATA AIR QUALITY =====")
        pilihan = input("Lakukan Analisis? (ya/tidak): ").lower()
        if pilihan == 'ya':
            
            nama_file = input("Masukkan nama file xlsx: ")
            df = preprocessing_data(nama_file)
            if df is not None:
                
                parameter = input("Masukkan nama kolom parameter (fitur): ")
                target = input("Masukkan nama kolom target (label): ")
                algoritma = input("Pilih algoritma (LinearRegression/DecisionTree): ")
                
                
                analisis_data(df, parameter, target, algoritma)
        elif pilihan == 'tidak':
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Input tidak valid. Masukkan 'ya' atau 'tidak'.")

if __name__ == "__main__":
    main()
