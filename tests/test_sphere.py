import pytest
import math
from geometry.sphere import volume_sphere

def test_volume_sphere_valid_inputs():
    """Test volume computation for valid sphere dimensions."""
    radius = 3.0
    expected = 36 * math.pi
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)

# La función incluye su propia validación para radios negativos

def test_volume_sphere_zero_dimension():
    """Document current behaviour when a zero dimension is used."""
    assert volume_sphere(0.0) == 0.0

def test_volume_sphere_float_tolerance():
    """Test volume computation using approximate comparison."""
    radius = 2.5
    expected = (4/3) * math.pi * radius**3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)
