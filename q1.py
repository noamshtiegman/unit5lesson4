
import pandas as pd

import matplotlib.pyplot as plt





tables = pd.read_html("https://en.wikipedia.org/wiki/Minnesota", match = "historical Population")

table = tables[0]

print(table["Census"])
print(table["Pop."])
df = table[["Census", "Pop."]]
df = df.iloc[0:-2].astype("int")

df.plot(x = "census", y = "pop.")
plt.show()