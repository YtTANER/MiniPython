import random 

harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sayılar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
semboller = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Şifre Oluşturucuya hoş geldiniz!")

soru_harf = int(input("Kaç harf istersiniz?\n"))
soru_sembol = int(input("Kaç sembol istersiniz?\n"))
soru_sayı = int(input("Kaç sayı istersiniz?\n"))  

sifre = "" 
karakterler = []

for karakter in range(0, soru_harf):
    karakterler.append(random.choice(harfler))
for karakter in range(0, soru_sembol):
    karakterler.append(random.choice(semboller))
for karakter in range(0, soru_sayı):
    karakterler.append(random.choice(sayılar))
random.shuffle(karakterler)  # Karakterlerin sırasını karıştır
karisik_sifre = ''.join(karakterler)  # Listeyi string hale getir
print(f"Şifreniz Oluşturulmuştur: {karisik_sifre}")
