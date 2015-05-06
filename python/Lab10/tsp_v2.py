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
latlong1 = latlong.copy()
endanswer = ""
endtotal = -1
for start in range(1,1001):
    latlong = latlong1.copy()
    print start
    answer = "%s" % start
    count = 1
    total = 0
    while count<1000:
        small = -1
        count+=1
        temp = latlong.pop(start)
        for key, value in latlong.iteritems():
            dist = haver(temp[0],temp[1],value[0],value[1])
            if (dist<small):
                start = key
                small = dist
            elif small==-1:
                start = key
                small = dist
        total+=small
        answer += ".%s" % (start)
    if (total<endtotal):
        endtotal = total
        endanswer = answer
    elif endtotal==-1:
        endtotal = total
        endanswer = answer
print endanswer
print endtotal