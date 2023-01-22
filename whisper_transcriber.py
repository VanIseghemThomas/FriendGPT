import whisper
import speech_recognition as sr
import tempfile
import os
import io
from pydub import AudioSegment
from time import perf_counter

class WhisperTranscriber:
    def __init__(self, model, energy=500, dynamic_energy=True, pause=0.8):
        self._model = model
        self._energy = energy
        self._dynamic_energy = dynamic_energy
        self._pause = pause

        self._audio_model = whisper.load_model(self._model)
        self._recognizer = self._create_recognizer(self._energy, self._dynamic_energy, self._pause)

        self._temp_dir = tempfile.mkdtemp()
        self._audio_export = os.path.join(self._temp_dir, "temp.wav")


    def _create_recognizer(self, energy, dynamic_energy, pause):
        r = sr.Recognizer()
        r.energy_threshold = energy
        r.pause_threshold = pause
        r.dynamic_energy_threshold = dynamic_energy

        return r


    def start_transcribing(self, verbose=True, callback=None):
        with sr.Microphone(sample_rate=16000) as source:
            print("---------- Whisper initialized! ----------")
            while True:
                audio = self._recognizer.listen(source)

                start = perf_counter()
                data = io.BytesIO(audio.get_wav_data())
                audio = AudioSegment.from_file(data)
                audio.export(self._audio_export, format="wav")

                result = self._audio_model.transcribe(self._audio_export, language='english')

                if callback:
                    callback(result)

                predicted_text = result["text"]
                duration = perf_counter() - start

                if verbose:
                    print("Prediction: " + predicted_text + " | delay: ", "{:.2f}".format(duration), "s")

        