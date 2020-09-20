"""Plane angles tests module.

Copyright (c) 2020 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""

from siarnaq.planeangles import PlaneAngle


def test_property_getter_scales():
    assert PlaneAngle().scales == {'de', 'gr', 'mi', 'ma', 'ra', 'sa'}


def test_conv_de_to_gr():
    assert round(PlaneAngle.conv_de_to_gr(1), 2) == 1.11


def test_conv_de_to_mi():
    assert round(PlaneAngle.conv_de_to_mi(1), 2) == 17.45


def test_conv_de_to_ma():
    assert round(PlaneAngle.conv_de_to_ma(1), 2) == 60


def test_conv_de_to_ra():
    assert round(PlaneAngle.conv_de_to_ra(1), 2) == 0.02


def test_conv_de_to_sa():
    assert round(PlaneAngle.conv_de_to_sa(1), 2) == 3600


def test_conv_gr_to_de():
    assert round(PlaneAngle.conv_gr_to_de(1), 2) == 0.9


def test_conv_gr_to_mi():
    assert round(PlaneAngle.conv_gr_to_mi(1), 2) == 15.71


def test_conv_gr_to_ma():
    assert round(PlaneAngle.conv_gr_to_ma(1), 2) == 54


def test_conv_gr_to_ra():
    assert round(PlaneAngle.conv_gr_to_ra(1), 2) == 0.02


def test_conv_gr_to_sa():
    assert round(PlaneAngle.conv_gr_to_sa(1), 2) == 3240


def test_conv_mi_to_de():
    assert round(PlaneAngle.conv_mi_to_de(1), 2) == 0.06


def test_conv_mi_to_gr():
    assert round(PlaneAngle.conv_mi_to_gr(1), 2) == 0.06


def test_conv_mi_to_ma():
    assert round(PlaneAngle.conv_mi_to_ma(1), 2) == 3.44


def test_conv_mi_to_ra():
    assert round(PlaneAngle.conv_mi_to_ra(1000), 2) == 1.00


def test_conv_mi_to_sa():
    assert round(PlaneAngle.conv_mi_to_sa(1), 2) == 206.26


def test_conv_ma_to_de():
    assert round(PlaneAngle.conv_ma_to_de(1), 2) == 0.02


def test_conv_ma_to_gr():
    assert round(PlaneAngle.conv_ma_to_gr(1), 2) == 0.02


def test_conv_ma_to_mi():
    assert round(PlaneAngle.conv_ma_to_mi(1), 2) == 0.29


def test_conv_ma_to_ra():
    assert round(PlaneAngle.conv_ma_to_ra(1000), 2) == 0.29


def test_conv_ma_to_sa():
    assert round(PlaneAngle.conv_ma_to_sa(1), 2) == 60
