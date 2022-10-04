import csv
import matplotlib.pyplot as plt
import folium

f = open("LOCAL_PEOPLE_DONG_202208.csv", encoding="UTF-8") # 파일 오픈
data = csv.reader(f)
next(data)
data = list(data)

lat = [37.530734, 37.587817, 37.613029, 37.532612, 37.537541, 37.550578, 37.597248, 37.523807, 37.524399, 37.514315]
long = [127.028461, 127.001745, 126.974485, 126.990182, 127.005165, 127.081722, 126.992899, 127.026492, 127.050457, 127.062824]
localName = ["압구정동", "혜화동", "평창동", "이태원1동", "한남동", "능동", "성북동", "신사동", "청담동", "삼성1동"]
iconShape = ["star", "heart", "flag", "home", "glass", "cutlery", "tag", "bookmark", "pencil", "fire"]
iconColor = ["lightred", "lightgreen", "blue", "cadetblue", "orange", "lightblue", "green", "purple", "pink", "red"]

# 압구정
o_dong_code = "11680545"
o_population = []
o_time = 0
o_p = 0

# 혜화
h_dong_code = "11110650"
h_population = []
h_time = 0
h_p = 0

# 평창
p_dong_code = "1110560"
p_population = []
p_time = 0
p_p = 0

# 이태원1
e_dong_code = "11170650"
e_population = []
e_time = 0
e_p = 0

# 한남
han_dong_code = "11170685"
han_population = []
han_time = 0
han_p = 0

# 능동
n_dong_code = "11215780"
n_population = []
n_time = 0
n_p = 0

# 성북
sung_dong_code = "11290525"
sung_population = []
sung_time = 0
sung_p = 0

# 신사
sin_dong_code = "11680510"
sin_population = []
sin_time = 0
sin_p = 0

# 청담
chung_dong_code = "11680565"
chung_population = []
chung_time = 0
chung_p = 0

# 삼성1
sam_dong_code = "11680580"
sam_population = []
sam_time = 0
sam_p = 0


x = []

for i in range(24):
    x.append(i)

for i in range(24):
    o_population.append(0)
    h_population.append(0)
    p_population.append(0)
    e_population.append(0)
    han_population.append(0)
    n_population.append(0)
    sung_population.append(0)
    sin_population.append(0)
    chung_population.append(0)
    sam_population.append(0)

for row in data:
    if row[2] == o_dong_code:
        o_time = int(row[1])
        o_p = float(row[3])
        o_population[o_time] += o_p

    if row[2] == h_dong_code:
        h_time = int(row[1])
        h_p = float(row[3])
        h_population[h_time] += h_p

    if row[2] == p_dong_code:
        p_time = int(row[1])
        p_p = float(row[3])
        p_population[p_time] += p_p

    if row[2] == e_dong_code:
        e_time = int(row[1])
        e_p = float(row[3])
        e_population[e_time] += e_p

    if row[2] == han_dong_code:
        han_time = int(row[1])
        han_p = float(row[3])
        han_population[han_time] += han_p

    if row[2] == n_dong_code:
        n_time = int(row[1])
        n_p = float(row[3])
        n_population[n_time] += n_p

    if row[2] == sung_dong_code:
        sung_time = int(row[1])
        sung_p = float(row[3])
        sung_population[sung_time] += sung_p

    if row[2] == sin_dong_code:
        sin_time = int(row[1])
        sin_p = float(row[3])
        sin_population[sin_time] += sin_p

    if row[2] == chung_dong_code:
        chung_time = int(row[1])
        chung_p = float(row[3])
        chung_population[chung_time] += chung_p

    if row[2] == sam_dong_code:
        sam_time = int(row[1])
        sam_p = float(row[3])
        sam_population[sam_time] += sam_p


for i in range(24):
    o_population[i] = o_population[i]/31
    h_population[i] = h_population[i] / 31
    p_population[i] = p_population[i] / 31
    e_population[i] = e_population[i] / 31
    han_population[i] = han_population[i] / 31
    n_population[i] = n_population[i] / 31
    sung_population[i] = sung_population[i] / 31
    sin_population[i] = sin_population[i] / 31
    chung_population[i] = chung_population[i] / 31
    sam_population[i] = sam_population[i] / 31

plt.rc("font", family="NanumGothic")

plt.plot(x, o_population, label="압구정동")
plt.plot(x, h_population, label="혜화동")
plt.plot(x, p_population, label="평창동")
plt.plot(x, e_population, label="이태원1동")
plt.plot(x, han_population, label="한남동")
plt.plot(x, n_population, label="능동")
plt.plot(x, sung_population, label="성북동")
plt.plot(x, sin_population, label="신사동")
plt.plot(x, chung_population, label="청담동")
plt.plot(x, sam_population, label="삼성1동")

plt.title("시간대별 평균 인구")
plt.xlabel("시간대")
plt.ylabel("평균 인구 수")
plt.legend(loc="upper left")
plt.xticks(x)

plt.show()

map_y = folium.Map([lat[0], long[0]], zoom_start=15)

for i in range(10):
    folium.Marker([lat[i], long[i]], tooltip=localName[i], icon=folium.Icon(color=iconColor[i], icon=iconShape[i], prefix="fa")).add_to(map_y)

map_y