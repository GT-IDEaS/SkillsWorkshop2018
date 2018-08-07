def palindrome():
	palindromeList = []
	#This code is not meant to be super robust
	for i in range(9,-1,-1):
		string1 = str(i)+str(i)
		for j in range(9,-1,-1):
			string2 = str(j) +string1+ str(j)
			for k in range(9,0,-1):
				string3 = str(k)+string2+str(k)
				palindromeList.append(string3)
	newList = []
	for item in palindromeList:
		newItem = int(item)
		newList.append(newItem)
	#print(newList)
	newList.sort(reverse=True)
	numbySet =[] 
	for item in newList:
		for item2 in range(999,99,-1):
			if item%item2 == 0 and item//item2 <1000:
				numbySet.append(item2)
				numbySet.append(item/item2)
			if len(numbySet) >= 2:
				break
	
	print(numbySet)
				













palindrome()