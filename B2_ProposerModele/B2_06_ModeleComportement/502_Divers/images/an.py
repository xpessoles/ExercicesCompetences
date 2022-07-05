import math as m
num = m.log(0.38)
num = num*num

den = m.pi*m.pi+num

xi=m.sqrt(num/den)

Tp = 0.44
om0 = 2*m.pi/(Tp*m.sqrt(1-xi*xi))