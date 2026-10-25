
"""Uzay oyunu için üreteçler ve veri akışı."""


def fibonacci():
    """Sonsuz Fibonacci sayılarını üretir."""
    onceki, simdiki = 0, 1
    while True:
        yield onceki
        onceki, simdiki = simdiki, onceki + simdiki


def yakit_gostergesi(yakit: int, tuketim: int):
    """Her çağrıda yakıtı azaltır ve kalan miktarı üretir."""
    if tuketim <= 0:
        raise ValueError("Tüketim sıfırdan büyük olmalıdır.")

    while yakit > 0:
        yakit = max(0, yakit - tuketim)
        yield yakit


def satirlari_oku(yol: str):
    """Boş ve yorum satırlarını atlayarak dosyayı satır satır okur."""
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.strip()
            if satir and not satir.startswith("#"):
                yield satir


def ayristir(satirlar):
    """Seyir satırlarını kaynak, hedef ve yakıt demetlerine dönüştürür."""
    for satir in satirlar:
        satir = satir.strip()

        if not satir or satir.startswith("#"):
            continue

        kaynak, ok, kalan = satir.partition("->")
        if not ok:
            raise ValueError(f"Gecersiz seyir satiri: {satir}")

        hedef, yakit = kalan.split()
        yield kaynak.strip(), hedef.strip(), int(yakit)

def uzun_yolculuklar(kayitlar, esik: int):
    """Yakıtı eşikten büyük olan yolculukları üretir."""
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield kaynak, hedef, yakit
            