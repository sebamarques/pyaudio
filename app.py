import pyaudio
import wave
import whisper

while True:
    print("a = grabar audio\n b= transcribir audio\nc=terminar programa")
    x = input("")
    if x == "a":
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100,input=True,frames_per_buffer=1024)
        frames= []
        try:
            while True:
                data = stream.read(1024,exception_on_overflow=False)
                frames.append(data)
        except KeyboardInterrupt:
            pass

        stream.stop_stream()
        stream.close()
        audio.terminate()

        sound_file = wave.open("myrecording.wav","wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(frames))
        sound_file.close()
    if x == "b": 
        model = whisper.load_model("base")
        result = model.transcribe('myrecording.wav')
        print(result["text"])    
        with open("nuevo.txt","a") as texto:
            texto.write(result["text"])
    elif x == "c":
        break
        
