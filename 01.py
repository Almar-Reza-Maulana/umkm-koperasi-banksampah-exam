# Query 1: Membuat Class untuk Sistem UMKM
class UMKMSystem:
    def __init__(self, nama_umkm):
        self.nama_umkm = nama_umkm
        self.anggota = []  # list kosong untuk menyimpan data anggota
        self.dana_pinjaman = 50000000  # Rp50 juta

    # Query 2: Method untuk Menambah Anggota UMKM
    def tambah_anggota(self, nama_anggota, jumlah_pinjaman):
        anggota_dict = {"nama": nama_anggota, "pinjaman": jumlah_pinjaman}
        self.anggota.append(anggota_dict)
        print(
            f"Anggota '{nama_anggota}' telah ditambahkan dengan pinjaman Rp{jumlah_pinjaman}"
        )

    # Query 3: Method untuk Menghitung Pengembalian Pinjaman
    def hitung_pengembalian(self, nama_anggota, tahun_pengembalian):
        # Mencari data anggota berdasarkan nama
        anggota = next(
            (anggota for anggota in self.anggota if anggota["nama"] == nama_anggota),
            None,
        )
        if anggota is None:
            print("Anggota tidak ditemukan!")
            return None
        # Menghitung bunga sederhana 5% per tahun: total = pinjaman * (1 + 0.05 * tahun)
        total = anggota["pinjaman"] * (1 + 0.05 * tahun_pengembalian)
        print(
            f"Total pengembalian pinjaman untuk '{nama_anggota}' selama {tahun_pengembalian} tahun: Rp{total}"
        )
        return total


# Query 4: Membuat Class untuk Koperasi, mewarisi class UMKMSystem
class Koperasi(UMKMSystem):
    def __init__(self, nama_koperasi):
        super().__init__(nama_koperasi)
        self.transaksi = []  # list kosong untuk menyimpan transaksi

    # Query 5: Method untuk Mencatat Transaksi Koperasi
    def catat_transaksi(self, nama_anggota, jenis_transaksi, jumlah):
        transaksi = {"nama": nama_anggota, "jenis": jenis_transaksi, "jumlah": jumlah}
        self.transaksi.append(transaksi)
        print(f"Transaksi dicatat: {transaksi}")

    # Query 6: Method untuk Menghitung Keuntungan Koperasi
    def hitung_keuntungan(self):
        total_jual = 0
        total_beli = 0
        for trx in self.transaksi:
            if trx["jenis"].lower() == "jual":
                total_jual += trx["jumlah"]
            elif trx["jenis"].lower() == "beli":
                total_beli += trx["jumlah"]
        keuntungan = total_jual - total_beli
        print(f"Total keuntungan koperasi: Rp{keuntungan}")
        return keuntungan


# Query 7: Membuat Class untuk Bank Sampah, mewarisi class UMKMSystem
class BankSampah(UMKMSystem):
    def __init__(self, nama_bank_sampah):
        super().__init__(nama_bank_sampah)
        # data_sampah menyimpan data per anggota dengan rincian jenis sampah dan jumlah (kg)
        self.data_sampah = {}

    # Query 8: Method untuk Mencatat Data Sampah
    def catat_sampah(self, nama_anggota, jenis_sampah, jumlah):
        # Jika data untuk anggota belum ada, inisialisasi sebagai dictionary kosong
        if nama_anggota not in self.data_sampah:
            self.data_sampah[nama_anggota] = {}
        # Jika jenis sampah sudah tercatat, tambahkan jumlahnya; jika belum, inisialisasi
        if jenis_sampah.lower() in self.data_sampah[nama_anggota]:
            self.data_sampah[nama_anggota][jenis_sampah.lower()] += jumlah
        else:
            self.data_sampah[nama_anggota][jenis_sampah.lower()] = jumlah
        print(
            f"Data sampah untuk '{nama_anggota}' telah diperbarui: {jenis_sampah} = {self.data_sampah[nama_anggota][jenis_sampah.lower()]} kg"
        )

    # Query 9: Method untuk Menghitung Nilai Tukar Sampah
    def hitung_nilai_tukar(self):
        # Menetapkan nilai tukar per kg untuk jenis sampah
        rates = {"plastik": 5000, "kertas": 2000}  # Rp5000/kg  # Rp2000/kg
        total_nilai = 0
        # Hitung nilai tukar berdasarkan data sampah setiap anggota
        for anggota, sampah in self.data_sampah.items():
            for jenis, jumlah in sampah.items():
                rate = rates.get(jenis, 0)
                total_nilai += jumlah * rate
        print(f"Total nilai tukar sampah: Rp{total_nilai}")
        return total_nilai

    # Query 10: Method untuk Pesan Edukasi Lingkungan
    def pesan_edukasi(self):
        # Hitung total sampah yang dikumpulkan seluruhnya
        total_sampah = sum(
            sum(jumlah for jumlah in data.values())
            for data in self.data_sampah.values()
        )
        if total_sampah >= 100:
            pesan = "Luar biasa! Terus kumpulkan sampah dan daur ulang untuk lingkungan yang lebih hijau."
        elif total_sampah >= 50:
            pesan = "Bagus! Mari tingkatkan upaya pengumpulan sampah untuk dampak yang lebih besar."
        else:
            pesan = "Mulailah dari yang kecil. Setiap sampah yang dikumpulkan membawa kita menuju lingkungan yang lebih bersih."
        print(pesan)
        return pesan


