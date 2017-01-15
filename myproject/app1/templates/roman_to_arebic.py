roman_value = {'I':10,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}



n = raw_input()
value = 0
for i in range(0,len(n)):
	value += roman_value[n[i]]
	print value,roman_value[n[i]]
	if (i < (len(n)-1)):
		if (roman_value[n[i+1]] < roman_value[n[i]]):
			value -= roman_value[n[i]]*2


print value 
