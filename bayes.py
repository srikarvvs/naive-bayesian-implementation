from data import *

#x = ["senior","medium","no","excellent"]

def count_a(clss,atti,val,body):
    count = 0
    for i in body:
        if i[-1] == clss and i[atti] == val:
            count += 1
    return count
def by_bayes_theorem(body,x):
    clss = {}
    for i in body:
        if i[-1] not in clss.keys():
            clss[i[-1]] = 1
        else:
            clss[i[-1]] += 1
    main = {}
    for i,xi in enumerate(x):
        for j in clss:
            cnt = count_a(j,i,xi,body)
            temp = float(cnt)/float(clss[j])
            main[(xi,j)] = temp
    prob = {}
    for i in clss:
        prob[i] = 1
        for j in main:
            if j[1] == i:
                if main[j] == 0:
                    continue
                prob[i] *= main[j]
    for i in prob:
        prob[i] = prob[i]*(float(clss[i])/len(body))
    max,maxItem = 0,""
    for i in prob:
        if prob[i] > max:
            maxItem = i
            max = prob[i]
    return maxItem
def main():
    body = []
    x = [] 
    print("---data slecetion--\n1.buys computer\n2.play cricket")
    try:
        ch = int(input("enter choice : "))
    except:
        print("Something wrong with choice")
    else:
        if ch == 1:
            body += buys_computer_body
            for i in buys_computer_head:
                temp = input("Enter %s : "%(i))
                x.append(temp)
            print(by_bayes_theorem(body,x),",Buys computer")
        elif ch == 2:
            body += play_cricket_body
            for i in play_cricket_head:
                temp = input("Enter %s : "%(i))
                x.append(temp)
            print(by_bayes_theorem(body,x),",Play golf")
            
main()





            


