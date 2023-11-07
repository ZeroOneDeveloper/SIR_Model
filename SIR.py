from matplotlib import pyplot as plt

mu = float(input("mu(개인의 사망률 & 모집단의 출생률) = "))
beta = float(input("beta(전파율)  = "))
gamma = float(input("gamma(회복률) = "))
S = float(input("S(0)  = "))
I = float(input("I(0)  = "))
R = float(input("R(0)  = "))
dS, dI, dR = 0, 0, 0
S_data, I_data, R_data = [], [], []
TIME = 1000
for time in range(TIME):
    t = time / TIME
    S_data.append(S)
    I_data.append(I)
    R_data.append(R)
    dS = mu - beta * S * I - mu * S
    dI = beta * S * I - gamma * I - mu * I
    dR = gamma * I - mu * R
    S += dS
    I += dI
    R += dR
plt.plot(range(TIME), S_data, "b", label="S")
plt.plot(range(TIME), I_data, "r", label="I")
plt.plot(range(TIME), R_data, "g", label="R")
plt.legend()
plt.show()
