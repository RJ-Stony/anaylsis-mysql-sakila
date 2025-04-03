import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

palette = sns.color_palette("Set2")

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='genre', y='rating_count', hue='rating', palette=palette)
plt.title('장르별 등급 카운트 막대 그래프')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

pivot_count = df.pivot(index='genre', columns='rating', values='rating_count')
pivot_count.fillna(0, inplace=True)
pivot_count = pivot_count.loc[pivot_count.sum(axis=1).sort_values(ascending=False).index]
colors = sns.color_palette("Set3", n_colors=pivot_count.shape[1])
pivot_count.plot(kind='bar', stacked=True, figsize=(12, 6), color=colors)
plt.title('장르별 등급 카운트 누적 막대 그래프')
plt.ylabel('등급 카운트')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

genres = df['genre'].unique()
num_genres = len(genres)
cols = 4
rows = (num_genres + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(cols*4, rows*4))
axes = axes.flatten()
for ax, genre in zip(axes, genres):
    data_genre = df[df['genre'] == genre]
    pie_colors = sns.color_palette('Set2', n_colors=len(data_genre))
    ax.pie(data_genre['rating_count'], labels=data_genre['rating'], autopct='%1.1f%%', startangle=140, colors=pie_colors)
    ax.set_title(genre)
for ax in axes[len(genres):]:
    ax.axis('off')
plt.suptitle("장르별 등급 분포 파이차트", fontsize=16)
plt.tight_layout()
plt.show()
