import time
import sys

def geri_sayim(dakika, mesaj):
    """Verilen dakika boyunca terminalde canlı geri sayım yapar."""
    toplam_saniye = dakika * 60
    
    print(f"\n{mesaj}")
    print("-" * 30)
    
    while toplam_saniye > 0:
        # Saniyeyi dakika ve saniyeye çevir (Örn: 125 saniye -> 2 dk 5 sn)
        dk, sn = divmod(toplam_saniye, 60)
        
        # Süreyi 00:00 formatında hazırla
        zaman_formati = f"{dk:02d}:{sn:02d}"
        
        # \r (carriage return) imleci satırın başına alır, böylece aynı satırı güncelleriz
        sys.stdout.write(f"\r⏳ Kalan Süre: {zaman_formati}")
        sys.stdout.flush() # Terminali anında güncellemeye zorlar
        
        time.sleep(1) # 1 saniye bekle
        toplam_saniye -= 1
        
    # Süre bitince bir uyarı sesi (beep) çıkar (Bazı bilgisayarlarda çalışır)
    print("\a") 

def main():
    print("🍅 PYTHON POMODORO SAYACINA HOŞ GELDİN 🍅")
    
    while True:
        print("\n" + "="*40)
        print("1. Klasik Pomodoro Başlat (25dk Çalışma + 5dk Mola)")
        print("2. Özel Süre Belirle")
        print("3. Çıkış")
        
        secim = input("\nNe yapmak istersin? (1/2/3): ")
        
        if secim == '1':
            calisma_suresi = 25
            mola_suresi = 5
            
            # Çalışma Sayacı
            geri_sayim(calisma_suresi, "🚀 ODAKLANMA ZAMANI! Telefonları sessize alıyoruz.")
            print("\n\n🎉 HARİKA İŞ ÇIKARDIN! Çalışma süresi bitti.")
            
            # Mola Sayacı
            geri_sayim(mola_suresi, "☕ MOLA ZAMANI! Kalk, esne ve bir bardak su iç.")
            print("\n\n⏰ Mola bitti! Yeni bir seansa hazır mısın?")
            
        elif secim == '2':
            try:
                calisma_suresi = int(input("Kaç dakika çalışmak istersin? : "))
                mola_suresi = int(input("Kaç dakika mola istersin? : "))
                
                geri_sayim(calisma_suresi, f"🚀 {calisma_suresi} DAKİKALIK ODAKLANMA BAŞLADI!")
                print("\n\n🎉 SÜRE BİTTİ!")
                
                geri_sayim(mola_suresi, f"☕ {mola_suresi} DAKİKALIK MOLA BAŞLADI!")
                print("\n\n⏰ Mola bitti!")
            except ValueError:
                print("❌ Lütfen sadece sayı gir!")
                
        elif secim == '3':
            print("Verimli çalışmalar dilerim! Görüşmek üzere. 👋")
            break
        else:
            print("❌ Hatalı seçim, lütfen tekrar dene.")

if __name__ == "__main__":
    main()
