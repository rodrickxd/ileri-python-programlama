"""Uzay oyunu komut kayıt sistemi."""
from functools import wraps


class KomutKayit:
    def __init__(self):
        self.komutlar = {}

    def ekle(self, ad, aciklama=""):
        def dekorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            self.komutlar[ad] = {"fonksiyon": wrapper, "aciklama": aciklama}
            return wrapper
        return dekorator

    def calistir(self, ad, *args, **kwargs):
        if ad not in self.komutlar:
            raise ValueError(f"Bilinmeyen komut: {ad}")
        return self.komutlar[ad]["fonksiyon"](*args, **kwargs)

    def yardim(self):
        return "\n".join(
            f"{ad}: {bilgi['aciklama']}".rstrip(": ")
            for ad, bilgi in self.komutlar.items()
        )


KOMUTLAR = KomutKayit()


@KOMUTLAR.ekle("envanter", "Eşyalarını gösterir")
def envanter():
    return "envanter: boş"


@KOMUTLAR.ekle("harita", "Gidilebilecek gezegenleri gösterir")
def harita():
    return "orion, dünya, kara_delik"


@KOMUTLAR.ekle("yardim", "Komutları listeler")
def yardim():
    return KOMUTLAR.yardim()
