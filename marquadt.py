#!/usr/bin/env python

"""
Levenberg-Marquadt method.

"""

import numpy as np
from scipy.linalg import solve

def marqcof(x,y,w,func,a,params={}):
  na = len(a)
  alfa = np.zeros((na,na))
  beta = np.zeros(na)

  # func must return value and Jacobian vector at x


def marqmin(x,y,w,func,a0):
  lam = 0.001
  
  # CALCULATE alpha, beta, chisq

  solve(alfa,beta)
