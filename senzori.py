"""senzori.py — citiri simulate de la senzorii unei clădiri."""

import random
from datetime import datetime


def citeste_senzor(medie: float = 22.0, abatere: float = 3.0) -> tuple[float, float]:
    """Simulează o citire. Returnează (temperatura în °C, umiditatea în %)."""
    temp = round(random.gauss(medie, abatere), 1)
    umid = round(random.uniform(30, 70), 1)
    return temp, umid


def clasifica(temp: float, prag_rece: float = 18.0, prag_cald: float = 26.0) -> str:
    """Returnează RECE, CONFORT sau CALD."""
    if temp < prag_rece:
        return "RECE"
    if temp > prag_cald:
        return "CALD"
    return "CONFORT"


def main() -> None:
    random.seed(2)  # aceleași valori la fiecare rulare
    for _ in range(6):
        t, u = citeste_senzor()
        ora = datetime.now().strftime("%H:%M:%S")
        print(f"{ora}  A101  {t:5.1f} °C  {u:4.1f} %  {clasifica(t)}")


assert clasifica(17.9) == "RECE"
assert clasifica(18) == "CONFORT"
assert clasifica(26.1, prag_cald=27) == "CONFORT"

if __name__ == "__main__":
    main()
