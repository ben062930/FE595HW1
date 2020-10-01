#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:15:50 2020

@author: tianyiyang
"""


import numpy as np
import matplotlib.pyplot as plt
a = np.arange(0, 2*np.pi, 0.001)
plt.plot(a, np.cos(a))
plt.plot(a, np.sin(a))
plt.show()
