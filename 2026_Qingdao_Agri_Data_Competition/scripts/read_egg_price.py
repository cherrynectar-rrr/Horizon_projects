import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/egg_price_sample.csv")
print(data)

plt.plot(data["date"], data["price"])
plt.show()