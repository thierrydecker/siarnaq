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

    def __add__(self, other):
        new_scale = self.scale
        new_angle = self.angle
        if isinstance(other, PlaneAngle):
            if self.scale == 'de':
                new_angle += other.degree
            elif self.scale == 'gr':
                new_angle += other.gradian
            elif self.scale == 'mi':
                new_angle += other.milliradian
            elif self.scale == 'ma':
                new_angle += other.minute_of_arc
            elif self.scale == 'ra':
                new_angle += other.radian
            elif self.scale == 'sa':
                new_angle += other.second_of_arc
        else:
            new_angle += float(other)
        return PlaneAngle(scale=new_scale, angle=new_angle)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        new_scale = self.scale
        new_angle = self._angle
        if isinstance(other, PlaneAngle):
            if self.scale == 'de':
                new_angle -= other.degree
            elif self.scale == 'gr':
                new_angle -= other.gradian
        else:
            new_angle -= float(other)
        return PlaneAngle(scale=new_scale, angle=new_angle)

    def __mul__(self, other):
        return PlaneAngle(scale=self.scale, angle=self.angle * float(other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return PlaneAngle(scale=self.scale, angle=self.angle / float(other))

    def __str__(self):
        if self.scale == 'de':
            return f'{self.angle} °'
        if self.scale == 'gr':
            return f'{self.angle} g'
        if self.scale == 'mi':
            return f'{self.angle} mrad'
        if self.scale == 'ma':
            return f'{self.angle} \''
        if self.scale == 'ra':
            return f'{self.angle} rad'
        if self.scale == 'sa':
            return f'{self.angle} \'\''

    def __repr__(self):
        return f'PlaneAngle(\'{self.scale}\', {self.angle})'

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

    @property
    def milliradian(self):
        """Milliradian value.

        Returns:
            A float containg the Milliradian value.
        """
        if self._scale == 'de':
            return self.conv_de_to_mi(self._angle)
        if self._scale == 'gr':
            return self.conv_gr_to_mi(self._angle)
        if self._scale == 'mi':
            return self._angle
        if self._scale == 'ma':
            return self.conv_ma_to_mi(self._angle)
        if self._scale == 'ra':
            return self.conv_ra_to_mi(self._angle)
        if self._scale == 'sa':
            return self.conv_sa_to_mi(self._angle)

    @property
    def minute_of_arc(self):
        """Minute of arc value.

        Returns:
            A float containg the Minute of arc value.
        """
        if self._scale == 'de':
            return self.conv_de_to_ma(self._angle)
        if self._scale == 'gr':
            return self.conv_gr_to_ma(self._angle)
        if self._scale == 'mi':
            return self.conv_mi_to_ma(self._angle)
        if self._scale == 'ma':
            return self._angle
        if self._scale == 'ra':
            return self.conv_ra_to_ma(self._angle)
        if self._scale == 'sa':
            return self.conv_sa_to_ma(self._angle)

    @property
    def radian(self):
        """Radian value.

        Returns:
            A float containg the Radian value.
        """
        if self._scale == 'de':
            return self.conv_de_to_ra(self._angle)
        if self._scale == 'gr':
            return self.conv_gr_to_ra(self._angle)
        if self._scale == 'mi':
            return self.conv_mi_to_ra(self._angle)
        if self._scale == 'ma':
            return self.conv_ma_to_ra(self._angle)
        if self._scale == 'ra':
            return self._angle
        if self._scale == 'sa':
            return self.conv_sa_to_ra(self._angle)

    @property
    def second_of_arc(self):
        """Second of arc value.

        Returns:
            A float containg the Secnd of arc value.
        """
        if self._scale == 'de':
            return self.conv_de_to_sa(self._angle)
        if self._scale == 'gr':
            return self.conv_gr_to_sa(self._angle)
        if self._scale == 'mi':
            return self.conv_mi_to_sa(self._angle)
        if self._scale == 'ma':
            return self.conv_ma_to_sa(self._angle)
        if self._scale == 'ra':
            return self.conv_ra_to_sa(self._angle)
        if self._scale == 'sa':
            return self._angle

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
