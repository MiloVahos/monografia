import typing as t
import typing_extensions as te

from pydantic import BaseModel, Field, PositiveInt, PositiveFloat

class ModelInput(BaseModel):
  radius_mean: PositiveFloat
  texture_mean: PositiveFloat
  perimeter_mean: PositiveFloat
  area_mean: PositiveFloat
  smoothness_mean: PositiveFloat
  compactness_mean: PositiveFloat
  concavity_mean: PositiveFloat
  concave_points_mean: PositiveFloat#
  symmetry_mean: PositiveFloat
  fractal_dimension_mean: PositiveFloat
  radius_se: PositiveFloat
  texture_se: PositiveFloat
  perimeter_se: PositiveFloat
  area_se: PositiveFloat
  smoothness_se: PositiveFloat
  compactness_se: PositiveFloat 
  concavity_se: PositiveFloat
  concave_points_se: PositiveFloat#
  symmetry_se: PositiveFloat
  fractal_dimension_se: PositiveFloat 
  radius_worst: PositiveFloat
  texture_worst: PositiveFloat
  perimeter_worst: PositiveFloat
  area_worst: PositiveFloat
  smoothness_worst: PositiveFloat
  compactness_worst: PositiveFloat
  concavity_worst: PositiveFloat
  concave_points_worst: PositiveFloat #
  symmetry_worst: PositiveFloat
  fractal_dimension_worst: PositiveFloat 
