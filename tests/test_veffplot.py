from src.v_eff import Veff
from src.viz import VeffPlot

def test_veffplot():
    veff_instance = Veff(L=4.5)
    data = veff_instance.Veff_values
    veffploter = VeffPlot(data)
    assert isinstance(veffploter, VeffPlot)
