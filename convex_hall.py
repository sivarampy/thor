import math
#jarvis march algorithm

points = [(-7,8), (-4,6), (2,6), (6,4), (8,6), (7,-2), (4,-6), (8,-7),(0,0), (3,- 2),(6,-10),(0,6),(-9,-5),(-8,-2),(-8,0),(-10,3),(-2,2),(-10,4)]

left_most_point = float('inf')      ##find the left most point index
for i in range(len(points)):
    if points[i][0] < left_most_point:
        left_most_point = i

l = left_most_point
result = []
result.append(points[l])

def direction(a,b,p):
    #translate points such that a becomes origin
    b = (b[0]-a[0],b[1]-a[1])
    p = (p[0]-a[0],p[1]-a[1])
    #cross product bxp, if bxp > 0 left of ab line
    cross = b[0]*p[1]-b[1]*p[0]
    if cross > 0:
        return 'left'
    elif cross < 0:
        return 'right'
    else:
        return 'colinear'

while True:
    colinear = []
    n = l - 1
    print(points[l],end=' ')
    for i in range(len(points)):
        if i == l:
            continue
        else:
            if direction(points[l],points[n],points[i]) == 'left':
                n = i
            elif direction(points[l],points[n],points[i]) == 'colinear':
                if (points[i][0]-points[l][0])**2+(points[i][1]-points[l][1])**2 > (points[n][0]-points[l][0])**2+(points[n][1]-points[l][1])**2:
                    colinear.append(points[n])
                    n = i
    if n == left_most_point:
        break
    print('adding: ',points[n])
    result.append(points[n])
    l = n
    if colinear:
        print('adding: ',colinear)
        result = result + colinear

print('boundaries are: ',result)
                    
