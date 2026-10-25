# İleri Python Programlama – Hafta 5 Lab: Dekoratörler

Bu proje Hafta 4 projesinin devamıdır.

## Eklenen dosyalar
- `uzay_oyunu/decoratorler.py`: `sure_olc`, `say`, `log_cagri`, `sinirla` ve bonus `hafiza` dekoratörleri.
- `uzay_oyunu/komutlar.py`: dekoratörle komut kaydı ve komut çalıştırma sistemi.
- `tests/test_decoratorler.py`: yeni özelliklerin testleri.

## Testleri çalıştırma
Proje klasöründe terminal açıp çalıştırın:

```bash
python -m pytest -q
```

Son doğrulamada 11 test geçti.

## Örnekler
```python
from uzay_oyunu.decoratorler import sure_olc, say, log_cagri, sinirla, hafiza

@sure_olc
def hesapla(n):
    return n * n

@sinirla(0, 100)
def yakit_harca(miktar):
    return 100 - miktar
```
