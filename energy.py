#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:22:34 2020

@author: hp
"""


import librosa
import numpy as np
import matplotlib.pyplot as plot
import librosa.display
y, sr = librosa.load('hello.wav')
hop_length = 256
frame_length = 512
size = len(y)

total_energy = np.empty((0,512))
for i in range(0,size,hop_length):
    energy =  sum(abs(y[i:i+frame_length]**2))
    total_energy = np.append(total_energy,[energy])
    #print(total_energy)


plot.subplot(111)
plot.plot(y)
plot.xlabel('time')
plot.ylabel('amplitude')   
