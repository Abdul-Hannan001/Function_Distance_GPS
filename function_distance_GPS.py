#distance from North Nazimabad to Manzoor Colony
from math import sqrt,sin,cos,asin,radians

def distance(lat1,lon1,lat2,lon2):
    lat1=radians(lat1)
    lon1=radians(lon1)
    lat2=radians(lat2)
    lon2=radians(lon2)

    dlat=lat2-lat1
    dlon=lon2-lon1

    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*asin(sqrt(a))
    d=c*6371
    print("\n",d,"Kilometers")

distance(24.946178099999997,67.0606352,24.8541244,67.089757)    
