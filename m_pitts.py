# McCulloch-Pitts neuron model

# [1] Exclusive OR Gate

#from neural.mcculloch.pitts import model
from neuron import hoc

class XorNetwork(model.Network):
    def __init__(self, a, b):
        super(XorNetwork, self).__init__(*XorNetwork.build_net(a, b))

    @staticmethod
    def build_net(a, b):
       
        return model.AndNeuron(
            model.OrNeuron(a, b),
            model.NotNeuron(model.AndNeuron(a, b))
        ),


class HalfAdder(model.Network):
    def __init__(self, a, b):
        self.output, self.carry = HalfAdder.build_net(a, b)
        super(HalfAdder, self).__init__(self.output, self.carry)

    @staticmethod
    def build_net(a, b):
        sum = XorNetwork.build_net(a, b)[0]
        carry = model.AndNeuron(a, b)
        return sum, carry


class FullAdder(model.Network):
    def __init__(self, cin, a, b):
        self.output, self.carry = FullAdder.build_net(cin, a, b)
        super(FullAdder, self).__init__(self.output, self.carry)

    @staticmethod
    def build_net(cin, a, b):
        xor = XorNetwork.build_net(a, b)[0]
        sum = XorNetwork.build_net(xor, cin)[0]
        carry = model.OrNeuron(
            model.AndNeuron(xor, cin),
            model.AndNeuron(a, b)
        )
        return sum, carry