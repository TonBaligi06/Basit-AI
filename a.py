# kodu kopyalamadan önce ingilizce diline çevirin(hatalar çıkabilir)
import math

# Basit veri tabanı: soru türleri ve mantıklı cevaplar
bilgi = {
    "selam": "Merhaba! Nasıl yardımcı olabilirim?",
    "nasılsın": "İyiyim! Seninle sohbet etmek güzel.",
    "adın ne": "Ben Python ile yapılan bir yapay zekayım. Nasıl yardımcı olabilirim?",
    "hava": "Hava durumunu bilemem ama umarım senin havan iyidir :)",
    "bana tavsiye ver": "En iyi tavsiyem: Bugün yeni bir şey öğrenmeye çalış.",
    "üzgünüm": "Üzgün olduğunu duymak üzücü… Konuşmak istersen buradayım.",
    "mutluyum": "Ne güzel! Mutluluk bulaşıcıdır :)",
    "korkuyorum": "Korkmak normaldir. Ama yalnız değilsin.",
    "gün": "Günün güzel geçiyordur umarım!",
    "ingilizce mi öğrensem sence": "Ooo. Çok iyi fikir. Hemen başla bence. Örneğin Duolingo ile başlayabilirsin. Yeni başlayanlar için mükemel"
}

# Cümleleri kelimelere ayırıp vektör yap
def vektörize(cümle):
    kelimeler = cümle.lower().split()
    v = {}
    for k in kelimeler:
        v[k] = v.get(k, 0) + 1
    return v

# Kosinüs benzerliği
def benzerlik(v1, v2):
    ortak = set(v1.keys()) & set(v2.keys())
    pay = sum(v1[k] * v2[k] for k in ortak)
    a = math.sqrt(sum(x*x for x in v1.values()))
    b = math.sqrt(sum(x*x for x in v2.values()))
    if a * b == 0:
        return 0
    return pay / (a * b)

def cevapla(soru):
    soru_v = vektörize(soru)
    en_iyi = None
    en_skor = 0

    for anahtar, cevap in bilgi.items():
        skor = benzerlik(soru_v, vektörize(anahtar))
        if skor > en_skor:
            en_skor = skor
            en_iyi = cevap
    
    if en_iyi is None:
        return "Bunu tam anlamadım ama öğrenmek isterim!"
    return en_iyi


print("MiniAI: Merhaba! Bana bir şey sor :)")
while True:
    soru = input("Sen: ")
    if soru.lower() in ("çık", "exit", "quit"):
        print("MiniAI: Görüşürüz! :)")
        break
    print("MiniAI:", cevapla(soru))

