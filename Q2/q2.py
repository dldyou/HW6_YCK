import matplotlib.pyplot as plt
import numpy as np
import random as r
import csv

# def makeCSV():
#     N = 100
#     while(N <= 100000):
#         dice = []
#         for i in range(N):
#             x = r.randint(1, 6)
#             dice.append(x)

#         file_name = f"./test/Q2/sample{N}.csv"
#         f = open(file_name, "w", encoding="cp949")
#         f.write("dice\n")
#         for i in range(N):
#             f.write(f"{dice[i]}\n")
#         f.close()
#         N *= 10
    
def solve():
    N = 100
    plt.figure(1)
    idx = 411
    while(N <= 100000):
        file_name = f"./sample{N}.csv"
        f = open(file_name)
        data = csv.reader(f)
        next(data)
        
        dice = [0]
        for row in data:
            dice.append(int(row[0]))
        
        plt.subplot(idx)
        plt.title(f"Dice Simulator N={N}")
        plt.xlabel("dice")
        plt.ylabel("cnt")
        plt.hist(dice, bins=7, width=1)
        plt.axhline(N / 6, color="r", linewidth="1", label="avg")
        plt.xlim(1, 6)
        plt.legend()
        N *= 10
        idx += 1
    plt.show()
def main():
    # makeCSV()
    solve()
if __name__ =="__main__":
    main()