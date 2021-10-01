from .common import backend_test, plotting_test
from regdata import Step, Smooth1D, Olympic

def test_step():
    backend_test(Step)
    plotting_test(Step)

def test_smooth1d():
    backend_test(Smooth1D)
    plotting_test(Smooth1D)

def test_olympic():
    backend_test(Olympic)
    plotting_test(Olympic)