# Query 11: Integrasi Seluruh Komponen dalam Sistem Utama
def main():
    print("Selamat datang di Sistem Pengelolaan UMKM, Koperasi, dan Bank Sampah!")

    # Membuat instansi untuk setiap sistem
    umkm = UMKMSystem("UMKM Desa Sejahtera")
    koperasi = Koperasi("Koperasi Desa Sejahtera")
    bank_sampah = BankSampah("Bank Sampah Desa Sejahtera")

    while True:
        print("\n===== Menu Utama =====")
        print("1. Tambah Anggota UMKM")
        print("2. Hitung Pengembalian Pinjaman UMKM")
        print("3. Catat Transaksi Koperasi")
        print("4. Hitung Keuntungan Koperasi")
        print("5. Catat Data Sampah Bank Sampah")
        print("6. Hitung Nilai Tukar Sampah")
        print("7. Pesan Edukasi Lingkungan")
        print("8. Keluar")

        pilihan = input("Masukkan pilihan (1-8): ")

        if pilihan == "1":
            nama = input("Masukkan nama anggota UMKM: ")
            try:
                jumlah = int(input("Masukkan jumlah pinjaman (dalam rupiah): "))
            except ValueError:
                print("Input jumlah harus berupa angka!")
                continue
            umkm.tambah_anggota(nama, jumlah)

        elif pilihan == "2":
            nama = input("Masukkan nama anggota UMKM: ")
            try:
                tahun = int(input("Masukkan lama pinjaman (dalam tahun): "))
            except ValueError:
                print("Input tahun harus berupa angka!")
                continue
            umkm.hitung_pengembalian(nama, tahun)

        elif pilihan == "3":
            nama = input("Masukkan nama anggota untuk transaksi koperasi: ")
            jenis = input("Masukkan jenis transaksi (beli/jual): ")
            try:
                jumlah_trx = int(input("Masukkan jumlah transaksi (dalam rupiah): "))
            except ValueError:
                print("Input jumlah harus berupa angka!")
                continue
            koperasi.catat_transaksi(nama, jenis, jumlah_trx)

        elif pilihan == "4":
            koperasi.hitung_keuntungan()

        elif pilihan == "5":
            nama = input("Masukkan nama anggota bank sampah: ")
            jenis = input("Masukkan jenis sampah (misalnya, plastik/kertas): ")
            try:
                jumlah_sampah = float(input("Masukkan jumlah sampah (dalam kg): "))
            except ValueError:
                print("Input jumlah sampah harus berupa angka!")
                continue
            bank_sampah.catat_sampah(nama, jenis, jumlah_sampah)

        elif pilihan == "6":
            bank_sampah.hitung_nilai_tukar()

        elif pilihan == "7":
            bank_sampah.pesan_edukasi()

        elif pilihan == "8":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
