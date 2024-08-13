import math

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Hata: Sifira bölme yapilmaz."
    return a / b

def karekok(a):
    if a < 0:
        return "Hata: Negatif sayinin karekökü alinamaz."
    return math.sqrt(a)

def us_alma(a, b):
    return a ** b

def mod_alma(a, b):
    return a % b

# Hesap makinesi fonksiyonu
def hesap_makinesi():
    gecmis = []
    while True:
        print("\nLütfen bir işlem seçin:")
        print("1. Toplama")
        print("2. Çikarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Karekök")
        print("6. Üs alma")
        print("7. Mod alma")
        print("8. Geçmişi göster")
        print("9. Çikiş")

        secim = input("Seçiminiz (1/2/3/4/5/6/7/8/9): ")

        if secim == '9':
            print("Hesap makinesinden çikiliyor")
            break
        elif secim in ['1', '2', '3', '4', '6', '7']:
            sayi1 = float(input("Birinci sayiyi girin: "))
            sayi2 = float(input("İkinci sayiyi girin: "))

            if secim == '1':
                sonuc = toplama(sayi1, sayi2)
                print(f"Sonuç: {sonuc}")
            elif secim == '2':
                sonuc = cikarma(sayi1, sayi2)
                print(f"Sonuç: {sonuc}")
            elif secim == '3':
                sonuc = carpma(sayi1, sayi2)
                print(f"Sonuç: {sonuc}")
            elif secim == '4':
                sonuc = bolme(sayi1, sayi2)
                print(f"Sonuç: {sonuc}")
            elif secim == '6':
                sonuc = us_alma(sayi1, sayi2)
                print(f"Sonuç: {sonuc}")
            elif secim == '7':
                sonuc = mod_alma(sayi1, sayi2)
                print(f"Sonuç: {sonuc}")

            gecmis.append(f"{sayi1} ve {sayi2} ile yapilan işlem sonucu: {sonuc}")

        elif secim == '5':
            sayi = float(input("Bir sayi girin: "))
            sonuc = karekok(sayi)
            print(f"Sonuç: {sonuc}")
            gecmis.append(f"{sayi} sayisinin karekökü: {sonuc}")

        elif secim == '8':
            print("\nGeçmiş:")
            for item in gecmis:
                print(item)
            if not gecmis:
                print("Henüz gecmiste bir işlem yok.")

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


hesap_makinesi()