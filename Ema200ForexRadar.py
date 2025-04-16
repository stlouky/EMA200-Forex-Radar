import requests
import pandas as pd
from termcolor import colored

API_KEY = "SXk7s5rdIwA2kgOi67A6Cwg60duLPb5r"  # ← vlož si svůj API klíč

symbols = [
    "EURAUD", "USDJPY", "EURUSD", "GBPUSD", "AUDUSD", "NZDUSD",
    "USDCAD", "USDCHF", "EURJPY", "EURGBP", "GBPJPY", "GBPNZD",
    "EURCAD", "CADJPY", "NZDCHF", "CHFJPY"
]

results = []

for symbol in symbols:
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={API_KEY}&serietype=line"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Nepodařilo se načíst data pro {symbol}")
        continue

    data = response.json()
    if "historical" not in data or len(data["historical"]) < 200:
        print(f"Nedostatek dat u {symbol}")
        continue

    prices = [entry["close"] for entry in data["historical"][:200]]
    current_price = prices[0]
    ema200 = sum(prices) / len(prices)
    diff_pips = (current_price - ema200) * (100 if "JPY" in symbol else 10000)
    diff_percent = ((current_price - ema200) / ema200) * 100

    results.append({
        "Měnový pár": symbol,
        "Cena": round(current_price, 5),
        "EMA200": round(ema200, 5),
        "Rozdíl (pipy)": round(diff_pips, 2),
        "Rozdíl (%)": round(diff_percent, 2)
    })

# Vytvoření tabulky
radar = pd.DataFrame(results)
radar = radar.sort_values(by="Rozdíl (%)", ascending=False)

# Výpis tabulky
print("\n📊 Přehled měnových párů a jejich odchylek od EMA200:\n")
header = f"{'Měnový pár':<10} {'Cena':>10} {'EMA200':>10} {'Rozdíl (pipy)':>18} {'Rozdíl (%)':>15}"
print(header)
print("-" * len(header))

for _, row in radar.iterrows():
    line = f"{row['Měnový pár']:<10} {row['Cena']:>10.5f} {row['EMA200']:>10.5f} {row['Rozdíl (pipy)']:>18.2f} {row['Rozdíl (%)']:>15.2f}"
    color = "green" if row["Rozdíl (%)"] >= 0 else "red"
    print(colored(line, color))

# 🧭 Interpretace rozdílů od EMA200 (procenta)
print("\n🧭 Interpretace rozdílů od EMA200:")
print("🟢 nad +5 %          → Překoupený trh – vysoké riziko korekce směrem dolů")
print("🟢 +2 % až +5 %      → Růstový trend – silný moment, ale sledovat zpomalení")
print("⚪  0 % až +2 %      → Mírný růst – v normálním trendovém rozpětí")
print("⚪ –2 % až 0 %       → Mírný pokles – v normálním trendovém rozpětí")
print("🔴 –5 % až –2 %      → Klesající trh – potenciál pro návrat nebo pokračování")
print("🔴 pod –5 %          → Přeprodaný trh – vysoké riziko korekce směrem nahoru")
