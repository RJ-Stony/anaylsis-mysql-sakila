import pymysql
import pandas as pd

# python mysql에 연결
host = 'localhost'
user = 'root'
password = 'pw'
db_name = 'sakila'

# 접속: pymysql.connect()
# host=접속주소(IP)
# user=아이디
# password=비밀번호
# db=DB이름
# charset=인코딩값(utf8)

conn = pymysql.connect(host=host,
                       user=user,
                       password=password,
                       db=db_name,
                       charset='utf8')

# 커서 생성: query를 실행하는 execute()
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 쿼리 끝에 반드시 ;
query = """
SELECT 
    c.name AS genre,
    AVG(f.length) AS avg_length
FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name;
        """

# query 실행
cursor.execute(query)

# 결과로 반환된 테이블의 모든 행을 가져오기: cursor.fetchall()
result = cursor.fetchall()

# df로 변환
df = pd.DataFrame(result)

# 원하는 데이터를 가져왔으면 DB 연결을 반드시 종료
conn.close()

from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    print('Check your OS system')
    
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
