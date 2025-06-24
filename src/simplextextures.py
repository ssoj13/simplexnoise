# Copyright (c) 2012 Eliot Eshelman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
###############################################################################

"""Composite procedural textures built from noise functions.

Various textures are available in multiple dimensions (2D, 3D, and 4D).
"""

import math

import simplexnoise

def marble_noise_2d(octaves, persistence, scale, x, y):
    """2D Marble Noise on the x-axis."""
    return math.cos(float(x) * scale + simplexnoise.octave_noise_2d(
            octaves, persistence, float(scale) / 3.0, x, y)
        );

def marble_noise_3d(octaves, persistence, scale, x, y, z):
    """3D Marble Noise on the x-axis."""
    return math.cos(float(x) * scale + simplexnoise.octave_noise_3d(
            octaves, persistence, float(scale) / 3.0, x, y, z)
        );

def marble_noise_4d(octaves, persistence, scale, x, y, z, w):
    """4D Marble Noise on the x-axis."""
    return math.cos(float(x) * scale + simplexnoise.octave_noise_4d(
            octaves, persistence, float(scale) / 3.0, x, y, z, w)
        );
