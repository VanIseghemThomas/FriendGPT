# Since enabling docker support for microphones is a bit of a pain,
# it is easier to run a whisper server in a docker container and send audio to it.
# This is the server that will be used to transcribe audio.
# 
# The server will be a fastapi websocket server

import fastapi
from fastapi import WebSocket, WebSocketDisconnect
import whisper_transcriber as wt

app = fastapi.FastAPI()
transcriber = wt.WhisperTranscriber("base")

# This is the websocket endpoint that will be used to send audio to the server
@app.websocket("/whisper/transcribe")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            # We will need to save it to a temporary file and then transcribe it
            # We will then send the result back to the client
            # For now, we will just print the result
            prediction, duration = transcriber.transcribe(data)
            print(transcriber.format_output(prediction, duration))
            
    except WebSocketDisconnect:
        print("Client disconnected")