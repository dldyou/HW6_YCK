import matplotlib.pyplot as plt
import numpy as np
import csv

def solve():
    # file open
    f = open('./jeju_gender.csv')
    data = csv.reader(f)
    next(data)

    year = []
    male = []
    female = []
    for row in data:
        year.append(row[0])
        male.append(int(row[2]))
        female.append(int(row[3]))
    
    plt.title("Jeju Gender 1955-2010")
    plt.xlabel("year")
    plt.ylabel("cnt")
    x = np.arange(len(year))
    plt.xticks(x, year)
    plt.plot(x, male, label="male")
    plt.plot(x, female, label="female")
    plt.legend()
    plt.show()
    # file close 
    f.close()

def main():
    solve()
if __name__ =="__main__":
    main()