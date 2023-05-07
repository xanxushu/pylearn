"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

import math
from abc import ABCMeta, abstractmethod

class employee(object,metaclass=ABCMeta):
    def __init__(self,name):
        self.name=name

    def getname(self):
        print(self.name)

    @abstractmethod
    def salry(self):
        pass

class partmenteo(employee):
    def __init__(self, name):
        super().__init__(name)
    
    def getname(self):
        return super().getname()
    
    def salry(self):
        return 15000
    
class iter(employee):
    def __init__(self, name):
        super().__init__(name)
    
    def getname(self):
        return super().getname()
    
    def salry(self):
        global worktime
        return worktime*150
    
class saler(employee):
    def __init__(self, name):
        super().__init__(name)
    
    def getname(self):
        return super().getname()
    
    def salry(self):
        global sales
        return 1200+0.05*sales
    
if __name__=='__main__':
    emps=[partmenteo('lisa'),iter('xanxus'),saler('bob'),iter('amy'),saler('taoxin')]
    for emp in emps:
        emp.getname()
        if isinstance(emp,iter):
            worktime=float(input("please input the worktime:"))
        elif isinstance(emp,saler):
            sales=float(input("please input the sales:"))
        print("%.2f"%emp.salry())