from ModelFactory import *

class FlaskModel():
    def __init__(self):
        self.factory = ModelFactory()
        self.state = self.factory.getModelByState('classify')
        self.state_name = "classify"

    # def forward(self, input):
    #     return self.state.forward(input)

    def predict(self, input):
        return self.state.predict(input)

    def getState(self):
        return self.state_name

    def switch_state(self, state_name):
        self.state = self.factory.getModelByState(state_name)
        self.state_name = state_name