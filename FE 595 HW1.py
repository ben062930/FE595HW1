#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:15:50 2020

@author: tianyiyang
"""


import numpy as np
import matplotlib.pyplot as plt
a = np.arange(0, 2*np.pi, 0.001)
plt.plot(a, np.cos(a), color = "green", label = "SIN")
plt.plot(a, np.sin(a), color = "yellow", label = "COS")
# plt.show()
plt.plot(a, np.tan(a), label = "TAN", color = "red")
plt.ylim(-10,10)

plt.show()
