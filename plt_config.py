import matplotlib
import matplotlib.pyplot as plt

try:
    matplotlib.use("Qt5Agg")
except:
    pass
params = {
    "font.family": "Times New Roman",
    "figure.figsize": (8, 6),
    "figure.dpi": 300,
    "font.size": 28,
    "lines.linewidth": 3,
    "legend.fontsize": 18
}
plt.rcParams.update(params)

print('Customized matplotlib configuration loaded.')
