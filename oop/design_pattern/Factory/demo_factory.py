import abc


class Laptop(abc.ABC):
    @abc.abstractmethod
    def view(self):
        pass


class XPS(Laptop):
    def view(self):
        print('Dell XPS')


class ThinkPad(Laptop):
    def view(self):
        print('Lenovo thinkpad')


class MacPro(Laptop):
    def view(self):
        print('best one')


class LaptopFactory:
    @staticmethod
    def view_laptop(str_type):
        if str_type == 'XPS':
            lap = XPS()
            lap.view()
        elif str_type == 'ThinkPad':
            lap = ThinkPad()
            lap.view()
        elif str_type == 'MacPro':
            lap = MacPro()
            lap.view()


def main():
    lap_factory = LaptopFactory()
    lap_factory.view_laptop('XPS')
    lap_factory.view_laptop('ThinkPad')
    lap_factory.view_laptop('MacPro')


if __name__ == '__main__':
    main()