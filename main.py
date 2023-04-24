import config
import stt
import webbrowser
import tts
import random
import datetime
from fuzzywuzzy import fuzz
from num2t4ru import num2text

print(f'{config.DA_NAME} начала свою работу...')


def da_respond(voice: str):
    print(voice)
    if voice.startswith(config.DA_AlIAS):

        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.DA_CMD_LIST.keys():
            text = "Я вас не расслышала"
            tts.da_speak(text)
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice
    for al in config.DA_AlIAS:
        cmd = cmd.replace(al, '').strip()

    for x in config.DA_TBR:
        cmd = cmd.replace(x, '').strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for key, value in config.DA_CMD_LIST.items():
        for v in value:
            vrt = fuzz.ratio(cmd, v)
            if vrt > rc['percent']:
                rc['cmd'] = key
                rc['percent'] = vrt
    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "и открывать браузер"
        tts.da_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Сейч+ас " + num2text(now.hour) + " " + num2text(now.minute)
        tts.da_speak(text)

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                 'Программист это машина для преобразования кофе в код']

        tts.da_speak(random.choice(jokes))

    elif cmd == 'open_browser':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("https://my.itmo.ru/schedule")


# начать прослушивание команд
stt.da_listen(da_respond)
