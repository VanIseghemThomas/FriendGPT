import argparse
import whisper_transcriber as wt

parser = argparse.ArgumentParser( formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--model", default="base", help="Model to use", choices=["tiny", "base", "small", "medium", "large"])
parser.add_argument("--energy", default=500, help="Energy level for mic to detect", type=int)
parser.add_argument("--dynamic_energy", default=False, help="Flag to enable dynamic energy", type=bool)
parser.add_argument("--pause", default=0.8, help="Minimum length of silence (sec) that will register as the end of a phrase", type=float)
args = parser.parse_args()

def callback(result):
    # In the future, this callback will be used to do something with the result
    # For now, we just print it
    print("Prediction: " + result["text"] + " [ called back ]")
            
transcriber = wt.WhisperTranscriber(args.model, args.energy, args.dynamic_energy, args.pause)
transcriber.start_transcribing(callback=callback)