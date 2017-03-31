from core.lib.coreB.libB import Node
from core.lib import tester
from core.lib import pie as p

class Coffee(Node):
    def __init__(self):
        self.flavor = tester.FLAVOR
        print p.FINAL
