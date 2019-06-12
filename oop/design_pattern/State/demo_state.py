import abc


class State(abc.ABC):
    @abc.abstractmethod
    def do_action(self):
        pass


class StartState(State):
    def do_action(self):
        print('Start state now')


class StopState(State):
    def do_action(self):
        print('Stop state now')