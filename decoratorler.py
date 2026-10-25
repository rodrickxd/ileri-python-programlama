"""Hafta 5: dekoratör örnekleri."""
from functools import wraps
from time import perf_counter


def sure_olc(func):
    """Fonksiyonun çalışma süresini ölçer ve sonucunu değiştirmez."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        baslangic = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"{func.__name__} çalışma süresi: {perf_counter() - baslangic:.6f} sn")
    return wrapper


def say(func):
    """Fonksiyon çağrılarını sayar."""
    sayac = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal sayac
        sayac += 1
        wrapper.cagri_sayisi = sayac
        return func(*args, **kwargs)

    wrapper.cagri_sayisi = 0
    return wrapper


def log_cagri(func):
    """Çağrı argümanlarını ve dönüş değerini yazdırır."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        argumanlar = [repr(x) for x in args]
        argumanlar.extend(f"{k}={v!r}" for k, v in kwargs.items())
        print(f"-> {func.__name__}({', '.join(argumanlar)})")
        sonuc = func(*args, **kwargs)
        print(f"<- {func.__name__} = {sonuc!r}")
        return sonuc
    return wrapper


def sinirla(alt, ust):
    """İlk sayısal argümanın belirtilen aralıkta olmasını zorunlu kılar."""
    if alt > ust:
        raise ValueError("alt, ust değerinden büyük olamaz")

    def dekorator(func):
        @wraps(func)
        def wrapper(deger, *args, **kwargs):
            if not alt <= deger <= ust:
                raise ValueError(f"{func.__name__}: {deger} değeri {alt}-{ust} aralığında değil")
            return func(deger, *args, **kwargs)
        return wrapper
    return dekorator


def hafiza(maxsize=None):
    """Argümanlara göre sonuçları saklayan basit önbellek dekoratörü."""
    def dekorator(func):
        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            anahtar = (args, tuple(sorted(kwargs.items())))
            if anahtar in cache:
                return cache[anahtar]
            sonuc = func(*args, **kwargs)
            if maxsize is None or len(cache) < maxsize:
                cache[anahtar] = sonuc
            return sonuc

        wrapper.cache = cache
        return wrapper
    return dekorator


@sinirla(0, 100)
def yakit_harca(miktar):
    """Belirtilen miktarda yakıt harcar."""
    return 100 - miktar
