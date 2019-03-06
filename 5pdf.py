#函式
def add_x_and_y(x, y):
    pass #這個函式先不做事情
# --------------------------------------------------------------
def add_x_and_y1(x, y):
    """
        add x and y1 and return sum
        :param x:  eg.10
        :param y:  eg.7
        :return:  x+y
        """
    sum1 = x + y
    return sum1

a = 10
b = 7
a_b = add_x_and_y1(a, b)
print(a_b)
#函式的功用
c = 5
d = 20
c_d = add_x_and_y1(c, d)
print(c_d)
#--------------------------------------------------------------
#預設值
def add_x_and_y2(x, y=15):
    """
        add x and y2 and return sum
        :param x:  eg.7
        :param y:  eg.15
        :return:  x+y
        """
    sum2 = x + y
    return sum2

c = 7
c_ = add_x_and_y2(c)
print(c_)
#--------------------------------------------------------------
#變動數量量的參參數個數
def add_x_and_y3(x, *y): #第二個之後的被歸納為y
    """
        add x and y3 and return sum
        :param x:
        :param y:
        :return:  x+y
        """
    sum3 = x + sum(y)  #sum(y)為保留字 ,為y的總和
    return sum3

a = 10 #等於x
b = 6
c = 8
d = 5
e = 9
a_e = add_x_and_y3(a, b, c, d, e)
print(a_e)
a_e_20 = add_x_and_y3(a, b, c, d, e,20)
print(a_e_20)
#--------------------------------------------------------------
def add_x_and_y_return_multi_value(x, y):
    sum_num = x + y
    avg =  sum_num/2
    return sum_num, avg

f = 5
g = 20
f_g = add_x_and_y_return_multi_value(f, g)
print(f_g)
f_g_sum, f_g_avg1 = add_x_and_y_return_multi_value(f, g)
print(f_g_sum)
print(f_g_avg1)
#--------------------------------------------------------------
#匿名函式
#從list中過濾出奇數
ls = [5, 9, 6, 4, 56, 478, 78, 91]
def is_odd(x):
    return x % 2 == 1 #挑出奇數
#result = list(filter(is_odd, ls)) #怎麼過濾,過濾什麼
result = list(filter(lambda x: x % 2 == 1, ls)) #函式只用到一次,把它隱藏在裡面
print(result)
#--------------------------------------------------------------
#模組
def get_weather_observe():
    return 'weather_observe'

def get_weather_forecast():
    return 'weather_forecast'

import WeatherService as WeatherService