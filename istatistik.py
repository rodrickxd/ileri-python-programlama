
from functools import partial, reduce
from main import galaksi, travel


def istatistikleri_hesapla() -> dict:
    """Galaksi istatistiklerini iki farklı yöntemle hesaplar."""
    baglantilar = galaksi["baglantilar"]
    gezegenler = list(baglantilar)

    buyuk_harfler = list(map(str.upper, gezegenler))
    baglantili = list(filter(lambda g: len(baglantilar[g]) >= 2, gezegenler))
    toplam = reduce(lambda a, g: a + len(baglantilar[g]), gezegenler, 0)

    # Liste ve sum kullanımı daha okunaklıdır.
    buyuk_harfler2 = [g.upper() for g in gezegenler]
    baglantili2 = [g for g in gezegenler if len(baglantilar[g]) >= 2]
    toplam2 = sum(len(baglantilar[g]) for g in gezegenler)

    return {
        "map_filter_reduce": (buyuk_harfler, baglantili, toplam),
        "liste_sum": (buyuk_harfler2, baglantili2, toplam2),
    }


hizli_yolculuk = partial(travel, hiz=3)


if __name__ == "__main__":
    """İki yöntemin sonuçlarını ve hızlı yolculuğu gösterir."""
    print(istatistikleri_hesapla())
    print(hizli_yolculuk("sirius"))
