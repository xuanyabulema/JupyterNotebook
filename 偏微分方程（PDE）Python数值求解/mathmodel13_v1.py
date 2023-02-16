# mathmodel13_v1.py
# Demo10 of mathematical modeling algorithm
# Solving partial differential equations
# 偏微分方程数值解法

import numpy as np
import matplotlib.pyplot as plt

# 1. 一维平流方程 (advection equation)
# U_t + v*U_x = 0

# 初始条件函数 U(x,0)
def funcUx0(x, p): 
    u0 = np.sin(2 * (x-p)**2)
    return u0

# 输入参数
v1 = 1.0  # 平流方程参数，系统速度
p = 0.25  # 初始条件函数 u(x,0) 中的参数

tc = 0  # 开始时间
te = 1.0  # 终止时间: (0, te)
xa = 0.0  # 空间范围: (xa, xb)
xb = np.pi
dt = 0.02  # 时间差分步长
nNodes = 100  # 空间网格数

# 初始化
nsteps = round(te/dt)
dx = (xb - xa) / nNodes
x = np.arange(xa-dx, xb+2*dx, dx)
ux0 = funcUx0(x, p)

u = ux0.copy()  # u(j)
ujp = ux0.copy()  # u(j+1)

# 时域差分
for i in range(nsteps):
    plt.clf()  # 清除当前 figure 的所有axes, 但是保留当前窗口

    # 计算 u(j+1)
    for j in range(nNodes + 2):
        ujp[j] = u[j] - (v1 * dt/dx) * (u[j] - u[j-1])

    # 更新边界条件
    u = ujp.copy()
    u[0] = u[nNodes + 1]
    u[nNodes+2] = u[1]

    # 绘图
    plt.plot(x, u, 'b-', label="v1= 1.0")
    plt.axis((xa-0.1, xb + 0.1, -1.1, 1.1))
    plt.xlabel("x")
    plt.ylabel("U(x)")
    plt.legend(loc=(0.05,0.05))
    plt.title("Advection equation with finite difference method, t = %.4f" % (tc + dt))
    plt.text(0.05,0.9,"youcans-xupt",color='gainsboro')
    plt.pause(0.001)
    tc += dt

plt.show()
