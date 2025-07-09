import random
from adam_kelimeler import kelimeler #Başka dosyadan çağırmak
from adam_resim import adam
can=6
kelime = random.choice(kelimeler).lower().strip() #Kelime listesinden rastegele seçiyor
gorunecek_bosluk= "_" * len(kelime)
print(gorunecek_bosluk)
oyun_bitti = False
harf_birlestir= []
while not oyun_bitti:
    print(f"*************** {can}/6 Hakkınız Var****************")
    kullanıcı_harf=input("Harf Giriniz: ").strip().lower() #Küçük harfe çevir
    print(kullanıcı_harf)
    if kullanıcı_harf in harf_birlestir: #Kullanıcı aynı harfi yazarsa diye
        print(f"Bu harfi söylediniz {kullanıcı_harf}")
    sonuc=""   #Boşluğa harfin yerleştirimei burada oldu
    for harfler in kelime:
        if harfler == kullanıcı_harf:
            sonuc += harfler
            harf_birlestir.append(kullanıcı_harf) #Harfleri ekledik bunla
        elif harfler in harf_birlestir: #Harfler yerlerine cevaplarla yerleşiyor
            sonuc += harfler
        else:
            sonuc += "_"
    print(sonuc)
    if kullanıcı_harf not in kelime: #Yanlış kelime olduğunda adama eklencekler
        can -= 1
        print(f"Senin harf {kullanıcı_harf}, bu kelimede yok. Adamı asıyorsun dikkat et!!!")
        if can == 0:
            oyun_bitti= True
            print(f" ): KAYBETTİN Adam Asıldı Kelimeniz: {kelime} :(")
    if "_" not in sonuc:   #Döngüden buradan çıkıyoz
        oyun_bitti = True
        print(" (: KAZANDIN Adamı Kurtardın :)")
    print(adam[can])