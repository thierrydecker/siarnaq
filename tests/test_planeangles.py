"""Plane angles tests module.

Copyright (c) 2020 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""
import pytest

from siarnaq.planeangles import PlaneAngle


def test_property_getter_scales():
    assert PlaneAngle().scales == {'de', 'gr', 'mi', 'ma', 'ra', 'sa'}


def test_class_init():
    with pytest.raises(Exception):
        PlaneAngle(scale='Dummy')
        PlaneAngle(angle='Dummy')
        PlaneAngle(scale='Dummy', angle='Dummy')


def test_property_getter_scale():
    assert PlaneAngle(scale='de').scale == 'de'
    assert PlaneAngle(scale='gr').scale == 'gr'
    assert PlaneAngle(scale='mi').scale == 'mi'
    assert PlaneAngle(scale='ma').scale == 'ma'
    assert PlaneAngle(scale='ra').scale == 'ra'
    assert PlaneAngle(scale='sa').scale == 'sa'


def test_property_getter_angle():
    assert PlaneAngle(scale='de', angle=0).angle == 0
    assert PlaneAngle(scale='gr', angle=1).angle == 1
    assert PlaneAngle(scale='mi', angle=1.5).angle == 1.5
    assert PlaneAngle(scale='ma', angle=2).angle == 2
    assert PlaneAngle(scale='ra', angle=2.5).angle == 2.5
    assert PlaneAngle(scale='sa', angle=3).angle == 3


def test_property_getter_degree():
    assert round(PlaneAngle(scale='de', angle=10).degree, 2) == 10
    assert round(PlaneAngle(scale='gr', angle=10).degree, 2) == 9
    assert round(PlaneAngle(scale='mi', angle=10).degree, 2) == 0.57
    assert round(PlaneAngle(scale='ma', angle=10).degree, 2) == 0.17
    assert round(PlaneAngle(scale='ra', angle=10).degree, 2) == 572.96
    assert round(PlaneAngle(scale='sa', angle=1000).degree, 2) == 0.28


def test_property_getter_gradian():
    assert round(PlaneAngle(scale='de', angle=10).gradian, 2) == 11.11
    assert round(PlaneAngle(scale='gr', angle=10).gradian, 2) == 10
    assert round(PlaneAngle(scale='mi', angle=10).gradian, 2) == 0.64
    assert round(PlaneAngle(scale='ma', angle=10).gradian, 2) == 0.19
    assert round(PlaneAngle(scale='ra', angle=10).gradian, 2) == 636.62
    assert round(PlaneAngle(scale='sa', angle=1000).gradian, 2) == 0.31


def test_property_getter_milliradian():
    assert round(PlaneAngle(scale='de', angle=10).milliradian, 2) == 174.53
    assert round(PlaneAngle(scale='gr', angle=10).milliradian, 2) == 157.08
    assert round(PlaneAngle(scale='mi', angle=10).milliradian, 2) == 10
    assert round(PlaneAngle(scale='ma', angle=10).milliradian, 2) == 2.91
    assert round(PlaneAngle(scale='ra', angle=10).milliradian, 2) == 10000
    assert round(PlaneAngle(scale='sa', angle=1000).milliradian, 2) == 4.85


def test_property_getter_minute_of_arc():
    assert round(PlaneAngle(scale='de', angle=10).minute_of_arc, 2) == 600
    assert round(PlaneAngle(scale='gr', angle=10).minute_of_arc, 2) == 540
    assert round(PlaneAngle(scale='mi', angle=10).minute_of_arc, 2) == 34.38
    assert round(PlaneAngle(scale='ma', angle=10).minute_of_arc, 2) == 10
    assert round(PlaneAngle(scale='ra', angle=10).minute_of_arc, 2) == 34377.47
    assert round(PlaneAngle(scale='sa', angle=1000).minute_of_arc, 2) == 16.67


def test_property_getter_radian():
    assert round(PlaneAngle(scale='de', angle=10).radian, 2) == 0.17
    assert round(PlaneAngle(scale='gr', angle=10).radian, 2) == 0.16
    assert round(PlaneAngle(scale='mi', angle=10).radian, 2) == 0.01
    assert round(PlaneAngle(scale='ma', angle=1000).radian, 2) == 0.29
    assert round(PlaneAngle(scale='ra', angle=10).radian, 2) == 10
    assert round(PlaneAngle(scale='sa', angle=10000).radian, 2) == 0.05


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


def test_conv_ra_to_de():
    assert round(PlaneAngle.conv_ra_to_de(10), 2) == 572.96


def test_conv_ra_to_gr():
    assert round(PlaneAngle.conv_ra_to_gr(1), 2) == 63.66


def test_conv_ra_to_mi():
    assert round(PlaneAngle.conv_ra_to_mi(1), 2) == 1000


def test_conv_ra_to_ma():
    assert round(PlaneAngle.conv_ra_to_ma(1), 2) == 3437.75


def test_conv_ra_to_sa():
    assert round(PlaneAngle.conv_ra_to_sa(1), 2) == 206264.81


def test_conv_sa_to_de():
    assert round(PlaneAngle.conv_sa_to_de(1000), 2) == 0.28


def test_conv_sa_to_gr():
    assert round(PlaneAngle.conv_sa_to_gr(1000), 2) == 0.31


def test_conv_sa_to_mi():
    assert round(PlaneAngle.conv_sa_to_mi(1000), 2) == 4.85


def test_conv_sa_to_ma():
    assert round(PlaneAngle.conv_sa_to_ma(1000), 2) == 16.67


def test_conv_sa_to_ra():
    assert round(PlaneAngle.conv_sa_to_ra(100000), 2) == 0.48
