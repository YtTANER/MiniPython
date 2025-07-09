import random
tas = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
kagıt = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
makas= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Hoş Geldiniz oyunumuza")
sekiller=[tas,kagıt,makas]
secim=int(input("Taş için (0) , Kağıt için (1), Makas için (2) seçiniz"))
if secim >=0 and secim <=2:
     print(sekiller[secim])  #Görüntüyü yaparız
pc_secim=random.randint(0,2)
print(f"PC seçimi: ")
print(sekiller[pc_secim]) #Görüntüyü yaparız
if secim>=3:
    print("Geçersiz Sayı Girdiniz")
elif secim == 0 and pc_secim == 2:
    print("Kullanıcı Kazandı")
elif pc_secim==0 and secim==2:
    print("Bilgisayar kazandı")
elif secim > pc_secim:
    print("Kullanıcı Kazandı")
elif pc_secim > secim:
    print("Bilgisayar kazandı")
elif secim == pc_secim:
    print("Berabere")
elif secim>=3:
    print("Geçersiz Sayı Girdiniz")