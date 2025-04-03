# 🎬 Sakila MySQL Database Analysis

Sakila 샘플 DB를 활용해 영화 대여점 데이터를 시각화하고,  
Python을 통해 MySQL과 연동하여 쿼리부터 분석까지 자동화하는 프로젝트입니다.

---

## 📁 프로젝트 구조

```
anaylsis-mysql-sakila-main/
├── mysql_test.py      # ✅ MySQL 접속 및 데이터 추출
├── barchart.py        # ✅ 장르별 대여 수 등 막대 차트 시각화
├── wordcloud.py       # ✅ 배우 이름/키워드 기반 워드클라우드 생성
├── image.jpg          # 분석 결과 예시 이미지
├── README.md
└── .gitignore
```

---

## 🔌 MySQL 연동

- `mysql_test.py`를 통해 MySQL Sakila DB에 접속하고, 원하는 쿼리 실행 가능
- 예: 장르별 대여 수, 고객별 대여 내역, 배우별 출연 영화 수 등

```python
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='yourpassword', db='sakila')
cursor = conn.cursor()
cursor.execute("SELECT * FROM actor LIMIT 10")
```

---

## 📊 시각화

### 1. `barchart.py`

- matplotlib을 활용한 장르별 영화 대여 건수 시각화
- MySQL에서 추출한 데이터를 pandas DataFrame으로 변환 후 그래프 생성

### 2. `wordcloud.py`

- 배우 이름 또는 영화 키워드를 활용한 워드클라우드 생성
- 빈도 기반 시각화로 데이터의 트렌드/흐름 파악 가능

---

## 🛠 사용 기술

- Python 3.12+
- `pymysql`, `pandas`, `matplotlib`, `wordcloud`
- MySQL 8.x (또는 Sakila DB가 세팅된 환경)

---

## 💡 확장 아이디어

- 고객별 분석: 총 대여 금액, 충성도 랭킹 등
- 월별 트렌드 분석: 시즌별 인기 장르 파악
- 웹 앱으로 시각화 결과 공유 (Flask, Streamlit 등 활용 가능)

---

## ✅ 참고 사항

- 사전에 [Sakila 샘플 DB](https://dev.mysql.com/doc/sakila/en/)가 설치되어 있어야 함
- MySQL 접속 정보는 `mysql_test.py` 내에서 환경에 맞게 수정 필요
