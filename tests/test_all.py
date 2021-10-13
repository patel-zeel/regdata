from .common import backend_test, plotting_test_with_plt, plotting_test_without_plt, non_syntetic_test
import regdata as rd

common_tests = [backend_test, plotting_test_with_plt,
                plotting_test_without_plt]


def test_della_gatta_gene():
    backend_test(rd.DellaGattaGene)
    plotting_test_with_plt(rd.DellaGattaGene)
    plotting_test_without_plt(rd.DellaGattaGene)
    non_syntetic_test(rd.DellaGattaGene)


def test_heinonen_4():
    backend_test(rd.Heinonen4)
    plotting_test_with_plt(rd.Heinonen4)
    plotting_test_without_plt(rd.Heinonen4)
    non_syntetic_test(rd.Heinonen4)


def test_jump1d():
    backend_test(rd.Jump1D)
    plotting_test_with_plt(rd.Jump1D)
    plotting_test_without_plt(rd.Jump1D)
    non_syntetic_test(rd.Jump1D)


def test_mcycle():
    backend_test(rd.MotorcycleHelmet)
    plotting_test_with_plt(rd.MotorcycleHelmet)
    plotting_test_without_plt(rd.MotorcycleHelmet)
    non_syntetic_test(rd.MotorcycleHelmet)


def test_olympic():
    backend_test(rd.Olympic)
    plotting_test_with_plt(rd.Olympic)
    plotting_test_without_plt(rd.Olympic)
    non_syntetic_test(rd.Olympic)


def test_sinejump():
    backend_test(rd.SineJump1D)
    plotting_test_with_plt(rd.SineJump1D)
    plotting_test_without_plt(rd.SineJump1D)


def test_sinenoisy():
    backend_test(rd.SineNoisy)
    plotting_test_with_plt(rd.SineNoisy)
    plotting_test_without_plt(rd.SineNoisy)


def test_smooth1d():
    backend_test(rd.Smooth1D)
    plotting_test_with_plt(rd.Smooth1D)
    plotting_test_without_plt(rd.Smooth1D)


def test_step():
    backend_test(rd.Step)
    plotting_test_with_plt(rd.Step)
    plotting_test_without_plt(rd.Step)
