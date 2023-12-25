admin = {
    'username': ['admin1', 'admin2'],
    'name' : ['ekal', 'bono'],
    'password': ['123', '321']
}

direktur = {
    'username': ['direct1', 'direct2'],
    'name' : ['raden', 'thebon'],
    'password': ['123', '321']
}

customer_service = {
    'username' : ['cs1', 'cs2'],
    'name' : ['aliess', 'anton'],
    'password' : ['123', '321']
}

teller = {
    'username': ['teller1', 'teller2'],
    'name' : ['Tony', 'sucipto'],
    'password': ['123', '321']
}

nasabah = {
    'username' : ['Haikaltok', 'Luna', 'Arden', 'Bondan'],
    'name' : ['haikal', 'lunaa', 'raden', 'bono'],
    'password' : ['123', '321', '333', '444'],
    'transaksi' : [1050, 2020, 3000, 5000],
    'debit' : [1000, 2000, 3000, 4000],
    'kredit' : [0, 0, 1, 2],
    'bunga' : [5, 10, 6, 7], # dalam persen
    'biaya_administrasi' : [0, 0, 5, 5]
}

class bank:
    def __init__(self, username, name, password, mode):
        self.username = username
        self.name = name
        self._password = password
        self.mode = mode
    
    def main_menu(self):
        print('Pilih Menu: ')
        print('1. Masuk Sebagai Admin')
        print('2. Masuk Sebagai Direktur')
        print('3. Masuk Sebagai Customer Service')
        print('4. Masuk Sebagai Teller')
        print('5. Keluar')
        return int(input('Masukkan Jenis Akun Kamu: '))
    
    def keluar(self):
        print('Selamat Tinggal !')
        return False

    def sign_in(self):
        username = input('Enter Username: ')
        password = input('Enter Password: ')
        return username, password

    def login(self, mode):
        username, password = self.sign_in()
        for username_tersimpan, password_tersimpan, nama_tersimpan in zip(mode['username'], mode['password'], mode['name']):
            if username == username_tersimpan and password == password_tersimpan:
                return username_tersimpan, nama_tersimpan, password_tersimpan
        return '', '', ''
            
    def sign_up(self):
        username = input('Enter Username: ')
        name = input('Enter Your Name: ')
        password = input('Enter Password: ')
        return username, name, password        
    
    def cari_akun(self, username, password, mode):
        for i, j in zip(mode['username'], mode['password']):
            if username == i and password == j:
                return True
        return False
    
    def tambahData(self, tujuan, role):
        new_username, new_name, new_password = self.sign_up()
        tujuan['username'].append(new_username)
        tujuan['name'].append(new_name)
        tujuan['password'].append(new_password)
        if role == 'cs':
            tujuan['transaksi'].append(int(input('Masukkan Nilai Transaksi Pertama: ')))
            tujuan['debit'].append(0)
            tujuan['kredit'].append(0)
            tujuan['bunga'].append(0)
            tujuan['biaya_administrasi'].append(0)
        print('Data Telah Ditambahkan')      

    def gantiData(self, tujuan, role):
        old_username, old_password = self.sign_in()
        if self.cari_akun(old_username, old_password, tujuan):
            for i, username in enumerate(tujuan['username']):
                if username == old_username:
                    print('Tolong Isi Dengan Data Baru :')
                    if role != 'teller':    
                        tujuan['username'][i], tujuan['name'][i], tujuan['password'][i] = self.sign_up()
                        if role == 'cs':
                            tujuan['transaksi'][i] = int(input('Masukkan Nilai Transaksi Yang Baru: '))
                    elif role == 'teller':
                        tujuan['debit'][i] = int(input('Masukkan Nilai Debit Yang Baru: '))
                        tujuan['kredit'][i] = int(input('Masukkan Nilai Kredit Yang Baru: '))
                        tujuan['bunga'][i] = int(input('Masukkan Nilai Bunga Yang Baru (dalam persen) : '))
                        tujuan['biaya_administrasi'][i] = int(input('Masukkan Nilai Biaya Administrasi Yang Baru: '))
            print('Data Telah Diubah!')
        else:
            print('Data Tidak Ditemukan!')
            tambah = input('Ingin Menambah Data Baru (y/n)? ')
            if tambah.lower() == 'y':
                self.tambahData(tujuan, role)

    def cek_anggota(self, role, tujuan, key):
        if role == 'teller':
            print(f'No.\tUsername\tNama\tDebit\tKredit\tBunga\tBiaya Admin')
            for i in range(len(tujuan[key])):
                print(f"{i+1}.\t{tujuan['username'][i]}\t{tujuan['name'][i]}\t{tujuan['debit'][i]}\t{tujuan['kredit'][i]}\t{tujuan['bunga'][i]}\t{tujuan['biaya_administrasi'][i]}")
        else:
            print(f'No.\tUsername\t{key}')
            for i in range(len(tujuan[key])):
                print(f"{i+1}.\t{tujuan['username'][i]}\t{tujuan[key][i]}")

    def cek_keuangan(self, find, key):
        total = 0
        if find == 'transaksi' : 
            print(f'No.\tNama\tTransaksi')
            for i in range(len(key['transaksi'])):
                print(f"{i+1}.\t{key['name'][i]}\t{key['transaksi'][i]}")
        else:
            for i in range(len(key['transaksi'])):
                if isinstance(key['transaksi'][i], int):
                    total += key['transaksi'][i]
            if total != 0:
                return total
    
    def laporan_keuangan(self, cari, role):
        print(f'Nilai keuangan bank ini adalah sebesar: {self.cek_keuangan(cari , role)}')

