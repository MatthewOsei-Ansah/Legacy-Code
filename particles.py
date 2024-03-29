import pygame
from support import import_folder


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == 'jump':
            self.frame = import_folder(
                "C:\\Users\\Matthew!\\PycharmProjects\\Platformer2\\character\\dust_particles\\jump")

        if type == 'land':
            self.frame = import_folder(
                "C:\\Users\\Matthew!\\PycharmProjects\\Platformer2\\character\\dust_particles\\land")
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_Rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self,x_shift):
        self.animate()
        self.rect.x += x_shift