import os
from configparser import ConfigParser
from time import asctime

import matplotlib.pyplot as plt
import numpy as np

print('				函数查看器[BETA3.1]')
print('注意事项:', '+加,-减,*乘除,/除;', '三角函数:np.tan(),np.sin(),np.cos[PS:后面还可以加h];', '派为np.pi;')
print('不能使用数学写法要把每个符号写完整!')
print('注意:最新语法[Tool.x]')
print('配置文件:FunctionConfig.ini;每次修改完请重启')


class func:
    def __init__(self):
        self.FileName = 'FunctionConfig.ini'
        if self.isExisits() == False:
            self.ConfigWrite()
        self.ConfigSet = self.ConfigRead()
        self.x = np.arange(int(self.ConfigSet['Xms']), int(self.ConfigSet['Xmx']))

    def open(self, y, input):
        plt.plot(self.x, y, color=self.ConfigSet['Color'])
        plt.title('y=' + input)  # 标题
        plt.grid()  # 网格
        plt.show()  # 打开

    def ConfigWrite(self):
        con = ConfigParser()
        con['Plot'] = {'xms': '-10',
                       'xmx': '10',
                       'LineColor': 'Blue'}
        con.write(open(self.FileName, 'w'))

    def isExisits(self):
        return os.path.exists(self.FileName)

    def ConfigRead(self):
        con = ConfigParser()
        con.read(self.FileName)
        Xms = con['Plot']['xms']
        Xmx = con['Plot']['xmx']
        Color = con['Plot']['linecolor']
        Set = {'Xms': Xms, 'Xmx': Xmx, 'Color': Color}
        return Set


Tool = func()
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
        Tool.open(y, input1)

    except Exception as ex:
        with open('ERROR.log', 'a') as f:
            f.write('错误:' + str(ex) + '(Time:' + asctime() + ')' + '\n')
