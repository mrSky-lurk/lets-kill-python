import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Server and Client boxes
client_box = mpatches.FancyBboxPatch((0.5, 2.5), 2, 2, boxstyle="round,pad=0.1", fc="lightblue", ec="black", lw=1.5)
server_box = mpatches.FancyBboxPatch((7, 2.5), 2, 2, boxstyle="round,pad=0.1", fc="lightgreen", ec="black", lw=1.5)
ax.add_patch(client_box)
ax.add_patch(server_box)
ax.text(1.5, 3.67, "Client\n(Browser)", ha="center", va="center", fontsize=11, fontweight="bold")
ax.text(8, 3.67, "Server\n(Website)", ha="center", va="center", fontsize=11, fontweight="bold")

# Features with arrows
features = [
    ("Caching\n(Faster loads)", (2.5, 4.5), (7, 4.5)),
    ("Relax Origin\n(CORS)", (2.5, 4), (7, 4)),
    ("Authentication\n(Login)", (2.5, 3.5), (7, 3.5)),
    ("Proxy/Tunneling\n(Network path)", (2.5, 3), (7, 3)),
    ("Sessions\n(Shopping cart)", (2.5, 2.5), (7, 2.5)),
]

for text, start, end in features:
    ax.annotate(
        "", xy=end, xycoords='data', xytext=start, textcoords='data',
        arrowprops=dict(arrowstyle="->", lw=1.5, color="black")
    )
    ax.text((start[0]+end[0])/2, start[1], text, ha="center", va="center", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="black", lw=1))

# Title
ax.set_title("HTTP Features in Client–Server Communication", fontsize=14, fontweight="bold")

plt.show()