class Admin(bank):
    def __init__(self, username, name, password, mode):
        super().__init__(username, name, password, mode)
    
    def tambah_data(self, edit):
        print('Tolong isi data dibawah ini: ')
        self.tambahData(edit, 'direktur')

    def edit_data(self, edit):
        self.cek_anggota('admin', direktur, 'name')
        print('Tolong isi data yang ingin di ganti: ')
        self.gantiData(edit, 'admin')

    def verifikasi(self):
        return self.cari_akun(self.username, self._password, self.mode)

    def menu(self):
        print('Pilih Jabatan Yang Ingin Diganti:')
        print('1. Direktur')
        print('2. Teller')
        print('3. Keluar')

    def menu_ganti(self, destination):
        print('Pilih Menu:')
        print(f'1. Tambah {destination} Baru')
        print(f'2. Edit {destination}')
        print('3. Kembali')

class Direktur(bank):
    def __init__(self, username, name, password, mode):
        super().__init__(username, name, password, mode)

    def lihat_transaksi(self):
        tujuan = nasabah
        cari = 'transaksi'
        self.cek_keuangan(cari, tujuan)
    
    def lihat_laporan(self):
        tujuan = nasabah
        cari = ''
        self.laporan_keuangan(cari, tujuan)

    def lihat_data(self, tujuan, key):
        self.cek_anggota('direktur', tujuan, key)
    
    def verifikasi(self):
        return self.cari_akun(self.username, self._password, self.mode)

    def menu(self):
        print('Pilih Menu')
        print('1. Lihat Data Transaksi Keuangan Nasabah ')
        print('2. Lihat Laporan Keuangan Bank')
        print('3. Lihat Data Customer Service')
        print('4. Lihat Data Teller')
        print('5. Keluar')

class CustomerService(bank):
    def __init__(self, username, name, password, mode):
        super().__init__(username, name, password, mode)
    
    def tambah_data(self):
        print('Tolong Isi Data Di bawah ini: ')
        tujuan = nasabah
        self.tambahData(tujuan, 'cs')
    
    def edit_data(self):
        self.cek_anggota('cs', nasabah, 'transaksi')
        print('Pilih Data Nasabah yang ingin Diganti')
        tujuan = nasabah
        self.gantiData(tujuan, 'cs')

    def verifikasi(self):
        return self.cari_akun(self.username, self._password, self.mode)
    
    def menu(self):
        print('Pilih Menu: ')
        print('1. Menambah Data Nasabah')
        print('2. Mengedit Data Nasabah')
        print('3. Keluar')
    
class Teller(bank):
    def __init__(self, username, name, password, mode):
        super().__init__(username, name, password, mode)
    
    def tambah_data(self):
        tujuan = nasabah
        self.cek_anggota(' ', tujuan, 'username')
        print('Tolong Isi Data Dibawah ini:')
        self.gantiData(tujuan, 'teller')

    def lihat_data(self):
        tujuan = nasabah
        self.cek_anggota('teller', tujuan, 'transaksi')

    def verifikasi(self):
        return self.cari_akun(self.username, self._password, self.mode)

    def menu(self):
        print('Pilih Menu: ')
        print('1. Tambah Data Transaksi Nasabah')
        print('2. Lihat Data Transaksi Nasabah')
        print('3. Keluar')

aplikasi = bank('', '', '', '')
start = True
while start == True:
    role = aplikasi.main_menu()
    if role == 1:
        username, name, password = aplikasi.login(admin)
        mode = Admin(username, name, password, admin)
        
        if mode.verifikasi():
            while True:
                mode.menu()
                jabatan = int(input('Pilihan Kamu: '))
                if jabatan < 4:
                    if jabatan == 1:
                        edit = direktur
                        destination = 'Direktur'
                    elif jabatan == 2:
                        edit = teller
                        destination = 'teller'
                    elif jabatan == 3:
                        break
                    mode.menu_ganti(destination)
                    option = int(input('Opsi Kamu: '))
                    while option != 3:
                        if option == 1:
                            mode.tambah_data(edit)
                        elif option == 2:
                            mode.edit_data(edit)
                        else:
                            break
                        mode.menu_ganti(destination)
                        option = int(input('Opsi Kamu: '))
                    if option not in [1,2,3]:
                        print('Harap Pilih Pilihan Yang Ada')
                else:
                    print('Harap Pilih Pilihan Yang Ada')
        else :
            print('Akun Tidak Ditemukan!')
    elif role == 2:
        username, name, password = aplikasi.login(direktur)
        mode = Direktur(username, name, password, direktur)
        if mode.verifikasi():
            while True:
                mode.menu()
                option = int(input('Pilihanmu: '))
                if option == 1:
                    mode.lihat_transaksi()
                elif option == 2:
                    mode.lihat_laporan()
                elif option == 3:
                    mode.lihat_data(customer_service, 'name')
                elif option == 4:
                    mode.lihat_data(teller, 'name')
                else:
                    break
        else :
            print('Akun Tidak Ditemukan!')
    elif role == 3:
        username, name, password = aplikasi.login(customer_service)
        mode = CustomerService(username, name, password, customer_service)
        if mode.verifikasi():
            while True:
                mode.menu()
                opsi = int(input('Pilihanmu: '))
                if opsi == 1:
                    mode.tambah_data()
                elif opsi == 2:
                    mode.edit_data()
                else: 
                    break
        else :
            print('Akun Tidak Ditemukan!')
    elif role == 4:
        username, name, password = aplikasi.login(teller)
        mode = Teller(username, name, password, teller)
        if mode.verifikasi():
            while True:
                mode.menu()
                opsi = int(input('Pilihan kamu: '))
                if opsi == 1:
                    mode.tambah_data()
                elif opsi == 2:
                    mode.lihat_data()
                else:
                    break
        else :
            print('Akun Tidak Ditemukan!')
    elif role == 5:
        start = aplikasi.keluar()