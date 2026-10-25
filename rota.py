from functools import lru_cache


def rota_sayaci(baglantilar: dict):
    """Önbellek kullanarak farklı rotaların sayısını hesaplar."""

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """Belirtilen gezegenden tam adım sayısı kadar rota hesaplar."""
        if adim == 0:
            return 1

        return sum(
            rota_sayisi(hedef, adim - 1)
            for hedef in baglantilar.get(gezegen, [])
        )

    return rota_sayisi
