
from itertools import islice, takewhile

from uzay_oyunu.akis import (
    fibonacci,
    yakit_gostergesi,
    satirlari_oku,
    ayristir,
    uzun_yolculuklar,
)


def test_fibonacci():
    """İlk Fibonacci değerlerini ve üretecin tek kullanımlılığını test eder."""
    g = fibonacci()
    assert [next(g), next(g), next(g)] == [0, 1, 1]

    assert list(islice(fibonacci(), 12)) == [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    ]

    assert list(takewhile(lambda x: x < 100, fibonacci())) == [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    ]

    g = fibonacci()
    assert list(islice(g, 3)) == [0, 1, 1]
    assert list(islice(g, 3)) == [2, 3, 5]


def test_yakit_gostergesi():
    """Yakıtın sıfıra kadar azaldığını test eder."""
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]


def test_seyir_boruhatti():
    """Seyir kayıtlarının tembel biçimde işlendiğini test eder."""
    satirlar = [
        "dünya -> sirius 12",
        "# yorum",
        "",
        "sirius -> orion 8",
        "orion -> centauri 15",
    ]
    kayitlar = ayristir(satirlar)

    assert sum(y for _, _, y in kayitlar) == 35

    kayitlar = ayristir([
        "dünya -> sirius 12",
        "sirius -> orion 8",
        "orion -> centauri 15",
    ])
    assert [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)] == [
        "sirius", "centauri"
    ]
def test_fibonacci_tek_kullanimlik():
    from itertools import islice
    g = fibonacci()
    assert list(islice(g, 3)) == [0, 1, 1]
    assert list(islice(g, 3)) == [2, 3, 5]


def test_yakit_gecersiz_tuketim():
    import pytest
    with pytest.raises(ValueError):
        list(yakit_gostergesi(100, 0))