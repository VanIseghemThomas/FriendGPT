# This script will record the audio and send it to the websocket server.

import speech_recognition as sr
import websockets
import asyncio

r = sr.Recognizer()
r.energy_threshold = 500
r.pause_threshold = 0.8
r.dynamic_energy_threshold = False

# First open a websocket connection to the server at localhost:8000
async def connect_whisper():
    async with websockets.connect("ws://localhost:8000/whisper/transcribe") as websocket:
        with sr.Microphone(sample_rate=16000) as source:
            print("Ready! Speak into the microphone")
            while True:
                audio = r.listen(source)
                data = audio.get_wav_data()
                print("Sending audio segment")
                await websocket.send(data)

asyncio.get_event_loop().run_until_complete(connect_whisper())

