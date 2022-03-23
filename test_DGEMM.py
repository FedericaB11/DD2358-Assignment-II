#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import time
from timeit import default_timer as timer
from array import *
import numpy as np 


def DGEMM_list(N):

    A = [[1.0]*N for x in range(N)]
    B = [[2.0]*N for x in range(N)]
    C = [[0.0]*N for x in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C

def DGEMM_arr(N):
    A = list(range(N))
    B = list(range(N))
    C = list(range(N))
    for i in range(N):
        A[i] = [None] * N
        B[i] = [None] * N
        C[i] = [None] * N
        for j in range(N):
            A[i][j] = 1.0
            B[i][j] = 2.0
            C[i][j] = 0.0

    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C

def DGEMM_nump_arr(N):
    A = np.ones((N,N))
    B = np.ones((N,N))*2
    C = np.zeros((N,N))
    C = np.dot(A, B.T) + C
    return C

def test_DGEMM_list():
    assert np.sum(DGEMM_list(N=10)) == 2000

def test_DGEMM_arr():
    assert np.sum(DGEMM_arr(N=10)) == 2000

def test_DGEMM_nump():
    assert np.sum(DGEMM_nump_arr(N=10)) == 2000


    
    
