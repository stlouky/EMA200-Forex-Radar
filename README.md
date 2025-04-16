# EMA200 Forex Radar

Nástroj v Pythonu pro vyhledávání největších odchylek forexových měnových párů od klouzavého průměru EMA200. Slouží jako pomůcka pro mean reversion obchodní strategii (obchodování návratu k průměru).

## Funkce
- Zpracování aktuálních dat pro major a minor forex páry
- Spočítá EMA200 z denních časových řad (200 svíček)
- Seřazení párů podle odchylky v % od EMA200
- Barevné rozlišení (zeleně = nad EMA, červeně = pod EMA)
- Textová interpretace podle velikosti odchylky

## Ukázka tabulky
```
Měnový pár       Cena     EMA200      Rozdíl (pipy)      Rozdíl (%)
-------------------------------------------------------------------
EURAUD        1.78725    1.66225            1250.04            7.52
EURUSD        1.13421    1.07503             591.78            5.50
...
```

## Interpretace rozdílů od EMA200
| Rozdíl (%)        | Význam |
|--------------------|---------|
| nad +5 %           | 🟢  Překoupený trh – vysoké riziko korekce dolů |
| +2 % až +5 %       | 🟢  Růstový trend – silný moment |
| 0 % až +2 %        | ⚪  Mírný růst – normální trend |
| –2 % až 0 %        | ⚪  Mírný pokles – normální trend |
| –5 % až –2 %       | 🔴  Klesající trh – sledovat možný obrat |
| pod –5 %           | 🔴  Přeprodaný trh – vysoké riziko korekce nahoru |

## Instalace
1. Klonuj repozitář:
```bash
git clone https://github.com/uzivatel/ema200-forex-radar.git
cd ema200-forex-radar
```

2. Vytvoř virtuální prostředí:
```bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

3. Spusť radar:
```bash
python3 radar.py
```

## Nastavení API klíče
Zaregistruj se zdarma na [Financial Modeling Prep](https://site.financialmodelingprep.com/) a zkopíruj si API klíč. Uprav ho v souboru `radar.py`:
```python
API_KEY = "TVůj_API_klíč"
```

## Požadavky
- Python 3.8+
- Knihovny: `requests`, `pandas`, `colorama`

## Autor
Projekt vznikl jako praktická pomůcka pro sledování mean reversion obchodní strategie na Forexu.

