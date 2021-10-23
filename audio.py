
from scipy.io import wavfile
from scipy.fftpack import fft
from pytube import YouTube
import matplotlib.pyplot as plt
import numpy as np
import os, math

frameRate = 15
SILENTTHRESHOLD = .03
blocks = []

def getMaxVolume(s):
    maxv = float(np.max(s))
    minv = float(np.min(s))
    return max(maxv,-minv)

def downloadFile(url):
    name = YouTube(url).streams.first().download()
    newname = name.replace(' ','')
    os.rename(name,newname)
    return newname

sampleRate, data = wavfile.read('./samples/audio_only.wav', 'r')

# this is the length of the clip
length = len(data) / sampleRate

# this is the domain for the time
domain = np.array(range(0, len(data))) / length

# get the first channel of audio
first_channel = data.T[0] 

step_rate = int(sampleRate / frameRate)

c = fft(first_channel)

next = np.abs(c)

n = fft(next)

plt.plot(np.abs(n))
plt.plot(np.abs(c))
plt.show()

# ranger = np.array(range(0, len(first_channel))) / length
# plt.plot(ranger[0:2000], c[0:2000])
# plt.show()

# for i in range(1, len(data), step_rate):
#   start = i
#   end = i + step_rate - 1

#   if (end > len(data)):
#     break

#   audio = first_channel[start:end]
#   maxVolume = getMaxVolume(audio)
#   c = fft(audio)

#   info = {
#     "start": start,
#     "end": end,
#     "silent": False,
#     "volume": maxVolume,
#     "audio": audio,
#     "fft": c
#   }

#   if maxVolume < SILENTTHRESHOLD:
#     info['silent'] = True

#   blocks.append(info)


# for i in range(len(blocks)):
#   block = blocks[i]

#   if (block["silent"] == False):
#     audio_block = block['fft']
#     ranger = np.array(range(0, len(audio_block))) / length
#     condition = audio_block < 2000

#     plt.figure(figsize = [10,5])
#     plt.plot( ranger, np.abs(audio_block))
#     plt.show()
#     break


# print(blocks[0])
# plt.plot(time[0:200], first_channel[0:200])
# plt.xlabel('time (seconds)')
# plt.ylabel('Pressure')
# plt.show()

# thing = block['fft']
# print(type(thing))
# print(len(thing))

# time_block = len(thing)
# time_range = np.array(range(0, len(thing))) / time_block

# print('this is the new testing')
# print(time_block, len(time_range))

# plt.plot( time_range, np.abs(thing))
# plt.show()

#get the first channel of the soundtrack
# first_channel = data.T[0] 

# #get the max value in the array for normalizing
# channel_max = 0
# for number in first_channel:
#   if channel_max < abs(number):
#     channel_max = abs(number)

# #normalize the data to -1 to 1
# normalized = [(number / channel_max) for number in first_channel]

# audioSampleCount = data.shape[0]
# maxAudioVolume = getMaxVolume(data)

# samplesPerFrame = sampleRate/frameRate
# audioFrameCount = int(math.ceil(audioSampleCount/samplesPerFrame))
# hasLoudAudio = np.zeros((audioFrameCount))

# for i in range(audioFrameCount):
#     start = int(i * samplesPerFrame)
#     end = min(int((i+1)*samplesPerFrame),audioSampleCount)
#     audiochunks = data[start:end]
    
#     maxchunksVolume = float(getMaxVolume(audiochunks))/maxAudioVolume

#     info = {
#       "start": start,
#       "end": end,
#       "silent": False,
#       "volume": maxchunksVolume,
#       "audio": audiochunks
#     }
    
#     if maxchunksVolume < SILENTTHRESHOLD:
#       info['silent'] = True

#     blocks.append(info)
    
# print(blocks[1]["audio"])
# print(len(blocks[1]["audio"]))



# # calculate fourier transform (complex numbers list)
# fft_result = fft(blocks[1]["audio"]) 

# # you only need half of the fft list (real signal symmetry)
# d = len(fft_result) // 2 

# fig, (plt1, plt2) = plt.subplots(2)

# fig.suptitle('Two things')

# #get the xlabel
# k = np.arange(len(data))
# T = len(data)/sampleRate
# frqLabel = k/T

# plt.xlabel(frqLabel)  

#plot the fft spectrum




