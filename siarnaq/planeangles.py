"""Plane angles conversions.

Copyright (c) 2020 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""
import math


class PlaneAngle:
    """Plane angles class.

    """
    _scales = {
        'de',  # Degree
        'gr',  # Gradiant
        'mi',  # Milliradiant
        'ma',  # Minute of arc
        'ra',  # Radian
        'sa',  # Second of arc
    }

    def __init__(self, scale='de', angle=0.):
        """Initialize new PlaneAnge instances.

        Raises:
            NameError if the given scale is not supported.
        """
        if scale not in self._scales:
            raise NameError(scale)
        self._scale = scale
        self._angle = float(angle)

    @property
    def scales(self):
        """Supported plane angles scales.

        Returns:
            A set of the managed scales.
        """
        return self._scales

    @property
    def scale(self):
        """Scale of the object.

        Returns:
            A string containing a scale included in the supported scales set.
        """
        return self._scale

    @property
    def angle(self):
        """Angle of the object.

        Returns:
            A Float containing an angle included in the object's scale.
        """
        return self._angle

    @property
    def degree(self):
        """Degree value.

        Returns:
            A float containg the Degree value.
        """
        if self._scale == 'de':
            return self._angle
        if self._scale == 'gr':
            return self.conv_gr_to_de(self._angle)
        if self._scale == 'mi':
            return self.conv_mi_to_de(self._angle)
        if self._scale == 'ma':
            return self.conv_ma_to_de(self._angle)
        if self._scale == 'ra':
            return self.conv_ra_to_de(self._angle)
        if self._scale == 'sa':
            return self.conv_sa_to_de(self._angle)

    @property
    def gradian(self):
        """Gradian value.

        Returns:
            A float containg the Gradian value.
        """
        if self._scale == 'de':
            return self.conv_de_to_gr(self._angle)
        if self._scale == 'gr':
            return self._angle
        if self._scale == 'mi':
            return self.conv_mi_to_gr(self._angle)
        if self._scale == 'ma':
            return self.conv_ma_to_gr(self._angle)
        if self._scale == 'ra':
            return self.conv_ra_to_gr(self._angle)
        if self._scale == 'sa':
            return self.conv_sa_to_gr(self._angle)

    @staticmethod
    def conv_de_to_gr(angle):
        """Convert Degree value to Gradiant.

        Args:
            angle: A float containing the Degree value to convert.

        Returns:
            A float containing the Gradiant value.
        """
        return angle * 200 / 180

    @staticmethod
    def conv_de_to_mi(angle):
        """Convert Degree value to Milliradian.

        Args:
            angle: A float containing the Degree value to convert.

        Returns:
            A float containing the Milliradian value.
        """
        return angle * 1000 * math.pi / 180

    @staticmethod
    def conv_de_to_ma(angle):
        """Convert Degree value to Minute of arc.

        Args:
            angle: A float containing the Degree value to convert.

        Returns:
            A float containing the Minute of arc value.
        """
        return angle * 60

    @staticmethod
    def conv_de_to_ra(angle):
        """Convert Degree value to Radian.

        Args:
            angle: A float containing the Degree value to convert.

        Returns:
            A float containing the Radian value.
        """
        return angle * math.pi / 180

    @staticmethod
    def conv_de_to_sa(angle):
        """Convert Degree value to Second of arc.

        Args:
            angle: A float containing the Degree value to convert.

        Returns:
            A float containing the Second of arc value.
        """
        return angle * 3600

    @staticmethod
    def conv_gr_to_de(angle):
        """Convert Gradian value to Degree.

        Args:
            angle: A float containing the Gradian value to convert.

        Returns:
            A float containing the Degree value.
        """
        return angle * 180 / 200

    @staticmethod
    def conv_gr_to_mi(angle):
        """Convert Gradian value to Milliradian.

        Args:
            angle: A float containing the Gradian value to convert.

        Returns:
            A float containing the Milliradian value.
        """
        return angle * 1000 * math.pi / 200

    @staticmethod
    def conv_gr_to_ma(angle):
        """Convert Gradian value to Minute of arc.

        Args:
            angle: A float containing the Gradian value to convert.

        Returns:
            A float containing the Minute of arc value.
        """
        return angle * 54

    @staticmethod
    def conv_gr_to_ra(angle):
        """Convert Gradian value to Radian.

        Args:
            angle: A float containing the Gradian value to convert.

        Returns:
            A float containing the Radian value.
        """
        return angle * math.pi / 200

    @staticmethod
    def conv_gr_to_sa(angle):
        """Convert Gradian value to Second of arc.

        Args:
            angle: A float containing the Gradian value to convert.

        Returns:
            A float containing the Second of arc value.
        """
        return angle * 3240

    @staticmethod
    def conv_mi_to_de(angle):
        """Convert Milliradian value to Degree.

        Args:
            angle: A float containing the Milliradian value to convert.

        Returns:
            A float containing the Degree value.
        """
        return angle * 180 / 1000 / math.pi

    @staticmethod
    def conv_mi_to_gr(angle):
        """Convert Milliradian value to Gradian.

        Args:
            angle: A float containing the Milliradian value to convert.

        Returns:
            A float containing the Gradian value.
        """
        return angle * 200 / 1000 / math.pi

    @staticmethod
    def conv_mi_to_ma(angle):
        """Convert Milliradian value to Minute of arc.

        Args:
            angle: A float containing the Milliradian value to convert.

        Returns:
            A float containing the Minute of arc value.
        """
        return angle * 60 * 180 / 1000 / math.pi

    @staticmethod
    def conv_mi_to_ra(angle):
        """Convert Milliradian value to Radian.

        Args:
            angle: A float containing the Milliradian value to convert.

        Returns:
            A float containing the Radian value.
        """
        return angle / 1000

    @staticmethod
    def conv_mi_to_sa(angle):
        """Convert Milliradian value to Second of arc.

        Args:
            angle: A float containing the Milliradian value to convert.

        Returns:
            A float containing the Second of arc value.
        """
        return angle * (3600 * 180) / (1000 * math.pi)

    @staticmethod
    def conv_ma_to_de(angle):
        """Convert Minute of arc value to Degree.

        Args:
            angle: A float containing the Minute of arc value to convert.

        Returns:
            A float containing the Degree value.
        """
        return angle / 60

    @staticmethod
    def conv_ma_to_gr(angle):
        """Convert Minute of arc value to Gradian.

        Args:
            angle: A float containing the Minute of arc value to convert.

        Returns:
            A float containing the Gradian value.
        """
        return angle / 54

    @staticmethod
    def conv_ma_to_mi(angle):
        """Convert Minute of arc value to Milliradian.

        Args:
            angle: A float containing the Minute of arc value to convert.

        Returns:
            A float containing the Milliradian value.
        """
        return angle * 1000 * math.pi / (60 * 180)

    @staticmethod
    def conv_ma_to_ra(angle):
        """Convert Minute of arc value to Radian.

        Args:
            angle: A float containing the Minute of arc value to convert.

        Returns:
            A float containing the Radian value.
        """
        return angle * math.pi / (60 * 180)

    @staticmethod
    def conv_ma_to_sa(angle):
        """Convert Minute of arc value to Second of arc.

        Args:
            angle: A float containing the Minute of arc value to convert.

        Returns:
            A float containing the Second of arc value.
        """
        return angle * 60

    @staticmethod
    def conv_ra_to_de(angle):
        """Convert Radian value to Degree.

        Args:
            angle: A float containing the Radian value to convert.

        Returns:
            A float containing the Degreevalue.
        """
        return angle * 180 / math.pi

    @staticmethod
    def conv_ra_to_gr(angle):
        """Convert Radian value to Gradian.

        Args:
            angle: A float containing the Radian value to convert.

        Returns:
            A float containing the Gradian value.
        """
        return angle * 200 / math.pi

    @staticmethod
    def conv_ra_to_mi(angle):
        """Convert Radian value to Millirradian.

        Args:
            angle: A float containing the Radian value to convert.

        Returns:
            A float containing the Milliradian value.
        """
        return angle * 1000

    @staticmethod
    def conv_ra_to_ma(angle):
        """Convert Radian value to Miinute of arc.

        Args:
            angle: A float containing the Radian value to convert.

        Returns:
            A float containing the Minute of arc value.
        """
        return angle * 60 * 180 / math.pi

    @staticmethod
    def conv_ra_to_sa(angle):
        """Convert Radian value to Second of arc.

        Args:
            angle: A float containing the Radian value to convert.

        Returns:
            A float containing the Second of arc value.
        """
        return (angle * 3600 * 180) / math.pi

    @staticmethod
    def conv_sa_to_de(angle):
        """Convert Second of arc value to Degree.

        Args:
            angle: A float containing the Second of arc value to convert.

        Returns:
            A float containing the Degree value.
        """
        return angle / 3600

    @staticmethod
    def conv_sa_to_gr(angle):
        """Convert Second of arc value to Gradian.

        Args:
            angle: A float containing the Second of arc value to convert.

        Returns:
            A float containing the Gradian value.
        """
        return angle / 3240

    @staticmethod
    def conv_sa_to_mi(angle):
        """Convert Second of arc value to Milliradian.

        Args:
            angle: A float containing the Second of arc value to convert.

        Returns:
            A float containing the Milliradian value.
        """
        return (angle * 1000 * math.pi) / (180 * 3600)

    @staticmethod
    def conv_sa_to_ma(angle):
        """Convert Second of arc value to Minute of arc.

        Args:
            angle: A float containing the Second of arc value to convert.

        Returns:
            A float containing the Minute of arc value.
        """
        return angle / 60

    @staticmethod
    def conv_sa_to_ra(angle):
        """Convert Second of arc value to Radian.

        Args:
            angle: A float containing the Second of arc value to convert.

        Returns:
            A float containing the Radian value.
        """
        return (angle * math.pi) / (180 * 3600)
