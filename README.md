# 🍅 Python Pomodoro Odaklanma Sayacı (Terminal-Based Pomodoro Timer)

Bu proje, terminal üzerinden çalışan, canlı geri sayım özelliğine sahip minimalist bir Pomodoro odaklanma sayacıdır. Ders çalışırken, kod yazarken veya herhangi bir işe odaklanırken zaman yönetiminizi en üst seviyeye çıkarmak için tasarlanmıştır.

## 🚀 Özellikler

* **Canlı Geri Sayım:** Terminal ekranını satır satır doldurmak yerine `\r` (carriage return) kullanılarak aynı satır üzerinde dinamik ve temiz bir geri sayım animasyonu sunar.
* **Klasik Pomodoro Modu:** Tek tuşla bilimsel olarak kanıtlanmış 25 dakika odaklanma + 5 dakika mola döngüsünü başlatır.
* **Özelleştirilebilir Süre:** Çalışma ve mola sürelerini kendi çalışma stilinize göre (örneğin 50 dk çalışma / 10 dk mola) esnek bir şekilde belirleyebilirsiniz.
* **Sesli Bildirim:** Süre bittiğinde terminal üzerinden basit bir uyarı sesi (beep) vererek sizi uyarır.

## 🛠️ Kurulum ve Kullanım

Bu proje tamamen saf Python ile yazılmıştır ve ekstra hiçbir kütüphane kurulumu (pip install) gerektirmez. `time` ve `sys` gibi Python'un gömülü modüllerini kullanır.

1. Projeyi bilgisayarınıza indirin (clone).
2. Terminali veya komut satırını açın.
3. Proje dizinine gidin ve dosyayı çalıştırın:
   ```bash
   python main.py
