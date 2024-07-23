import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib


df = pd.read_csv("data/cases_cumulative_daily.csv",encoding="utf-8")

df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(9, 4))

plt.plot(df["Date"], df["ALL"],label="ALL")
plt.plot(df["Date"], df["Hokkaido"],label="Hokkaido")
plt.plot(df["Date"], df["Gifu"],label="Gifu")
plt.plot(df["Date"], df["Okinawa"],label="Okinawa")

plt.title("合計・北海道・岐阜・沖縄-コロナ感染者数")
plt.xlabel("日付")
plt.ylabel("感染者数")

plt.grid(True)
plt.xticks(rotation=45)

plt.legend()
plt.show()
