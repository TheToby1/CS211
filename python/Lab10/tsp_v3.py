#Created on 6 May 2015
from math import radians, cos, sin, asin, sqrt

def haver(lat1,lon1,lat2,lon2):
    Rad = 6371
    
    diffLat = radians(lat2 - lat1)
    diffLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    
    a = sin(diffLat/2)**2 + cos(lat1)*cos(lat2)*sin(diffLon/2)**2
    c = 2*asin(sqrt(a))
    
    return Rad * c

with open("1000airports.txt", "r") as fin:
    filein = fin.read().splitlines()

latlong = {}
for stuff in filein:
    things = [x.strip() for x in stuff.split(',')]
    latlong[int(things[0])] = [float(things[2]),float(things[3])]
#print latlong
count = 1
total = 0
answers = {}
while count<1001:
    temp = latlong[count]
    answers[count] = []
    for key, value in latlong.iteritems():
        dist = haver(temp[0],temp[1],value[0],value[1])
        answers[count].append([dist,key])
    answers[count].sort()
    answers[count].pop(0)
    count+=1
endanswer = ""
endtotal = -1
for start in range(1,1001):
    print start
    answer = "%s" % start
    count = 1
    total = 0
    visited = []
    while count<1000:
        answers1=answers.copy()
        count+=1
        visited.append(start)
        for things in (answers1[start]):
            if things[1] not in visited:
                dist = things[0]
                start = things[1]
                break
        total+=dist
        answer += ".%s" % (start)
    if (total<endtotal):
        endtotal = total
        endanswer = answer
    elif endtotal==-1:
        endtotal = total
        endanswer = answer
print endanswer
print endtotal