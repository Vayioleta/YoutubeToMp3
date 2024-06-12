import sys
import os
from pytube import YouTube
from moviepy.editor import *

def obtener_titulo_video(url):
    yt = YouTube(url)
    return yt.title

def limpiar_nombre(nombre):
    caracteres_no_validos = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for caracter in caracteres_no_validos:
        nombre = nombre.replace(caracter, '_')
    return nombre

def descargar_youtube_mp3(url):
    # Obtener el título del video
    titulo_video = obtener_titulo_video(url)
    nombre_archivo = limpiar_nombre(titulo_video) + ".mp3"

    try:
        # Descargar el video de YouTube
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        video.download(filename='temp.mp4')

        # Convertir el video a MP3
        video_clip = AudioFileClip('temp.mp4')
        video_clip.write_audiofile(nombre_archivo)

        # Eliminar el archivo de video temporal
        os.remove('temp.mp4')

        return nombre_archivo
    except Exception as e:
        print("Error al descargar el video:", e)
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL de YouTube>")
        sys.exit(1)

    url = sys.argv[1]

    nombre_archivo = descargar_youtube_mp3(url)
    if nombre_archivo:
        print("La canción se ha descargado y guardado como", nombre_archivo)
    else:
        print("No se pudo descargar la canción. Por favor, verifica la URL del video de YouTube.")
