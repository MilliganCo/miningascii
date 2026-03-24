import pygame
from world import World
from player import Player
from ascii_renderer import ASCIIRenderer
from ui import UI


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.world = World()
        self.player = Player()
        self.renderer = ASCIIRenderer(screen)
        self.ui = UI(screen)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                # WASD для перемещения
                if event.key == pygame.K_w:
                    self.player.move(0, -1)
                elif event.key == pygame.K_s:
                    self.player.move(0, 1)
                elif event.key == pygame.K_a:
                    self.player.move(-1, 0)
                elif event.key == pygame.K_d:
                    self.player.move(1, 0)
                # Клавиша E для копания/сбора ресурсов
                elif event.key == pygame.K_e:
                    self.player.dig()
                # Номера для выбора ячеек инвентаря (1-9, 0)
                elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                   pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0):
                    key_mapping = {
                        pygame.K_1: 0,
                        pygame.K_2: 1,
                        pygame.K_3: 2,
                        pygame.K_4: 3,
                        pygame.K_5: 4,
                        pygame.K_6: 5,
                        pygame.K_7: 6,
                        pygame.K_8: 7,
                        pygame.K_9: 8,
                        pygame.K_0: 9,
                    }
                    self.player.selected_slot = key_mapping[event.key]
                    print(f"Выбрана ячейка инвентаря {self.player.selected_slot + 1}")

    def update(self):
        self.player.update()
        self.world.update()
        # Обновление монстров, навыков и прочего

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.renderer.render_world(self.world)
        self.renderer.render_player(self.player)
        self.ui.draw()
        pygame.display.flip()
