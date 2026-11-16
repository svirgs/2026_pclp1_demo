citiri = {
    "II-1": [("08:00", 19.5), ("10:00", 22.00)],
    "II-3": [("08:00", 20.5), ("10:00", 16.00)],
}

reci = set()
for sala, lst in citiri.items():
    temps = [t for _, t in lst]
    medie = round(sum(temps) / len(temps), 2)
    print(sala, lst[-1], medie)
    if min(temps) < 18:
        reci.add(sala)
print(reci)
