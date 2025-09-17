from ellipse import Ellipse
import time 

def do_calcultaions():
    i = 0
    while i < 10:
        obj = Ellipse()
        print(f'Площадь эллипса равна: {Ellipse.calculate_area(obj)}')
        print(f'Периметр эллипса равен: {Ellipse.calculate_perimeter(obj)}')
        i += 1        
        time.sleep(0.5)
        
do_calcultaions()
