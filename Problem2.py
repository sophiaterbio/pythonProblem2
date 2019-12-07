import numpy as np
import math

x1 = int(input('Enter x coordinate of point 1: '))
y1 = int(input('Enter y coordinate of point 1: '))
x2 = int(input('Enter x coordinate of point 2: '))
y2 = int(input('Enter y coordinate of point 2: '))
x3 = int(input('Enter x coordinate of point 3: '))
y3 = int(input('Enter y coordinate of point 3: '))

xmatrix = np.array([[(x1**2+y1**2), y1, 1],
      [(x2**2+y2**2), y2, 1],
      [(x3**2+y3**2), y3, 1]])
ymatrix = np.array([[(x1**2+y1**2), x1, 1],
      [(x2**2+y2**2), x2, 1],
      [(x3**2+y3**2), x3, 1]])
zmatrix = np.array([[x1, y1, 1],
      [x2, y2, 1],
      [x3, y3, 1]])
amatrix = np.array([[(x1**2+y1**2), x1, y1],
      [(x2**2+y2**2), x2, y2],
      [(x3**2+y3**2), x3, y3]])
      
detx = np.linalg.det(xmatrix);
dety = np.linalg.det(ymatrix);
detz = np.linalg.det(zmatrix);
deta = np.linalg.det(amatrix);
      
h = round((1/2)*(detx/detz),4);
k = round(-1*(1/2)*(dety/detz),4);
c = [h,k];      
print('center (h,k): ',c);

r = round(math.sqrt(h**2 + k**2 + (deta/detz)),4);
print('radius r: ',r);


D = round(-1*(detx/detz),4);
E = round(dety/detz,4);
F = round(-1*(deta/detz),4);
v = [D,E,F];
print('Vector [D E F]: ',v);


