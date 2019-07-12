#encoding:utf-8
inData = []
with open('data.txt', mode='r', encoding='utf-8') as f:
    inData = f.readlines()
rows = len(inData)
for i in range(rows):
    inData[i] = inData[i].replace('\n', '').split('\t')
    # print(inData[i])

company, year, accountant, agency = 0, 0, 0, 0
countAgency = [[0, 0, 0]] #初始化一个二维数组 company, agency, count 每公司各事务所的连续次数，前提原始数据中每公司数据按年份排列
for i in range(rows):
    company, year, accountant, agency = inData[i][0], inData[i][1], inData[i][2], inData[i][3]
    # print(company, year, accountant, agency)
    index = len(countAgency) - 1
    if company == countAgency[index][0] and agency == countAgency[index][1]:
        countAgency[index][2] = countAgency[index][2] + 1
    else:
        countAgency.append([company, agency, 1])

length = len(countAgency)
with open('01result.txt', 'w', encoding='utf-8') as f:
    for i in range(length):
        f.write(str(countAgency[i][0]) + '\t' + str(countAgency[i][1]) + '\t' + str(countAgency[i][2]) + '\n')
    
maxAgency = [[0, 0, 0]] #初始化一个二维数组 company, agency, count 每公司只保留一个次数最多的事务所，有两个一样的只取前一个
company, agency, count = 0, 0, 0
for i in range(length):
    company, agency, max = countAgency[i][0], countAgency[i][1], countAgency[i][2]
    index = len(maxAgency) - 1
    if company == maxAgency[index][0]:
        if max > maxAgency[index][2]:
            maxAgency[index][2] = max
    else:
        maxAgency.append([company, agency, max])

length = len(maxAgency)
with open('02result.txt', 'w', encoding='utf-8') as f:
    for i in range(length):
        f.write(str(maxAgency[i][0]) + '\t' + str(maxAgency[i][1]) + '\t' + str(maxAgency[i][2]) + '\n')
    
