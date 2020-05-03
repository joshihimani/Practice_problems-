import librosa
import numpy 
import librosa.display
y, sr = librosa.load('should.wav')
hop_length = 256
frame_length = 512
size = len(y)
    
energy = numpy.array([
    sum(abs(y[i:i+frame_length]**2))
    for i in range(0, size, hop_length)
])
print(energy.shape)
