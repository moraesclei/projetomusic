# Primeiro Projeto em python a qual conseguimos importar um áudio em mp3 e executá-l0
# o codigo a seguir faz tocar uma música a partir dos comandos abaixo:
# neste caso precisamos instalar primeiro o pacote pygame e só depois realizar o import.
import pygame
pygame.init()

pygame.mixer.music.load('hillsong.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
