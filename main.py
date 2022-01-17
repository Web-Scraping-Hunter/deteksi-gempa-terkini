"""
APLIKASI DETEKSI GEMPA TERKINI
MODULARISASI DENGAN FUNCTION
"""


def ekstrasi_data():
    """
    Tanggal: 17 Januari 2022
    Waktu: 07:25:56 WIB
    Magnitudo: 5.4
    Kedalaman: 10 km
    Lokasi: 7.60 LS - 105.90 BT
    Pusat gempa: Pusat gempa berada di laut 84 km BaratDaya Bayah
    Dirasakan: Dirasakan (Skala MMI): II-III Cikembar, II-III Cireunghas, Kab. Sukabumi, II-III Pelabuhanratu, II-III Sumur, II-III Bogor, III Bayah, III Pandeglang, III Cikeusik, III Panimbang, II-III Jakarta Barat, II-III Jakarta Selatan, II-III Tambun
    :return:
    """
    hasil = dict()
    hasil["tanggal"] = "17 Januari 2022"
    hasil["waktu"] = "07:25:56 WIB"
    hasil["magnitudo"] = 5.4
    hasil["lokasi"] = {'ls': 7.60, 'bt': 105.90}
    hasil["pusat"] = "Pusat gempa berada di laut 84 km BaratDaya Bayah"
    hasil["dirasakan"] = "Dirasakan (Skala MMI): II-III Cikembar, II-III Cireunghas, Kab. Sukabumi, II-III Pelabuhanratu, II-III Sumur, II-III Bogor, III Bayah, III Pandeglang, III Cikeusik, III Panimbang, II-III Jakarta Barat, II-III Jakarta Selatan, II-III Tambun"

    return hasil


def tampilkan_data(result):
    print("gempa terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstrasi_data()
    tampilkan_data (result)