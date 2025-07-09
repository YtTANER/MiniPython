print(r'''
*******************************************************************************
                     ______
                   /|_||_\`.__
                  (   _    _ _\
                  =`-(_)--(_)-'      
*******************************************************************************
          HOŞ GELDİN!
    Gizemli ormana adım attın. Pusulan yok zamanın az!
        Kurtulmak için doğru seçimleri yapmalısın...
*******************************************************************************
''')
print("Gözlerini ıssız bir ormanda açtın. Önünde iki yol var.")
yol = input("Yol Seçiniz: Sağ Veya Sol !!!").strip().lower()

if yol == "sağ":
    print("Tebrikler bir araç buldun!")
    arac = input("Arabaya B veya D").strip().lower()
    if arac == "b":
        print("Tebrikler bir Silah buldun! ")
        silah = input(" Silahı SIK Silahı ALMA HİÇBİRİ Cevabı S A H yazın!!!").strip().lower()
        if silah =="s":
            print("Tebrikler silah yerinizi belli etti ve bulundunuz")
        elif silah =="a":
            print("Kısa süre sonra karşılaştığın tehlikeli bir yaratık seni yakaladı")
        elif silah =="h":
            print("Silah kaza yapınca patladı ve araba yandı")
        else:
            print("Geçersiz seçim! OYUN BİTTİ!")
    elif arac == "d":
        print("Ancak sık ağaçların arasında yönünü kaybettin. OYUN BİTTİ!")
elif yol == "sol":
    print("Ormanda kayboldun ve çıkış yolunu bulamadın. OYUN BİTTİ!")
else:
    print("Geçersiz seçim! OYUN BİTTİ!")

#strip() ile baştaki ve sondaki boşlukları temizler
#lower() ile tüm karakterleri küçük harfe çevirir