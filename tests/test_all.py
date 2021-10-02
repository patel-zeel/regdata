from .common import backend_test, plotting_test
import regdata as rd

def test_step():
    backend_test(rd.Step)
    plotting_test(rd.Step)

def test_smooth1d():
    backend_test(rd.Smooth1D)
    plotting_test(rd.Smooth1D)

def test_olympic():
    backend_test(rd.Olympic)
    plotting_test(rd.Olympic)

def test_mcycle():
    backend_test(rd.MotorcycleHelmet)
    plotting_test(rd.MotorcycleHelmet)


def test_gene():
    backend_test(rd.DellaGattaGene)
    plotting_test(rd.DellaGattaGene)