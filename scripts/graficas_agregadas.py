"""Recrea las gráficas H1/H2 desde CSV agregados; no recalcula inferencia muestral."""
from pathlib import Path
import csv
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datos"
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)

def rows(filename):
    with (DATA / filename).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def h1():
    items = rows("h1_resumen_ponderado.csv")
    y = [i["grupo"] for i in items]
    x = [float(i["prevalencia"]) for i in items]
    fig, ax = plt.subplots(figsize=(9.5, 4.3))
    bars = ax.barh(y, x, color=["#1476ab", "#27a8b8"], height=.45)
    ax.invert_yaxis()
    ax.set_xlim(0, 55)
    ax.set_xlabel("Antecedentes de ideación alguna vez en la vida (%)")
    ax.set_title("Jóvenes LGBT+ de 15–24 años · ENDISEG 2021", loc="left")
    for bar, v in zip(bars, x):
        ax.text(v + 1, bar.get_y() + bar.get_height()/2, f"{v:.2f}%", va="center")
    ax.spines[["top","right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT / "h1_comparacion.png", dpi=170)
    plt.close(fig)

def h2():
    items = rows("h2_resumen_ponderado.csv")
    x = [int(i["tipos"]) for i in items]
    y = [float(i["prevalencia"]) for i in items]
    lo = [v-float(i["ic95_inf"]) for v,i in zip(y,items)]
    hi = [float(i["ic95_sup"])-v for v,i in zip(y,items)]
    fig, ax = plt.subplots(figsize=(9.5, 4.6))
    ax.bar(x, y, color="#27a8b8")
    ax.errorbar(x, y, yerr=[lo,hi], fmt="none", ecolor="#092f46", capsize=4)
    ax.set_xticks(x)
    ax.set_xlabel("Número de tipos distintos de victimización")
    ax.set_ylabel("Antecedentes de ideación (%)")
    ax.set_ylim(0, 102)
    ax.set_title("Heterogeneidad entre categorías; no causalidad", loc="left")
    fig.tight_layout()
    fig.savefig(OUT / "h2_categorias.png", dpi=170)
    plt.close(fig)

if __name__ == "__main__":
    h1()
    h2()
    print("Gráficas recreadas desde resultados agregados.")
