import os
from configparser import ConfigParser
from time import asctime

import matplotlib.pyplot as plt
import numpy as np

print('				函数查看器[1.0]')
print('注意事项:', '+加,-减,*乘除,/除;', '三角函数:np.tan(),np.sin(),np.cos[PS:后面还可以加h];', '派为np.pi;')
print('不能使用数学写法要把每个符号写完整!')
print('注意:x不要大写|或使用Tool.x')
print('警告:[配置文件:FunctionConfig.ini;每次修改完请重启;切记不要乱改,否者后果自负]')


# 函数类
class func:
    def __init__(self):
        self.FileName = 'FunctionConfig.ini'
        if self.isExisits() == False:
            self.ConfigWrite()
        self.ConfigSet = self.ConfigRead()
        # 初始x
        self.x = np.arange(int(self.ConfigSet['Xms']), int(self.ConfigSet['Xmx']))

    # 设置函数
    def plots(self, y):
        plt.plot(self.x, y, color=self.ConfigSet['Color'])

    # 启动
    def open(self):
        plt.grid()  # 网格
        plt.show()  # 打开

    # 写入配置
    def ConfigWrite(self):
        con = ConfigParser()
        con['Plot'] = {'xms': '-10',
                       'xmx': '10',
                       'LineColor': 'Blue',
                       'LineNum': '1'}
        con.write(open(self.FileName, 'w'))

    # 判断配置是否存在
    def isExisits(self):
        return os.path.exists(self.FileName)

    # 读取配置
    def ConfigRead(self):
        con = ConfigParser()
        con.read(self.FileName)
        Xms = con['Plot']['xms']
        Xmx = con['Plot']['xmx']
        Color = con['Plot']['linecolor']
        Num = con['Plot']['LineNum']
        if len(Xms) == 0 or len(Xmx) == 0 or len(Color) == 0 or Num == 0:
            self.ConfigWrite()
        Set = {'Xms': Xms, 'Xmx': Xmx, 'Color': Color, 'LineNum': Num}
        return Set


# 初始化
Tool = func()
x = Tool.x
while True:
    try:
        for i in range(int(Tool.ConfigSet['LineNum'])):
            # 函数
            input1 = input('y=')
            # 输入的数不为空
            if len(input1) == 0:
                print('错误:不能为空!')
                continue
            # 执行函数
            y = eval(input1)
            Tool.plots(y)
        # 打开函数
        Tool.open()
    except Exception as ex:
        with open('ERROR.log', 'a') as f:
            f.write('错误:' + str(ex) + '(Time:' + asctime() + ')' + '\n')
