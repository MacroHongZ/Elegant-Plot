import matplotlib.pyplot as plt
import matplotlib
import numpy as np

vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

matplotlib.rcParams['font.family'] = 'serif'
fig = plt.figure(dpi=300)
ax = fig.subplots()

# custom your colors
cmap_straight = matplotlib.colors.LinearSegmentedColormap.from_list(
    "mycolor", [[0.95, 0.65, 0.58], [0.65, 0.95, 0.58]])

im = ax.imshow(harvest, cmap=cmap_straight)
colorbar = fig.colorbar(im, ax=ax)
colorbar.outline.set_visible(False)

ax.set_xticks(np.arange(len(farmers)), labels=farmers)
ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

ax.set_xticks(np.arange(harvest.shape[1] + 1) - .5, minor=True)
ax.set_yticks(np.arange(harvest.shape[0] + 1) - .5, minor=True)
ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
ax.tick_params(which="minor", bottom=False, left=False)

ax.spines[:].set_visible(False)

for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Title", pad=16, fontdict={'fontsize': 24})
fig.tight_layout()
plt.savefig('heatmap.pdf')
plt.show()

