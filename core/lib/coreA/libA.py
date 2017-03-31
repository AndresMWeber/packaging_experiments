from ..coreB import libB
from .. import tester
import core.lib.pie as p

class Coffee(libB.Node):
    def __init__(self):
        self.flavor = tester.FLAVOR
        print p
