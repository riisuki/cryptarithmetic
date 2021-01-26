#~~~~~~~~#
# README #
#~~~~~~~~#

i.   Deskripsi Program
     >> Program Cryptarithmetic
          Cryptarithmetic adalah puzzle penjumlahan dalam matematika. Dalam
        cryptarithmetic, angka penjumlahan diganti dengan huruf. Setiap
        angka direpresentasikan dengan huruf yang berbeda.
          Program menerima input persoalan cryptarithmetic dari file teks,
        kemudian mencetak hasil pemecahannya dengan algoritma brute force,
        waktu yang dibutuhkan untuk pemecahan, dan total tes yang dilakukan.


ii.  Requirements dan Instalasi
     >> Pastikan Anda sudah memiliki instalasi Python 3 terbaru.
        Informasi lebih lanjut dapat dilihat di https://www.python.org/
        Setelah itu, program dapat dijalankan melalui IDLE atau
        terminal.

iii. Cara Menggunakan
     >> Menjalankan Program
        a. Menggunakan IDLE
           Klik kanan file "main.py" pada folder src dan pilih "Edit
           with IDLE." Lalu, tekan F5 atau pilih Menu Run -> Run Module.
        b. Menggunakan Terminal
           Lakukan navigasi ke dalam folder src, lalu masukkan perintah
           "python main.py" tanpa tanda kutip.
           
     >> Memasukkan Input
        Masukkan path file input. Jika "main.py" dibuka dari folder src,
        maka path file adalah "../test/test_XX.txt" tanpa tanda petik,
        dengan XX diganti dengan angka sesuai nama file yang tersedia.
        
     >> Format File Input
        File input ditulis dengan huruf kapital dengan format seperti
        contoh berikut.
        
         SEND
         MORE+
        -----
        MONEY
        
        Untuk lebih dari 2 operand, contohnya adalah sebagai berikut.
        
         THREE
         THREE
           TWO
           TWO
           ONE+
        ------
        ELEVEN
        
        (Keterangan: Baris pertama dan seterusnya dalah operand, yang
                     diakhiri dengan tanda "+". Lalu, terdapat 1 baris
                     garis pembatas, diikuti dengan hasil penjumlahan.)
                     
     >> Pengaturan
        Terdapat opsi untuk terus mencetak jawaban lebih dari satu pada
        source code. Caranya gantilah nilai variabel satujawab di bawah
        komentar Setting menjadi False, lalu jalankan kembali "main.py".
        (Catatan: Fungsi eksperimental.)


iv.  Author
     >> Nama : Melita
        NIM  : 13519063
        Kelas: K-02
        