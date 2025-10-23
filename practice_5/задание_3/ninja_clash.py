from ninja import Ninja
import time
import random

class NinjaClash:
    def __init__(self, enemy_1: Ninja, enemy_2: Ninja) -> None:
        self.__enemies = [enemy_1, enemy_2]
        self.__victory = None
        
    def clash(self) -> None:
        print('Подбрасываем монетку...')
        time.sleep(1)
        who_first = random.randint(0, 1)
        if who_first == 0:
            print(f'Первым атакует {self.__enemies[0].name}')
            first_attack = self.__enemies[0]
            damage = first_attack.throw_shuriken()
            self.__enemies[1].health -= damage
            print(f'{self.__enemies[0].name} нанес {damage} единиц урона. Здоровье противника: {self.__enemies[1].health}')
        else:
            print(f'Первым атакует {self.__enemies[1].name}')
            first_attack = self.__enemies[1]
            damage = first_attack.throw_shuriken()
            self.__enemies[0].health -= damage
            print(f'{self.__enemies[1].name} нанес {damage} единиц урона. Здоровье противника: {self.__enemies[0].health}')

        
        i = who_first + 1
        
        while self.__enemies[0].health > 0 and self.__enemies[1].health > 0:
            if i % 2 == 0:
                damage = self.__enemies[0].throw_shuriken()
                self.__enemies[1].health -= damage
                if self.__enemies[1].health <= 0:
                    print(f'{self.__enemies[0].name} убил {self.__enemies[1].name}. Здоровье противника: 0')
                    self.__victory = self.__enemies[0].name
                    return 
                print(f'{self.__enemies[0].name} нанес {damage} единиц урона. Здоровье противника: {self.__enemies[1].health}')
            else:
                damage = self.__enemies[1].throw_shuriken()
                self.__enemies[0].health -= damage
                if self.__enemies[0].health <= 0:
                    print(f'{self.__enemies[1].name} убил {self.__enemies[0].name}. Здоровье противника: 0')
                    self.__victory = self.__enemies[1].name
                    return 
                print(f'{self.__enemies[1].name} нанес {damage} единиц урона. Здоровье противника: {self.__enemies[0].health}')
            i += 1
            
    def declare_victory(self) -> None:
        print(f'Победил {self.__victory}') 
            
    
ninja_1 = Ninja('Ninja1')
ninja_2 = Ninja('Ninja2')

clh = NinjaClash(ninja_1, ninja_2)

clh.clash()
clh.declare_victory()