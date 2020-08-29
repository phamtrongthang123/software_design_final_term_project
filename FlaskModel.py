from ModelFactory import *

class FlaskModel():
    def __init__(self):
        self.factory = ModelFactory()
        self.state = self.factory.getModelByState('classifier')

    # def forward(self, input):
    #     return self.state.forward(input)

    def predict(self, input):
        return self.state.predict(input)

    def switch_state(self, state_name):
        self.state = ModelFactory.getModelByState(state_name)