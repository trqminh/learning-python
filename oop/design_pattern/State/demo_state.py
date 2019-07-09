import abc


class State(abc.ABC):
    @abc.abstractmethod
    def do_action(self):
        pass


class StartState(State):
    def do_action(self):
        print('Start state now')

    def change_state(self, context):
        context.set_state(StopState())


class StopState(State):
    def do_action(self):
        print('Stop state now')


class Context:
    def __init__(self):
        self.__state = None

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

