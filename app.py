import pyaudio
import wave
import whisper
import tkinter
valor = 0
def grabar():
    print("grabando")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100,input=True,frames_per_buffer=1024)
    frames= []
    
    while True:
        data = stream.read(1024,exception_on_overflow=False)
        frames.append(data)
        if valor == 10:
            print("hola")
            break
            

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open("myrecording.wav","wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()

def reproducir():
        print("reproduciendo")
        model = whisper.load_model("base")
        result = model.transcribe('myrecording.wav')
        print(result["text"])    
        with open("nuevo.txt","a") as texto:
            texto.write(result["text"])
def salir():
    ventana.destroy()

def parar():
    valor = 10
    print(valor)
    return valor
ventana = tkinter.Tk()
ventana.geometry("400x300")
boton = tkinter.Button(ventana, text="presionar",command=grabar)
boton.pack()
boton1 = tkinter.Button(ventana,bg="blue",text="reproducir audio",command=reproducir)
boton1.pack()
boton3 = tkinter.Button(ventana,text="salir",command=salir)
boton3.pack()
boton4 = tkinter.Button(ventana,text="parar",command=parar())
boton4.pack()
ventana.mainloop()