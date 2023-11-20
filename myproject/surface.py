from manimlib import *
from typing import Tuple

from manimlib.constants import PI, TAU
import numpy as np


class ConicalSurface(Surface):
    def __init__(
        self,
        axes,
        r_range: Tuple[float, float] = (-np.sqrt(2)*3, np.sqrt(2)*3),
        theta_range: Tuple[float, float] = (0, TAU),

        phi=PI/4,

        **kwargs,
    ):
        self.theta_range = theta_range
        self.phi = phi
        self.axes = axes
        super().__init__(
            u_range=r_range,
            v_range=self.theta_range,
            **kwargs
        )

    def uv_func(self, r: float, theta: float) -> np.ndarray:
        x = r*np.cos(theta)*np.sin(self.phi)
        y = r*np.sin(theta)*np.sin(self.phi)
        z = r*np.cos(self.phi)
        re = self.axes.c2p(x, y, z)
        return re

    def set_theta_range(self, tuple):
        self.theta_range = tuple
        self.__init__(axes=self.axes, theta_range=self.theta_range)
        return self


class SphereInAxes(Sphere):
    def __init__(self,axes:ThreeDAxes, **kwargs):
        self.axes = axes        
        super().__init__( **kwargs)

    def uv_func(self, u: float, v: float) -> np.ndarray:
        re = super().uv_func(u, v)
        return self.axes.c2p(*re)
    
class TorusInAxes(Torus):
    def __init__(self,axes:ThreeDAxes,**kwargs):
        self.axes=axes
        super().__init__(**kwargs)
    def uv_func(self, u: float, v: float) -> np.ndarray:
        re = super().uv_func(u, v)
        return self.axes.c2p(*re)
        