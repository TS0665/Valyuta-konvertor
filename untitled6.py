# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16moBUY-oNGVnNkh8x08QH4OYWLlzmyEb
"""

!pip install requests

import requests
def get_exchange_rate():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        return data['rates']['UZS']
    except Exception as e:
        print("Kursni olishda xatolik yuz berdi:", e)
        return None

print("Valyuta konvertoriga xush kelibsiz!")
print("1. USD -> UZS")
print("2. UZS -> USD")
usd_to_uzs = get_exchange_rate()
if usd_to_uzs:
    print(f"Hozirgi valyuta kursi: 1 USD = {usd_to_uzs} UZS")
else:
    print("Valyuta kursi avtomatik olingani yo'q. Iltimos, kursni qo'lda kiriting.")
    usd_to_uzs = float(input("Valyuta kursini kiriting (USD -> UZS): "))

# Foydalanuvchi tanlovi
choice = int(input("Konvertatsiya turi (1 yoki 2): "))

if choice == 1:
    usd = float(input("Dollar miqdorini kiriting: "))
    uzs = usd * usd_to_uzs
    print(f"{usd} USD = {uzs:.2f} UZS")
elif choice == 2:
    uzs = float(input("So'm miqdorini kiriting: "))
    usd = uzs / usd_to_uzs
    print(f"{uzs} UZS = {usd:.2f} USD")
else:
    print("Noto'g'ri tanlov! Iltimos, 1 yoki 2ni tanlang.")