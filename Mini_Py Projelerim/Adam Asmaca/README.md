# ☠️ Adam Asmaca Oyunu (Python)
Bu Python projesi, klasik "Adam Asmaca" oyununun terminal versiyonudur.  
Kullanıcı, rastgele seçilen bir şehir ismini tahmin etmeye çalışır. Yanlış harflerde adam adım adım asılır!

## 🧠 Oyun Nasıl Çalışır?
- Program rastgele bir şehir ismi seçer (Türkiye'den).
- Oyuncu her seferinde bir harf tahmin eder.
- Doğru harfler yerleştirilir, yanlış harflerde adamın bir kısmı çizilir.
- Maksimum 6 hata hakkı vardır. Hatalar sonunda oyun biter.

## 🗂️ Dosya Yapısı
| Dosya Adı              | Açıklama                                              |
|------------------------|-------------------------------------------------------|
| `adam_asmaca.py`       | Ana oyun dosyası. Oyunun tüm akışını içerir.          |
| `adam_kelimeler.py`    | İçinde şehir isimlerinin bulunduğu kelime listesi     |
| `adam_resim.py`        | Her hata durumuna göre adamın ASCII çizimleri         |

## 🛠️ Kullanılan Python Özellikleri
| Özellik            | Açıklama                                              |
|--------------------|-------------------------------------------------------|
| `random.choice()`  | Şehir listesinden rastgele kelime seçimi              |
| `input()`          | Kullanıcıdan harf tahmini almak                       |
| `list`, `string`   | Kelimenin görünümü ve kontrol için kullanılır         |
| `if / elif / else` | Tahmin doğruluğu ve oyun akışını kontrol eder         |

## 🚀 Nasıl Çalıştırılır?
Aşağıdaki üç dosyanın aynı klasörde olduğundan emin olun:
   - `adam_asmaca.py`
   - `adam_kelimeler.py`
   - `adam_resim.py`
Aşağıdan çalıştırın:
Python adam_asmaca.py

