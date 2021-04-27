from time import asctime

import matplotlib.pyplot as plt
import numpy as np

# 创建坐标系的初始长度
x = np.arange(-10, 10)
print('				函数查看器[BETA3.0]')
print('注意事项:', '+加,-减,*乘除,/除;', '三角函数:np.tan(),np.sin(),np.cos[PS:后面还可以加h];', '派为np.pi;')
print('不能使用数学写法要把每个符号写完整!')
print('x不要大写!')
while True:
    try:
        # 函数
        input1 = input('y=')
        # 输入的数不为空
        if len(input1) == 0:
            print('错误:不能为空!')
            continue
        # 执行函数
        y = eval(input1)
        # 创建函数窗口
        plt.plot(x, y)
        plt.title('y=' + input1)  # 标题
        plt.grid()  # 网格
        plt.show()  # 打开
    except Exception as ex:
        with open('ERROR.log', 'a') as f:
            f.write('错误:' + str(ex) + '(Time:' + asctime() + ')' + '\n')
