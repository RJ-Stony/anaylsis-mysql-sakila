import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import numpy as np
from PIL import Image
mask = np.array(Image.open("image.jpg"))

for index, row in df.iterrows():
    genre = row['genre']
    text = row['all_descriptions']

    wordcloud = WordCloud(width=800, height=400, 
                          background_color='white', 
                          colormap='Set2',
                          mask=mask).generate(text)
    
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f"장르 워드 클라우드: {genre}")
    plt.axis('off')
    plt.tight_layout()
    plt.show()