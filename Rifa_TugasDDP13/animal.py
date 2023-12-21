class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

class Badak(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran_cula, warna_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_cula = ukuran_cula
        self.warna_kulit = warna_kulit

    def serang(self):
        print(f"{self.name} sedang menyerang!")

    def makan(self):
        print(f"{self.name} sedang makan rumput.")

class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenisSirip, warna_sisik):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_sirip = jenisSirip
        self.warna_sisik = warna_sisik

    def berenang(self):
        print(f"{self.name} sedang berenang.")

    def makan(self):
        print(f"{self.name} sedang makan {self.makanan}.")

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, berbisa, panjang):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.berbisa = berbisa
        self.panjang = panjang

    def merayap(self):
        print(f"{self.name} sedang merayap.")

    def berburu(self):
        print(f"{self.name} sedang berburu mangsa.")

# Contoh penggunaan:
badak = Badak("Badak", "rumput", "darat", "melahirkan", "besar", "abu-abu")
badak.serang()
badak.makan()

ikan = Ikan("Nemo", "plankton", "air", "bertelur", "dual", "warna-warni")
ikan.berenang()
ikan.makan()

ular = Ular("Cobra", "reptil kecil", "darat", "bertelur", True, "panjang")
ular.merayap()
ular.berburu()
