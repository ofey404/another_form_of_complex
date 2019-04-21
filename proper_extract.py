# 在程序中设计合适的计算函数，正确反映出函数g(z)=\sqrt{z^2-1}的计算特性。
from math import pi, e, sin, cos, sqrt, atan
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


class my_complex(object):
    """用r，theta重新定义一个复数类。重载一些运算符"""

    def __init__(self, r, theta):
        """角度单位为rad"""
        self.r = r
        self.t = theta

    def __add__(self, other):
        r1, t1, r2, t2 = self.r, self.t, other.r, other.t
        rf = sqrt(r1**2 + r2**2 + 2*r1*r2*cos(t1-t2))

        if rf == 0:
            return my_complex(0, 0)  # 0向量幅角定义为0

        sin_d = r2 * sin(t2-t1) / rf
        cos_d = (r1**2+rf**2-r2**2) / (2*r1*rf)

        if cos_d == 0:
            if sin_d > 0:
                delta = pi / 2
            else:
                delta = - pi / 2
        else:
            delta = atan(sin_d/cos_d)
            if cos_d >= 0:
                delta = delta
            elif cos_d < 0 and sin_d > 0:
                delta = delta + pi/2
            else:
                delta = delta - pi/2
        tf = t1 + delta

        return my_complex(rf, tf)

    def __sub__(self, other):
        return self + my_complex(other.r, other.t+pi)

    def __mul__(self, other):
        r1, t1, r2, t2 = self.r, self.t, other.r, other.t
        return my_complex(r1*r2, t1+t2)

    def __truediv__(self, other):
        r1, t1, r2, t2 = self.r, self.t, other.r, other.t
        if r2 == 0:
            raise Exception("r2 div 0 !!!")
        return my_complex(r1/r2, t1-t2)

    def __str__(self):
        return "{}*e^i*{}".format(self.r, self.t)

    def i_form(self):
        """转换成常规的复数"""
        real = self.r * cos(self.t)
        imag = self.r * sin(self.t)
        return complex(real, imag)


def mc_sqrt(mc, n):
    return my_complex(sqrt(mc.r), mc.t/2 + n*pi)


def mc_sqrt_generator(mc):
    """返回一个函数mcs_of_n
      mcs_of_n(n) = r^(1/2)*exp(i*(theta/2+n*pi))"""
    def mcs_of_n(n):
        return my_complex(sqrt(mc.r), mc.t/2 + n*pi)

    return mcs_of_n


def test_my_complex():
    a = my_complex(1, 0)
    b = my_complex(1, pi)
    c = my_complex(1, pi/2)
    print('a={}'.format(a))
    print('b={}'.format(b))
    print('c={}'.format(c))
    print("\n")
    print("a+b={}".format(a+b))
    print("a+c={}".format(a+c))
    print('a-b={}'.format(a-b))
    print('a-c={}'.format(a-c))
    print("\n")
    print("a*b={}".format(a*b))
    print("a*c={}".format(a*c))
    print("a/b={}".format(a/b))

    mcs_b = mc_sqrt_generator(b)
    for n in range(-2, 2):
        print('sqrt(b) = {} \n when n = {} \n'.format(mcs_b(n), n))
    print('b={}'.format(b))
    print("\n")
    
    print("the x+jy form of a = {}".format(a.i_form()))



def g(z):
    """目标函数
      z属于my_complex类型
      g = sqrt(z^2-1)
    """
    return mc_sqrt_generator(z*z - 1)


def main():
    """画出g(z)在n取单值的情况下，在r-theta极坐标下的三维图，第三维为函数g的取值 
      在r属于[0, inf], theta属于[-inf, inf]上
      或者说取r，theta为广义坐标
      此时的g是连续的，用画图来说明这一点。
      绘图参考了matplotlib中文手册：https://www.matplotlib.org.cn/gallery/mplot3d/voxels_torus.html
    """




if __name__ == "__main__":
    main()