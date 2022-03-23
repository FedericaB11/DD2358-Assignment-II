#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pytest
import math 

# DFT
def DFT(xr, xi, N):
    Xr, Xi = [], []
    for k in range(N):
      Xr_o, Xi_o = 0, 0
      for n in range(N):
        w = - float(n) * k * 2*np.pi/N
        Xr_o += xr[n] * np.cos(w) + xi[n] * np.sin(w)
        Xi_o += xr[n] * np.sin(w) + xi[n] * np.cos(w)
      Xr.append(Xr_o)
      Xi.append(Xi_o)
    return Xr, Xi

# Optimized DFT
def DFT_impr(x, N):
    x = np.asarray(x, dtype=float)
    n = np.arange(N)
    k = n.reshape((N,1))
    w = - n * k * 2*np.pi/N
    W = np.cos(w) - 1j * np.sin(w)
    return np.matmul(W, x)

N = 2
x = np.ones((N,1))
xr = np.ones((N,1))
xi = np.zeros((N,1))

# unit test 
def test_DFT():
    assert np.around(np.sum(DFT(xr, xi, N)), decimals=9) == N

def test_DFT_impr():
    assert np.around(np.sum(DFT_impr(x, N)), decimals=9) == N
