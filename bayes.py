"""
Author  :   Venkat
Topic   :   Bayes Classifier
"""

from data import *
import statistics
import math
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
def count_num(clss,attr_idx,attr_val,data_set):
    '''returns p(attr_val/clss) i.e., p(xi/ci) using Gaussian Probability Density Function
        g(xi,mean,sd)=(1 / (sqrt(2 * pi) * sd)) * exp(-((xi-mean^2)/(2*sd^2))) where
            mean is the mean of values of attribute Ai for observations of class ci
            sd is standard deviation of values of attribute Ai for observations of class ci
            ci is one of values of output variable
            xi is given value for attribute Ai
    '''
    attr_vals=[]
    for row in data_set:
        if row[-1]==clss :
            attr_vals.append(row[attr_idx])
    mean=statistics.mean(attr_vals)
    sd=statistics.stdev(attr_vals)
    res= (1 / (math.sqrt(2 * math.pi) * sd)) * math.exp(-((attr_val-mean**2)/(2*sd**2)))
    return res

def by_bayes_theorem(data_set,x,head,meta):
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
        p(xi/ci) = n(xi ^ ci) / n(ci) for categorical data
        p(xi/ci) = g(xi,mean_ci,sd_ci) where 'g()' is Gaussian Probability Density Function
        xi is in X tuple
        ci is class of output variable
    '''
    for i,xi in enumerate(x):
        for j in clss:
            if 'numeric' in meta[head[i]]:
                # For numeric data, we use Gaussian Probability Density Function
                temp=count_num(j,i,xi,data_set)
            else:
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
    print(prob)
    for i in prob:
        if prob[i] > max:
            maxItem = i
            max = prob[i]
    return maxItem
def _dismissquotes(line_list):
	return [i.strip('"') for i in line_list]
def load_data(file_name,headless=False,with_quote=True,sep=","):
	tuple_head,tuple_body = [],[]
	try:
		open_file = open(file_name)
	except:
		raise ValueError("No File Found")
	else:
		if not headless:
			tuple_head += open_file.readline().strip().split(sep)
			if with_quote:
				tuple_head[:] = _dismissquotes(tuple_head)
		if with_quote:
			for line in open_file.readlines():
				tuple_body += [_dismissquotes(line.strip().split(sep))]
		else:
			for line in open_file.readlines():
				if line.strip() == "":	
					continue	
				tuple_body += [line.strip().split(sep)]
		return tuple_head,tuple_body
def load_data_with_meta(file_name,meta,headless=False,with_quote=True,sep=","):
	tuple_head,tuple_body = load_data(file_name,headless,with_quote,sep)# load data 
	for attrib in meta:
		if meta[attrib] == "numeric":
			index = tuple_head.index(attrib)
			row = 0
			while row!=len(tuple_body):
				if '.' in tuple_body[row][index]:
					tuple_body[row][index] = float(tuple_body[row][index])
				else:
					tuple_body[row][index] = int(tuple_body[row][index])
				row += 1
	return tuple_head,tuple_body
def main():
    x = []
    print("---data slecetion--\n1.buys computer\n2.play cricket\n3.buys computer(age as numeric)")
    try:
        ch = int(input("enter choice : "))#select dataset
    except:
        print("Something wrong with choice")
    else:
        if ch == 1:
            _head, data_set = load_data(buys_computer_file,with_quote=True)  
            for i in _head:
                temp = input("Enter %s(%s): "%(i,buys_computer_meta[i]))
                x.append(temp)
            print(by_bayes_theorem(data_set,x,_head,buys_computer_meta),",Buys computer")
        elif ch == 2:
            _head,data_set = load_data(play_cricket_file,with_quote=True)
            for i in _head:
                temp = input("Enter %s(%s): "%(i,play_cricket_meta[i]))
                x.append(temp)
            print(by_bayes_theorem(data_set,x,_head,play_cricket_meta),",Play Cricket")
        elif ch == 3:
            _head,data_set = load_data_with_meta(buys_computer2_file,meta=buys_computer2_meta)
            for i in _head:
                temp = input("Enter %s(%s): "%(i,buys_computer2_meta[i]))
                x.append(temp)
            try:
                x[0]=int(x[0])
                print(by_bayes_theorem(data_set,x,_head,buys_computer2_meta),",Buys computer")
            except ValueError:
                print("Enter age value as number of years")
if __name__ == "__main__":
    print("--needed (test1.csv,buys_computer),(test2.csv,play cricket),(test3.csv,buys computer2withnumeric)---")         
    print("\tLook on the meta in 'data.py' file")
    main()