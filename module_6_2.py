class Vehicle:
    __Color_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    ch_color = '\033[34m '

    def __init__(self, owner='', __model='', __engine_power=0, __color=''):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'\033[34m Модель: {self.__model}\n'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}\n'

    def get_color(self):
        return f'\033[34m  Цвет:\033[0m {Vehicle.ch_color}{self.__color}\033[0m\n'

    def print_info(self):

        print(f'{self.get_model()} '
              f'{self.get_horsepower()} '
              f'{Vehicle.ch_color}{self.get_color()}\033[0m'
              f'\033[34mВладелец:\033[0m {Vehicle.ch_color}{self.owner}\033[0m'
              )

    def set_color(self, new_color=''):
        if new_color.lower() not in self.__Color_VARIANTS:
            print(f'\033[31m Нельзя сменить цвет на {new_color}\033[0m')
            Vehicle.ch_color = '\033[32m '
        else:
            self.__color = new_color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner='', __model='', __color='', __engine_power=0):
        super().__init__(owner, __model, __engine_power, __color)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
#Pink
# Проверяем что поменялось
vehicle1.print_info()
