abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 


#fungsi enkripsi dengan parameter abjad
def enkripsi(abjad):
    kalimat = input("Masukkan Kalimat : ") 
    key = int(input("Masukkan Key : ")) 

    kalimat = kalimat.lower() 
    hasil = '' 
    for char in kalimat: 
      if char in abjad: 
        n = abjad.index(char) 
        encrypt = (n - key) 
        convert = abjad[encrypt]
        hasil = hasil + convert 
      else:
          hasil = hasil + ' ' 

    print(f"Hasil : {hasil}") 
#fungsi dekripsi dengan parameter abjad
def dekripsi(abjad):
    kalimat = input("Masukkan Kalimat : ")  
    key = int(input("Masukkan Key : ")) 

    kalimat = kalimat.lower() 
    hasil = '' 

    for char in kalimat:
        if char in abjad:
          n = abjad.index(char) 
          encrypt = (n + key)
          convert = abjad[encrypt]
          hasil = hasil + convert 
        else:
            hasil = hasil + ' '  
    print(f"Hasil : {hasil}") 
#menampilkan menu
pilihan = 'ya' 

while (pilihan == 'ya'): 
  print("Menu : ")
  print("1. Enkripsi Data")
  print("2. Dekripsi Data")
  print("3. Keluar")
  menu = input("Menu yang dipilih : ")

  if menu == '1':
    print("Menu Enkripsi") 
    enkripsi(abjad)
  elif menu == '2':
    print("Menu Dekripsi")  
    dekripsi(abjad) 
  elif menu == '3':
    print("Progam selesai, terimakasih :) ")
    break 
  else:
    print("Menu tidak ditemukan") 

  pilihan = input("Apakah anda ingin melanjutkan ? (ya/tidak) : ") 
