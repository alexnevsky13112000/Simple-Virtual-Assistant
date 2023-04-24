import vosk
import sys
import sounddevice as sd
import queue
import json

model = vosk.Model("model_small")
sample_rate = 16000
device = 1
q = queue.Queue()


def q_callback(input_data, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(input_data))


def da_listen(callback):
    with sd.RawInputStream(samplerate=sample_rate, blocksize=8000, device=device, dtype='int16',
                           channels=1, callback=q_callback):
        rec = vosk.KaldiRecognizer(model, sample_rate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())['text'])


"""
with sd.RawInputStream(samplerate=sample_rate, blocksize=8000, device=device, dtype='int16',
                       channels=1, callback=q_callback):
    rec = vosk.KaldiRecognizer(model, sample_rate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())
"""