# Optik Okuma OMR (Optical Mark Reader) Python Projesi

Bu proje, Python kullanarak optik işaretleme tanıma (OMR) işlemleri gerçekleştirmek için tasarlanmıştır. Çeşitli optik formları tarayıp, işaretlenmiş yanıtları otomatik olarak algılayarak verileri analiz eder.

## Kurulum

Bu projeyi kullanmadan önce, aşağıdaki Python kütüphanelerinin yüklenmesi gerekmektedir:
```
pip install pillow
pip install pytesseract
pip install pandas
```
## Kullanım

Projeyi kullanmak için, aşağıdaki adımları izleyin:

1. Projeyi klonlayın veya indirin.
2. Terminal veya komut satırından proje dizinine gidin.
3. Eğer aynı optik form için denemek isterseniz `taramalar` klasöründen optik formu indirin.
4. `python optik_okuma_scripti.py` komutunu çalıştırarak optik okuma işlemini başlatın.
5. İşlenen veriler, belirtilen çıktı formatında kaydedilecektir.

## Özellikler

- Çoklu format desteği: Projede farklı optik form türleri için destek bulunmamaktadır. Farklı optikler için tanımlama yapınız.
- Hızlı ve doğru veri işleme: Optik işaretlerin hızlı ve doğru bir şekilde algılanması sağlanır.
- Kolay entegrasyon ve genişletilebilirlik: Proje, diğer sistemlerle entegre edilmeye uygun yapıda tasarlanmıştır.

  ## Katkıda Bulunma

Projeye katkıda bulunmak isteyenler için:

1. Projeyi forklayın.
2. Feature branch'ı oluşturun (`git checkout -b feature/YeniOzellik`).
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellikler eklendi'`).
4. Branch'ı push edin (`git push origin feature/YeniOzellik`).
5. Yeni bir Pull Request oluşturun.


