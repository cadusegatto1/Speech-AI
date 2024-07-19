This repository provides basic examples for performing Speech Recognition in Python using the Google Speech Recognition Engine. It includes code for recognizing speech from both microphones and audio files, as well as handling long audio files by breaking them into smaller chunks.


## Getting Started:

### 🔧 Features

Microphone Input: Recognizes speech from live audio.
Audio File Input: Processes speech from local audio files.
Long Audio File Handling: Splits long audio files into chunks for processing.

```python
# Clone this repository
$ git clone https://github.com/cadusegatto1/Speech-AI

# Go into the repository
$ cd Speech-AI
```


## Install dependencies:

### Linux users  
----------

```
$ pip3 install pydub
$ pip3 install PyAudio
$ pip3 install SpeechRecognition
```

### Window users
-----------

```python
$ pip install pydub
$ pip install PyAudio
$ pip install SpeechRecognition
```

### Archives & Functions

app.py: Speech recognition from microphone.
To run the Example do the following

```python
$ python app.py 
    Adjusting noise 
    Recording for 5 seconds
    Done recording
    Recognizing the text
    Decoded Text : Python is awesome
```

app_audio.py: Speech recognition from audio file.
```bash
$ python3 app_audio.py 
    Done recording
    Recognizing the text
    Decoded Text : python programming is the best of all by Jordan
```

long_audio.py: Processing long audio files in chunks.
```bash 
$ python3 app_audio.py 
    Done recording
    Recognizing the text
    Decoded Text : python programming is the best of all by Jordan
```
