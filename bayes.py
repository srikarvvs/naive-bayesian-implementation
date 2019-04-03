from data import *

#x = ["senior","medium","no","excellent"]

def count_a(clss,atti,val,data_set):
    '''Returns n(val ^ clss) in "data_set" dataset where
        val is the value Xi of an attribute atti
        clss is the class Ci of the output variable
    '''
    count = 0
    for i in data_set:
        if i[-1] == clss and i[atti] == val:
            count += 1
    return count
def by_bayes_theorem(data_set,x):
    '''returns the  Ci for given X using "data_set" Dataset  where
        where p(ci/X)>p(cj/X) for all 1<=j<=n , i!=j 
        Ci is one of classes of output variable
        X is a tuple (x1,x2,x3,.....,xn) where xi is value for attribute Ai
    '''
    clss = {} 
    ''' clss holds the n(ci) for each class ci of output variable
    '''
    for i in data_set:
        if i[-1] not in clss.keys():
            clss[i[-1]] = 1
        else:
            clss[i[-1]] += 1
    main = {}
    '''main holds the p(xi/ci) for each xi and ci where
        p(xi/ci) = n(xi ^ ci) / n(ci)
        xi is in X tuple
        ci is class of output variable
    '''
    for i,xi in enumerate(x):
        for j in clss:
            cnt = count_a(j,i,xi,data_set)
            temp = float(cnt)/float(clss[j])
            main[(xi,j)] = temp
    prob = {}
    ''' prob holds the p(ci/X) for each ci where
        p(ci/X) = ( p(x1/ci)*p(x2/ci)*......*p(xn/ci) )*p(ci) / p(X)
        but p(X) is neglected since it is same for all ci
    '''
    for i in clss:
        prob[i] = 1
        for j in main:
            if j[1] == i:
                if main[j] == 0:
                    continue
                prob[i] *= main[j]
    for i in prob:
        prob[i] = prob[i]*(float(clss[i])/len(data_set))
    max,maxItem = 0,""
    for i in prob:
        if prob[i] > max:
            maxItem = i
            max = prob[i]
    return maxItem
def main():
    data_set = []
    x = [] 
    print("---data slecetion--\n1.buys computer\n2.play cricket")
    try:
        ch = int(input("enter choice : "))#select dataset
    except:
        print("Something wrong with choice")
    else:
        if ch == 1:
            data_set += buys_computer_body
            for i in buys_computer_head:
                temp = input("Enter %s(%s): "%(i,buys_computer_meta[i]))
                x.append(temp)
            print(by_bayes_theorem(data_set,x),",Buys computer")
        elif ch == 2:
            data_set += play_cricket_body
            for i in play_cricket_head:
                temp = input("Enter %s(%s): "%(i,play_cricket_meta[i]))
                x.append(temp)
            print(by_bayes_theorem(data_set,x),",Play golf")
            
main()





            


