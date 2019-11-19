def strangeSort(mapping, nums):
    # Write your code here
    correctvals = []#creating list of all the correct values. Same length as nums
    for jumbl in nums:#going through jumbled values. jumbl is string
        cval = ""
        for jdig in jumbl:#going through each character of current jumbled value
            cval= cval + str(mapping.index(int(jdig)))#mapping is a list of numbers, so must cast each character as int for it to be found in list of ints
        correctvals.append([cval, jumbl])
    #now, have a list with list elements, where first element of each list is the correct value as a string, and second element is the jumbled value as a string
    smallest = correctvals[0]
    """for x in range(len(correctvals)):#selection sort
        position = x
        smallest = correctvals[x]
        for a in range(x+1, len(correctvals)):
            if(int(correctvals[a][0])<int(smallest[0])):
                position = a
                smallest = correctvals[a]
            #if(int(correctvals[a][0])==int(smallest[0])):
            #    position
        temp = correctvals[x]
        correctvals[x] = correctvals[position]
        correctvals[position] = temp
    finale = [] #list to which jumbled values will be added in order
    for x in range(len(correctvals)):
        finale.append(correctvals[x][1])"""
    for x in range(1, len(correctvals)):#insertion sort
        z = x
        while z>0:
            if(int(correctvals[z][0])<int(correctvals[z-1][0])):
                temp = correctvals[z-1]
                correctvals[z-1] = correctvals[z]
                correctvals[z] = temp
            z-=1
    finale = []
    for x in range(len(correctvals)):
        finale.append(correctvals[x][1])
 
 
    return finale
