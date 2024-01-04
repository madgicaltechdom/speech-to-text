<h1 align="center">
    <b>Speech to Text Vakyansh</b> 
<br>
</h1>

## Description

This repository contains a simple FastAPI-based web service for performing speech-to-text (STT) using the transformers library. It supports both Hindi and English languages.

## Instruction
To use this repository, follow these steps:
1. Clone this repository:
- https://github.com/madgicaltechdom/speech-to-text.git
- cd your-repo

2. Install the required dependencies:
- pip install -r requirements.txt
- pip install -r packages.txt
- pip install fastapi
- pip install uvicorn
- pip install pydantic

3. Run the FastAPI app:
- uvicorn app:app --reload

4. Test your API:
- http://127.0.0.1:8000/speech-to-text?language='English' or http://127.0.0.1:8000/speech-to-text?language='Hindi'

## Models Used
- Hindi Language Model:
    - Processor: Harveenchadha/vakyansh-wav2vec2-hindi-him-4200
    - Model: Harveenchadha/vakyansh-wav2vec2-hindi-him-4200

- English Language Model:
    - Processor: Harveenchadha/vakyansh-wav2vec2-indian-english-enm-700
    - Model: Harveenchadha/vakyansh-wav2vec2-indian-english-enm-700


 

