import pandas as pd
import os

def read_csv_files_in_folder(folder_path):
    csv_data = []

    # Mendapatkan daftar file dalam folder
    files = os.listdir(folder_path)

    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path, on_bad_lines='skip')
            csv_data.append(df)

    return csv_data

if __name__ == "__main__":
    folder_path = "csv_file"  # Ganti dengan path folder csv_file Anda
    data = read_csv_files_in_folder(folder_path)

    # Menampilkan data dari setiap file CSV
    for df in data:
        print(df)
