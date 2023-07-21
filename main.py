import pandas as pd
import os

def read_csv_files_in_folder(folder_path):
    csv_data = []

    # Mendapatkan daftar file dalam folder
    files = os.listdir(folder_path)

    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path, sep='|')
            csv_data.append(df)

    return csv_data

if __name__ == "__main__":
    folder_path = "csv_file"  # Ganti dengan path folder csv_file Anda
    data = read_csv_files_in_folder(folder_path)

    # Menampilkan data dari setiap file CSV
    for df in data:
       print(df)
     # Mengeluarkan data kolom per kolom
    print("Data pada kolom 'Well Name':")
    print(df['Well Name'])

    print("\nData pada kolom 'Card Time':")
    print(df['Card Time'])

    print("\nData pada kolom 'Card Type':")
    print(df['Card Type'])

    print("\nData pada kolom 'Stroke Period':")
    print(df['Stroke Period'])

    print("\nData pada kolom 'SPM':")
    print(df['SPM'])

    print("\nData pada kolom 'Stroke Length':")
    print(df['Stroke Length'])

    print("\nData pada kolom 'Hours Since Gauge Off':")
    print(df['Hours Since Gauge Off'])

    print("\nData pada kolom 'Surface Max Load':")
    print(df['Surface Max Load'])

    print("\nData pada kolom 'Surface Min Load':")
    print(df['Surface Min Load'])

    print("\nData pada kolom 'PositionLimit':")
    print(df['PositionLimit'])

    print("\nData pada kolom 'Surface Positions':")
    print(df['Surface Positions'])

    print("\nData pada kolom 'Surface Loads':")
    print(df['Surface Loads'])

    print("\nData pada kolom 'Downhole Positions':")
    print(df['Downhole Positions'])

    print("\nData pada kolom 'Downhole Loads':")
    print(df['Downhole Loads'])