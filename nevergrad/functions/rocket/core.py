# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
# Based on a discussion at Dagstuhl's seminar on Computational Intelligence in Games with:
# - Dan Ashlock
# - Chiara Sironi
# - Guenter Rudolph
# - Jialin Liu

import numpy as np
from nevergrad.parametrization import parameter as p
from ..base import ExperimentFunction
from .rocket import rocket as rocket

class Rocket(ExperimentFunction):

    def __init__(self) -> None:
        super().__init__(self._simulate_rocket, p.Array(shape=(25,)))
        self.register_initialization()
        self.order = np.arange(0, self.dimension)
        self.x = self.parametrization.random_state.normal(size=self.dimension)
        self.y = self.parametrization.random_state.normal(size=self.dimension)

    def _simulate_rocket(self, x: np.ndarray) -> float:
        return rocket(x)

