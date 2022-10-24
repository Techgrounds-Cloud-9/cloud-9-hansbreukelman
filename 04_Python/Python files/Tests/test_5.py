with open("test.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    row1  = next(csvreader)
    #print(row1)

    def makeadictionary(csvreader):
        dct = {}
        keys = []
        valuesdict = {}
        names = []
        next(csvreader)
        for row in csvreader:
            keys.append(row[0])
            dct[row[0]] = row[1],row[2]
            names.append(row[0])
        #print(names)
        for key,value in dct.items():
            value = list(value)
            #print(value)
            job = value[0]
            #print(job)
            birthmonth = value[1]  
            #print(birthmonth)
            dct[key][row1[1]] = job
            dct[key][row1[2]] = birthmonth
        return dct
    print(makeadictionary(csvreader))