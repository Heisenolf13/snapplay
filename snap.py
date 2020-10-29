import pyaudio
import wave
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import pyautogui
import webbrowser

#so you don't really need to know what the variables right below does but they are the best settings for recording sounds
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 1 # its kinda obvious what this does
WAVE_OUTPUT_FILENAME = "output.wav" # and this


while True:
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()# we recorded the sound and with the 'wf' below, we will turn it into a .wav file
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()# .wav file has been created

    Fs, data1 = read(WAVE_OUTPUT_FILENAME)# we read the .wav file

    data1 = data1[:,0]

    # print("Sampling frequency is", Fs)
    # print(data)
    cap = 20000

    for i in data1:
        if i > cap:# so if any intensity of the audio is louder than cap(milihertz i geuess), it does the code below 
            # webbrowser.open("www.youtube.com")
            pyautogui.press("playpause")
            break

    # and this part is for visualizing the waves
    # plt.figure()
    # plt.plot(data)
    # plt.xlabel("Sample index")
    # plt.ylabel("Amplitude")
    # plt.title("Waveform of test audio")
    # plt.show()
