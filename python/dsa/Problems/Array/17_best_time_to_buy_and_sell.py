

def solution_m1(price):
        mini = price[0]
        profit = 0
        i = 1
        n = len(price)
        while i < n:
            cost = price[i] - mini
            profit = max(cost, profit)
            mini = min(price[i], mini)
            i+=1
        return profit
      
if __name__ =="__main__":
    prices = [7,1,5,3,6,4]
 
    
    print("method 1 : ", solution_m1(prices) , end="\n\n")