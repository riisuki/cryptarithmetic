# PROGRAM CRYPTARITHMETIC
import time

# INISIALISASI VARIABEL
tabelHuruf = []
nilaiHuruf = []

# DEFINISI FUNGSI
def CharToInt(char):
    if char == '1':
        return 1
    elif char == '2':
        return 2
    elif char =='3':
        return 3
    elif char =='4':
        return 4
    elif char == '5':
        return 5
    elif char == '6':
        return 6
    elif char == '7':
        return 7
    elif char == '8':
        return 8
    elif char == '9':
        return 9
    else:
        return 0

def IntToChar(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    elif n == 2:
        return '2'
    elif n == 3:
        return '3'
    elif n == 4:
        return '4'
    elif n == 5:
        return '5'
    elif n == 6:
        return '6'
    elif n == 7:
        return '7'
    elif n == 8:
        return '8'
    else:
        return '9'
    
def StringToInt(string):
    hasil = 0
    for a in string:
        hasil = hasil*10 + CharToInt(a)

    return hasil

def LetterToNumber(string):
    hasil = ""
    for a in string:
        i = 0
        while a != tabelHuruf[i]:
            i = i + 1
        if nilaiHuruf[i] != 'X':
            hasil += nilaiHuruf[i]
    return StringToInt(hasil)

def InitTabelHuruf():
    global hurufOp
    global hurufHasil
    global tabelHuruf
    for char in hurufHasil:
        if char not in tabelHuruf:
            tabelHuruf.append(char)
    for kata in hurufOp:
        for char in kata:
            if char not in tabelHuruf:
                tabelHuruf.append(char)

def InitNilaiHuruf():
    global tabelHuruf
    global nilaiHuruf
    for i in range (0,len(tabelHuruf)):
        if i == 0:
            nilaiHuruf.append('1')
        elif i == 1:
            nilaiHuruf.append('0')
        else:
            nilaiHuruf.append(IntToChar(i))
        
def IsHurufAwalNol():
    hurufawal = False
    global hurufOp
    global hurufHasil
    global tabelHuruf
    global nilaiHuruf

    i = 0
    while (not hurufawal) and (i < len(tabelHuruf)):
        if nilaiHuruf[i] == '0':
            #Jika ada yang nilainya nol
            for kata in hurufOp:
                if kata[0] == tabelHuruf[i]:
                    hurufawal = True
            if hurufHasil[0] == tabelHuruf[i]:
                hurufawal = True
        i = i + 1
    return hurufawal

def ListToInt(li):
    hasil = 0
    for a in li:
        hasil = hasil * 10 + CharToInt(a)
    return hasil

def IntToList(angka, length):
    hasil = []
    while angka > 0:
        x = angka % 10
        angka = angka // 10
        hasil.append(IntToChar(x))
    hasil2 = []
    for i in range(0,length-len(hasil)):
        hasil2.append('0')
    for j in hasil[::-1]:
        hasil2.append(j)
    return hasil2

def IsNotUnique():
    temp = []
    notunik = False
    global nilaiHuruf
    for char in nilaiHuruf:
        if char not in temp:
            temp.append(char)
        else:
            notunik = True
    return notunik
    
def NextTry():
    global nilaiHuruf
    while True:
        curr = ListToInt(nilaiHuruf)
        curr = curr + 1
        newlist = IntToList(curr,len(nilaiHuruf))
        for i in range(0,len(nilaiHuruf)):
            nilaiHuruf[i] = newlist[i]
        if not IsNotUnique():
            break

def IsMaxList():
    global nilaiHuruf
    i = 0
    isMax = True
    while (isMax) and (i<len(nilaiHuruf)):
        if nilaiHuruf[i] != len(nilaiHuruf) - 1:
            isMax = False
        else:
            i = i + 1
    if isMax:
        print(nilaiHuruf)
    return isMax

    
# PROGRAM UTAMA
# Setting: Berhenti setelah satu jawaban jika True
satujawab = True

# Menerima nama file input dan baca file
namaFile = input("Masukkan path file input: ")
file = open(namaFile, "r")
isiteks = file.readlines()
file.close()

# Proses input ke variabel dan print soal
# Mulai hitung waktu di sini
starttime = time.time()

hurufOp = []
hurufHasil = ""
bacahasil = False
print()
print("Hasil input:")
for baris in isiteks:
    print(baris.rstrip())
    a = baris.strip()
    if a[-1:] == '+':
        hurufOp.append(a[:-1])
    elif a[0] == '-':
        bacahasil = True
    elif bacahasil:
        hurufHasil += a
    else:
        hurufOp.append(a)

# Mulai percobaan
count = 0
jawab = False
selesai = False
print()
print("Jawaban:")
InitTabelHuruf()


if len(tabelHuruf) > 10:
    print("Tidak bisa dihitung karena huruf unik lebih dari 10.")
else:
    InitNilaiHuruf()
    
    while not selesai:
        if count > 0:
            NextTry()
            
        
        if not IsHurufAwalNol():
            if not satujawab:
                if IsMaxList():
                    selesai = True
                    
            totalOperand = 0
            count = count + 1
            for kata in hurufOp:
                # Cari hasil penjumlahan semua operand
                totalOperand += LetterToNumber(kata)
            totalHasil = LetterToNumber(hurufHasil)
            if totalHasil == totalOperand:
                # Jika benar, cetak jawaban
                jawab = True
                if satujawab:
                    selesai = True

                j = 0        
                for kata in hurufOp:
                    j = j + 1
                    for i in range(0,len(hurufHasil)-len(kata)):
                        print(" ", end="")
                    print(LetterToNumber(kata), end="")
                    if j == len(hurufOp):
                        print("+")
                    else:
                        print()
                for char in hurufHasil:
                    print("-", end="")
                print()
                print(LetterToNumber(hurufHasil))
                print()
                                 
if not jawab:
    print("Tidak ada solusi yang ditemukan.")
    
print()
print("Waktu eksekusi program:", time.time() - starttime, "detik.")
print("Total tes yang dilakukan:", count, "kali.")
