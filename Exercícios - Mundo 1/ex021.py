# Faça um programa em Python que abra e reproduza um áudio de um arquivo MP3

import pygame

# Iniciando a biblioteca e passando o audio
pygame.init()
audio = 'audio-me.mp3'  # tente/try 'extra.mp3'

pygame.mixer.music.load(audio)
pygame.mixer.music.play()

# Aguardando o audio ser executado em loop
input()
pygame.event.wait()
