from colorthief import ColorThief
import matplotlib.pyplot as plt

color_thief = ColorThief("./img/KR-6277840301/0.png")

dominant_color = color_thief.get_color(quality=1)

palette = color_thief.get_palette(color_count=3)

plt.imshow([[palette[i] for i in range(4)]])
plt.show()

print(dominant_color)

print(palette)