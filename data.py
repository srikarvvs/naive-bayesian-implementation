"""
data should be loaded into following format
either any one dataset should be loaded
other datset should be in comments
"""
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
				tuple_body += _dismissquotes(line.strip().split(sep))
		else:
			for line in open_file.readlines():
				tuple_body += line.strip().split(sep)
		return tuple_head,tuple_body

"""
first dataset
"""

buys_computer_head = ["age","income","student","credit_rating"]
buys_computer_body = [
	["youth","high","no","fair","no"],
	["youth","high","no","excellent","no"],
	["middle aged","high","no","fair","yes"],
	["senior","medium","no","fair","yes"],
	["senior","low","yes","fair","yes"],
	["senior","low","yes","excellent","no"],
	["middle aged","low","yes","excellent","yes"],
	["youth","medium","no","fair","no"],
	["youth","low","yes","fair","yes"],
	["senior","medium","yes","fair","yes"],
	["youth","medium","yes","excellent","yes"],
	["middle aged","medium","no","excellent","yes"],
	["middle aged","high","yes","fair","yes"],
	["senior","medium","no","excellent","no"]
]

"""
second dataset 
"""
play_cricket_head = ["outlook","temp","humidty","windy"]
play_cricket_body = [
	["sunny","hot","high","false","no"],
	["sunny","hot","high","true","no"],
	["overcast","hot","high","false","yes"],
	["rainy","mild","high","false","yes"],
	["rainy","cool","normal","false","yes"],
	["rainy","cool","normal","true","no"],
	["overcast","cool","normal","true","yes"],
	["sunny","mild","high","false","no"],
	["rainy","cool","normal","false","yes"],
	["sunny","mild","normal","false","yes"],
	["sunny","mild","normal","true","yes"],
	["overcast","mild","high","true","yes"],
	["overcast","hot","normal","false","yes"],
	["rainy","mild","high","true","no"]
]




#made by venkat 
