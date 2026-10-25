import pytest
from uzay_oyunu.decoratorler import sure_olc, say, log_cagri, sinirla, hafiza, yakit_harca
from uzay_oyunu.komutlar import KOMUTLAR


def test_sure_olc_sonucu_korur(capsys):
    @sure_olc
    def topla(a, b):
        return a + b
    assert topla(2, 3) == 5
    assert "çalışma süresi" in capsys.readouterr().out


def test_say():
    @say
    def iki_kat(x):
        return x * 2
    assert iki_kat(3) == 6
    assert iki_kat(4) == 8
    assert iki_kat.cagri_sayisi == 2


def test_log_cagri(capsys):
    @log_cagri
    def selam(ad):
        return f"Merhaba {ad}"
    assert selam("Ada") == "Merhaba Ada"
    out = capsys.readouterr().out
    assert "-> selam('Ada')" in out
    assert "<- selam" in out


def test_sinirla():
    assert yakit_harca(30) == 70
    with pytest.raises(ValueError):
        yakit_harca(150)
    with pytest.raises(ValueError):
        yakit_harca(-1)


def test_komut_kayit():
    assert "envanter" in KOMUTLAR.komutlar
    assert KOMUTLAR.calistir("envanter") == "envanter: boş"


def test_hafiza():
    sayac = {"n": 0}
    @hafiza()
    def kare(x):
        sayac["n"] += 1
        return x * x
    assert kare(4) == 16
    assert kare(4) == 16
    assert sayac["n"] == 1
