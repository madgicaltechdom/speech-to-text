import soundfile as sf
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor,Wav2Vec2ProcessorWithLM
import gradio as gr
import sox
import subprocess
from fastapi import FastAPI, File, UploadFile
# Create FastAPI instance
app = FastAPI()

def read_file_and_process(wav_file, processor):
    filename = wav_file.split('.')[0]
    filename_16k = filename + "16k.wav"
    resampler(wav_file, filename_16k)
    speech, _ = sf.read(wav_file)#filename_16k
    inputs = processor(speech, sampling_rate=16_000, return_tensors="pt", padding=True)
    
    return inputs


def resampler(input_file_path, output_file_path):
    command = (
        f"ffmpeg -hide_banner -loglevel panic -i {input_file_path} -ar 16000 -ac 1 -bits_per_raw_sample 16 -vn "
        f"{output_file_path}"
    )
    subprocess.call(command, shell=True)



def parse_transcription(logits,processor):
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0], skip_special_tokens=True)
    return transcription


def parse(wav_file, language):

    if language == 'Hindi':
        processor = Wav2Vec2Processor.from_pretrained("Harveenchadha/vakyansh-wav2vec2-hindi-him-4200")
        model = Wav2Vec2ForCTC.from_pretrained("Harveenchadha/vakyansh-wav2vec2-hindi-him-4200")
    elif language == 'English':
        processor = Wav2Vec2Processor.from_pretrained("Harveenchadha/vakyansh-wav2vec2-indian-english-enm-700")
        model = Wav2Vec2ForCTC.from_pretrained("Harveenchadha/vakyansh-wav2vec2-indian-english-enm-700")
    

    input_values = read_file_and_process(wav_file, processor)
    with torch.no_grad():
        logits = model(**input_values).logits

    return parse_transcription(logits, processor)

@app.get("/speech-to-text")
def get_transcription(file: UploadFile = File(...), language: str=''):
    data = parse("english.wav", language) # parameter will be file and laguage
    with open("data.txt", "w") as f:
        f.write(data)
    return {"transcription": data}