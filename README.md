# **FriendGPT:** The AI based friend

This project started of as a joke for myself, but also as an excuse to build something with the new emerging NLP technologies. The idea is to use an ASR to convert spoken audio -> text. After the text is generated, it is fed into another model that generates a response.

The plan as it stands, is to use Whisper for the ASR and GPT3 for the actual responses. This is just the language processing side of things. I see potential to also implement some kind of text-to-audio model that enables you to have actual conversations.

## Usage

### Whisper ASR

For now you can use just use the Whisper model by OpenAI to do the ASR. This can be done in 2 ways. Either you install all dependecies:

```
apt update && apt install -y ffmpeg portaudio19-dev python3-pip git
pip install -r requirements.txt
```
and use `whisper_cli.py` to do use the Whisper ASR as a standalone application.

Or you can use the Dockerfile to build a Whisper server container and connect to it using the client. This way you don't have to install any dependencies instead of the one's the client needs (SpeechRecognition).

After building the container you can use `docker run -it -p 8000:8000 <image-name>` to run the server. Along that you can spin up the client using `python whisper_client.py`. 
