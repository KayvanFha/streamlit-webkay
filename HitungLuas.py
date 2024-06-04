import streamlit as st
from streamlit_option_menu import option_menu

#navigasi halaman sidebar
with st.sidebar :
    selected = option_menu('Hitung Luas Bangun Datar',
                            ['Home',
                             'Tutorial Penggunaan',
                             'Hitung Luas Persegi',
                             'Hitung Luas Persegi Panjang',
                             'Hitung Luas Segitiga',
                             'Hitung Luas Lingkaran',],)

#halaman home
if(selected == 'Home') :
    st.title("APLIKASI MENGHITUNG LUAS BANGUN DATAR")
    st.write("SELAMAT DATANG DI APLIKASI MENGHITUNG LUAS BANGUN DATAR SEDERHANA BUATAN KELOMPOK 4")
    st.write("KELOMPOK INI TERIDRI DARI 5 ANGGOTA :")
    st.write('1. Indah Meiladihi (16)')
    st.write('2. Isal Ziyad Mubarak (17)')
    st.write('3. Ivanna Zahra Azizah (18)')
    st.write('4. Jelita Alya Cantika (19)')
    st.write('5. Kayvan Fadhli Hafizh Ardavan (20)')

    st.write("SELAMAT MENGGUNAKAN")
    
#halaman tutorial penggunaan
if(selected == 'Tutorial Penggunaan') :
    st.title("LANGKAH PENGGUNAAN APLIKASI MENGHITUNG INI ADALAH SEBAGAI BERIKUT :")
    st.write("1. PILIH LUAS BANGUN DATAR MANA YANG INGIN DICARI")
    st.write("2. PASTIKAN KALIAN SUDAH MENGETAHUI NILAI NILAI YANG DIBUTUHKAN UNTUK MENCARI LUAS BANGUN DATAR TERSEBUT")
    st.write("4. MASUKKAN NILAI NILAI YANG DIMINTA UNTUK MENCARI LUAS BANGUN DATAR YANG DIPILIH")
    st.write("4. KLIK TOMBOL HITUNG LUAS (NAMA BANGUN DATAR YANG DICARI)")
    st.write("5. HASIL BERADA DI BAWAH, KALIAN TELAH SELESAI MENCARI LUAS BANGUN DATAR")

#halaman Hitung luas persegi
if(selected == 'Hitung Luas Persegi') :
    st.title("LUAS PERSEGI")

    sisi = st.number_input("Masukkan Sisi", 0)
    hitung = st.button("Hitung Luas Persegi")

    if hitung:
        luas = sisi * sisi
        st.success(f"Luas Persegi adalah = {luas} cm²")

#halaman hitung luas persegi panjang
if(selected == 'Hitung Luas Persegi Panjang') :
    st.title("LUAS PERSEGI PANJANG")

    panjang = st.number_input("Masukkan Panjang", 0)
    lebar = st.number_input("Masukkan Lebar", 0)
    hitung = st.button("Hitung Luas Persegi Panjang")

    if hitung:
        luas = panjang * lebar
        st.success(f"Luas Persegi Panjang adalah = {luas} cm²")

#halaman hitung luas segitiga
if(selected == 'Hitung Luas Segitiga') :
    st.title("LUAS SEGITIGA")

    alas = st.number_input("Masukkan Alas", 0)
    tinggi = st.number_input("Masukkan Tinggi", 0)
    hitung = st.button("Hitung Luas Segitiga")

    if hitung:
        luas = 1/2 * alas * tinggi
        st.success(f"Luas Segitiga adalah = {luas} cm²")

#halaman hitung luas Lingkaran
if(selected == 'Hitung Luas Lingkaran') :
    st.title("LUAS LINGKARAN")
    selected = option_menu ("Phi 22/7 or 3,14",
                            ['Phi = 22/7',
                            'Phi = 3,14'])
    
    if(selected == 'Phi = 22/7') :
         st.title("LUAS LINGKARAN (22/7)")
    
         r = st.number_input("Masukkan Jari Jari", 0)
         hitung = st.button("Hitung Luas Lingkaran")
            
         if hitung:
            luas = 22/7 * r * r
            st.success(f"Luas Lingkaran = {luas} cm²")
    
    if(selected == 'Phi = 3,14') :
        st.title("LUAS LINGKARAN (3,14)")

        r = st.number_input("Masukkan Jari Jari", 0)
        hitung = st.button("Hitung Luas Lingkaran")

        if hitung:
            luas = 3,14 * r * r
            st.success(f"Luas Lingkaran = {luas} cm²")
 
#UNTUK MENJALANKAN BUKA TERMINAL LALU BERI PERINTAH "Strimlit run HitungLuas.py"