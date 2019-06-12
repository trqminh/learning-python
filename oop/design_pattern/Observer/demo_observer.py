# https://viblo.asia/p/design-pattern-observer-V3m5WO8W5O7
import abc


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, message):
        pass


class Observer1(Observer):
    def update(self, message):
        print('Message 1 update: ' + message)


class Observer2(Observer):
    def update(self, message):
        print('Message 2 update: ' + message)


class Subject:
    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify_change(self, message):
        for observer in self.__observers:
            observer.update(message)


def main():
    subject = Subject()

    obs1 = Observer1()
    obs2 = Observer2()

    subject.attach(obs1)
    subject.attach(obs2)

    subject.notify_change('first change')
    subject.notify_change('second change')


if __name__ == '__main__':
    main()

