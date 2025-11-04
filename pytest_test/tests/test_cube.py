import pytest
import src.shapes as shapes

@pytest.mark.parametrize("side_length, expected_volume", [(3, 27), (5, 125), (4, 64)])
def test_cube_volume(side_length, expected_volume):
  assert shapes.Cube(side_length).volume() == expected_volume