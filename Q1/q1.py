import matplotlib.pyplot as plt
import numpy as np
import csv

data = {
    "all": [],
    "seoul": [],
    "daejeon": [],
    "busan": [],
    "jeju": []
}

regions = ["all", "seoul", "daejeon", "busan", "jeju"]

def solve():
    # get data
    for region in regions:
        f = open(f"./{region}.csv", "r")
        d = csv.reader(f) 
        next(d)
        
        for row in d:
            if row[2] == "":
                continue
            data[region].append(float(row[2]))
        f.close()
    # print graph
    plt.title("Month Average Temp in 2022")
    for region in regions:
        plt.xticks(np.arange(0, 12, 1))
        plt.plot(data[region], label=region)
    plt.xlabel("month - 1")
    plt.ylabel("temp")
    plt.legend()
    plt.show()
    
def main():
    solve()
if __name__ =="__main__":
    main()