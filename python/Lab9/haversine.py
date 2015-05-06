#Created on 1 May 2015

from math import radians, cos, sin, asin, sqrt
'''lat1 = int(raw_input("Please enter the first latitude."))
lon1 = int(raw_input("Please enter the first longitude."))
lat2 = int(raw_input("Please enter the second latitude."))
lon2 = int(raw_input("Please enter the second longitude."))'''
lat1,lon1,lat2,lon2 = 40.689248, -74.044501, 53.382797, -6.602593

Rad = 6371

diffLat = radians(lat2 - lat1)
diffLon = radians(lon2 - lon1)
lat1 = radians(lat1)
lat2 = radians(lat2)

a = sin(diffLat/2)**2 + cos(lat1)*cos(lat2)*sin(diffLon/2)**2
c = 2*asin(sqrt(a))

print "Distance =",Rad * c