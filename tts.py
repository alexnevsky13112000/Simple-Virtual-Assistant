import torch
import sounddevice as sd
import time

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'kseniya' # aidar, baya, kseniya, xenia, random
put_accent, put_yo = True, True
device = torch.device('cpu')
text = 'Добрый вечер, Саша!!!'

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)
model.to(device)  # gpu or cpu


def da_speak(what: str):
    audio = model.apply_tts(text=what+"....",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    sd.play(audio, sample_rate)
    time.sleep((len(audio) / sample_rate) + 1)
    sd.stop()

# sd.play(audio, sample_rate)
# Length of synthesized speech len(audio) / sample_rate, len(audio) - numpy array, sr - discrete freq
# time.sleep(len(audio) / sample_rate)
# sd.stop()
# test = "Я вас не расслышала"
# da_speak(test)