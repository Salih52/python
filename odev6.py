import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


xCordinat = np.random.randint(0, 1000, 1000)
yCordinat = np.random.randint(0, 1000, 1000)

data = {'x': xCordinat, 'y': yCordinat}
df = pd.DataFrame(data)


df.to_excel('kordinatlar.xlsx', index=False)

df = pd.read_excel('kordinatlar.xlsx')

xCordinat = df['x'].values
yCordinat = df['y'].values


bolmeSayisi = 100
colors = list(mcolors.CSS4_COLORS.values())


plt.figure(figsize=(10, 10))
plt.scatter(xCordinat, yCordinat, c='black', s=10)


for i in range(0, 1000, bolmeSayisi):
    for j in range(0, 1000, bolmeSayisi):
        rect = plt.Rectangle((i, j), bolmeSayisi, bolmeSayisi, facecolor='none')
        plt.gca().add_patch(rect)

        mask = (xCordinat >= i) & (xCordinat < i + bolmeSayisi) & (yCordinat >= j) & (yCordinat < j + bolmeSayisi)
        plt.scatter(xCordinat[mask], yCordinat[mask], color=np.random.choice(colors), s=10)

plt.xlim(0, 1000)
plt.ylim(0, 1000)
plt.xlabel('X Kordinatlar')
plt.ylabel('Y Kordinatlar')
plt.title('Python Ödev 6')
plt.grid(True)
plt.show()
