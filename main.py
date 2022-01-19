"""
APLIKASI DETEKSI GEMPA TERKINI
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
from gempaterkini import ekstrasi_data,tampilkan_data

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstrasi_data()
    tampilkan_data (result)