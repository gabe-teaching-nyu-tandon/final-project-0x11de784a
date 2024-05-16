from src.v_eff import Veff
from src.viz import VeffPlot
import tkinter as tk

def test_veffplot():
    veff_instance = Veff(L=4.5)
    data = veff_instance.Veff_values
    veffploter = VeffPlot(tk.Tk(), data, 0.979795)
    assert isinstance(veffploter, VeffPlot)
