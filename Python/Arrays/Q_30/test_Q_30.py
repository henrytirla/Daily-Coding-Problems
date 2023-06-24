from Q_30 import apartmentHunting
import Q_30
def test_appartmentHunting():
     req =Q_30.reqs
     block =Q_30.blocks
     assert(apartmentHunting(block,req)) == 3

