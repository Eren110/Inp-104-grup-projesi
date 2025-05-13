import random

# Film ve dizi veritabanı
veritabani = {
    "Aksiyon": ["John Wick", "Mad Max: Fury Road", "The Dark Knight", "Mission: Impossible", "Die Hard"],
    "Komedi": ["The Hangover", "Superbad", "Step Brothers", "Anchorman", "Bridesmaids"],
    "Dram": ["The Shawshank Redemption", "Forrest Gump", "The Godfather", "Schindler's List", "Fight Club"],
    "Bilim Kurgu": ["Inception", "Interstellar", "The Matrix", "Blade Runner 2049", "Star Wars: Empire Strikes Back"],
    "Korku": ["The Conjuring", "Hereditary", "Get Out", "A Quiet Place", "The Exorcist"],
    "Dizi": ["Breaking Bad", "Stranger Things", "Game of Thrones", "Friends", "The Office"]
}

def film_oneri():
    print("Merhaba! Film/Dizi Öneri Sistemine Hoş Geldiniz!")
    print("Mevcut kategoriler:", ", ".join(veritabani.keys()))
    
    while True:
        kategori = input("\nHangi kategoriden öneri istersiniz? (Çıkmak için 'q'): ").capitalize()
        
        if kategori == 'Q':
            print("Güle güle!")
            break
            
        if kategori in veritabani:
            oneri = random.choice(veritabani[kategori])
            print(f"\n⭐ Önerimiz: {oneri} ⭐\n")
        else:
            print("Üzgünüm, bu kategori bulunamadı. Lütfen listedeki kategorilerden birini seçin.")

# Programı çalıştır
if __name__ == "__main__":
    film_oneri()