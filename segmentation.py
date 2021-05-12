#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:50:30 2021

@author: hp
"""

import librosa
y, sr = librosa.load('should.wav') # load the audio data

n = len(y)
print("The sampling rate is: ", sr)
print("The number of samples: ", n)

frame_rate = input("Enter the frame rate: ")
frame_rate = int(frame_rate)

H = n / frame_rate 
hop_length = int(H)
print("The hop length for the samples is: ", hop_length)

window_sec = input("Enter the duration for window: ")
window_size = float(window_sec) * sr
frame_length = int(window_size)
print("The frame length for the samples is: ", frame_length)

import librosa
frames = librosa.util.frame(y, frame_length, hop_length, axis=0)
#print(frames)
print("Shape of the frames",frames.shape)

import numpy as np
total_energy = np.empty((0,frame_length))
for i in range(0,n,hop_length):
    energy =  ((1/frame_length)*sum(abs(y[i:i+frame_length]**2))) # compute the energy
    total_energy = np.append(total_energy,[energy])
#print("total energy :", total_energy)
print(total_energy.shape)

import matplotlib.pyplot as plot
plot.subplot(211)
plot.plot(total_energy)
plot.xlabel('time')
plot.ylabel('amplitude')    

from statistics import mean    
threshold = mean(total_energy)  
#print(threshold) 
i=0 
for x in total_energy:
    if x > threshold:
        print("Speech signal")
        #i=i+1  
    else:
        print("N")
        i=i+1
        
 














