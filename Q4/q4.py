import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import csv

def solve():
    # 폰트가 설치되어 있는지 확인해주세요!
    font_path = "C:/Windows/Fonts/batang.ttc"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font, size=9)
    # file open
    f = open('.card.csv')
    d = csv.reader(f)
    next(d)
    next(d)
    
    data = [[], [], []]
    # [0] line [1] id [2] station [3] 7-8 in [4] 7-8 out [5] 8-9 in [6] 8-9 out
    for row in d:
        flag = 1
        for i in range(3, 7):
            if(row[i] == ""):
                flag = 0
                break
            else:
                row[i] = int(row[i])
        # no missing data
        if(flag == 1):
            rsum = row[3] + row[5]
            qsum = row[4] + row[6]
            rqsum = rsum + qsum
            data[0].append([rsum, row[0] + "\n" + row[2]])
            data[1].append([qsum, row[0] + "\n" + row[2]])
            data[2].append([rqsum, row[0] + "\n" + row[2]])
    # sort desc
    for i in range(3):
        data[i].sort(reverse=True)
        data[i] = data[i][:30]
    title = ["Riding", "Quit", "Riding And Quit"]
    index = [311, 312, 313]
    plt.figure(figsize=(20, 10))
    plt.subplots_adjust(hspace=1.5)
    for row in range(3):
        plt.subplot(index[row])
        plt.title(f"Busiest Subway 7AM to 9AM({title[row]})")
        plt.xlabel("지하철역")
        plt.ylabel("인원 수")
        plt.xticks(rotation=90)
        pdata = [[], [], []]
        for i in range(30):
            pdata[0].append(data[row][i][0])
            pdata[1].append(data[row][i][1])
        plt.bar(pdata[1], pdata[0], 0.7)
    plt.savefig("./test/Q4/q4-1.jpg")
    plt.show()
    # file close 
    f.close()

def main():
    solve()
if __name__ =="__main__":
    main()