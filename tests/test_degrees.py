"""Degrees tests module.

Copyright (c) 2020 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""

import pytest

from siarnaq.degrees import Degree


def test_instanciations():
    assert isinstance(Degree(), Degree)

    assert isinstance(Degree('ce'), Degree)
    assert isinstance(Degree('fa'), Degree)
    assert isinstance(Degree('ke'), Degree)

    assert isinstance(Degree(temp=10), Degree)

    assert isinstance(Degree(scale='ce'), Degree)
    assert isinstance(Degree(scale='fa'), Degree)
    assert isinstance(Degree(scale='ke'), Degree)

    assert isinstance(Degree(scale='ce', temp=0), Degree)
    assert isinstance(Degree(scale='fa', temp=0), Degree)
    assert isinstance(Degree(scale='ke', temp=0), Degree)

    with pytest.raises(Exception):
        assert Degree(scale='Dummy')
        assert Degree(temp='Dummy')
        assert Degree(scale='Dummy', temp='Dummy')


def test_static_methods():
    assert round(Degree.conv_ce_to_fa(temp=0), 2) == 32.00
    assert round(Degree.conv_ce_to_fa(temp=10), 2) == 50.00
    assert round(Degree.conv_ce_to_fa(temp=-10), 2) == 14.00

    assert round(Degree.conv_ce_to_ke(temp=0), 2) == 273.15
    assert round(Degree.conv_ce_to_ke(temp=-273.15), 2) == 0.00
    assert round(Degree.conv_ce_to_ke(temp=-100), 2) == 173.15

    assert round(Degree.conv_fa_to_ce(temp=32), 2) == 0.00
    assert round(Degree.conv_fa_to_ce(temp=-100), 2) == -73.33
    assert round(Degree.conv_fa_to_ce(temp=100), 2) == 37.78
