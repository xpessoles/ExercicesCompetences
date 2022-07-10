Km = 3.24
Kf = 2.55*1e10
T1 = 10
T2 = 5
Kpom = 1.234*1e7
Kcap = 2.5*1e-8
dqe  = 5*1e-4
q0 = 40e5

Kp = (Kf*dqe-q0)/(q0*Km*Kpom*Kcap)

Kp1 = (-Kf*dqe*Kcap-q0)/(q0*Km*Kpom*Kcap)
Kp2 = (Kf*dqe*Kcap-q0)/(q0*Km*Kpom*Kcap)
print(Kp1,Kp2)