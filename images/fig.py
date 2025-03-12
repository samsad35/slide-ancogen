import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Appliquer un style moderne
plt.style.use("seaborn-v0_8-darkgrid")

# Données
data = {
    "Product": ["Noisy", "Noisy", "Noisy", "Ours", "Ours", "Ours",
                "Conv-TasNet", "Conv-TasNet", "Conv-TasNet", "DPTNet", "DPTNet", "DPTNet"],
    "Segment": ["N-MOS", "WER", "BAK", "N-MOS", "WER", "BAK",
                "N-MOS", "WER", "BAK", "N-MOS", "WER", "BAK"],
    "Amount_sold": [2.62, 2.56, 2.97, 4.24, 4.32, 3.81,
                    4.12, 4.30, 3.78, 4.12, 4.30, 3.78]
}

df = pd.DataFrame(data)

# Pivot pour structurer les données
pivot_df = df.pivot(index="Segment", columns="Product", values="Amount_sold")

# Réorganiser les colonnes pour afficher "Noisy" en dernier
ordered_columns = [col for col in pivot_df.columns if col != "Noisy"] + ["Noisy"]
pivot_df = pivot_df[ordered_columns]

# Palette de couleurs moderne (Noisy en gris foncé pour le différencier)
colors = sns.color_palette("muted", n_colors=len(pivot_df.columns) - 1) + ["#4A4A4A"]

# Créer un graphique avec des couleurs modernes
ax = pivot_df.plot.bar(grid=True, figsize=(7, 5), color=colors, alpha=0.85, edgecolor="black")

# Personnalisation
plt.legend(frameon=True, fontsize=10)
ax.set_xlabel('')
ax.set_ylabel('Metrics', fontsize=12)
ax.set_title('Performance Metrics Comparison', fontsize=14, fontweight="bold")

# Supprimer les bordures inutiles pour un look épuré
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# Afficher le graphique
plt.show()
