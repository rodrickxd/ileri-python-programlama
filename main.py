from uzay_oyunu.akis import yakit_gostergesi
"""Uzay oyununun temel galaksi verileri."""

galaksi = {
    "baglantilar": {
        "dünya": ["centauri", "sirius", "orion"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion", "kara_delik"],
        "orion": ["dünya", "centauri", "sirius"],
        "kara_delik": ["sirius"],
    },
    "yakit": 100,
}


def travel(gezegen: str, hiz: int = 1) -> str:
    """Belirtilen gezegene yolculuk mesajı döndürür."""
    if gezegen not in galaksi["baglantilar"]:
        return f"{gezegen} galakside bulunamadı."

    if hiz < 1:
        return "Hız en az 1 olmalıdır."

    return f"{gezegen} gezegenine {hiz} hızında yolculuk yapılıyor."


if __name__ == "__main__":
    print("Uzay oyunu başlatıldı!")
    yakit_gostergesi_oyuncu = yakit_gostergesi(galaksi["yakit"], 5)
    print(travel("sirius"))

