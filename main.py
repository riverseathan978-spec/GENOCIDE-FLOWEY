import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 850, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GENOCIDE FLOWEY")

def load_image(path, size, fallback_color=(255,255,0)):
    # Stub for art: Replace with pygame.image.load(path) when you have assets!
    surf = pygame.Surface(size)
    surf.fill(fallback_color)
    return surf

# Replace below with assets in 'assets/' as you expand!
flowey_sprite = load_image("assets/flowey.png", (90, 104))
lord_flowey_sprite = load_image("assets/lord_flowey.png", (180, 208))
human_soul_sprites = [load_image(f"assets/soul_{i}.png", (30, 40), (i*40,50,200)) for i in range(6)]

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
theme_music_started = False

def draw_text(surface, text, pos, color=(255,255,255), size=36):
    font = pygame.font.Font(None, size)
    txt_surface = font.render(text, True, color)
    surface.blit(txt_surface, pos)

class SceneBase:
    def __init__(self):
        self.next = self
    def process_input(self, events, pressed_keys): pass
    def update(self): pass
    def render(self, screen): pass
    def switch_to_scene(self, next_scene): self.next = next_scene
    def terminate(self): self.switch_to_scene(None)

class FloweyScared(SceneBase):
    def __init__(self): super().__init__(); self.timer = 0
    def update(self):
        self.timer += clock.get_time()
        if self.timer > 2500: self.switch_to_scene(AsgoreObliterated())
    def render(self, screen):
        screen.fill((0,0,0))
        draw_text(screen, "Flowey: You're really going to fight Sans...", (80,150), (200,200,50), 44)
        screen.blit(flowey_sprite, (WIDTH // 2 - 45, 260))

class AsgoreObliterated(SceneBase):
    def __init__(self): super().__init__(); self.timer = 0
    def update(self):
        self.timer += clock.get_time()
        if self.timer > 1400: self.switch_to_scene(FloweySlash())
    def render(self, screen):
        screen.fill((50,0,0))
        draw_text(screen, "ASGORE IS OBLITERATED!", (90,100), (255,255,255), 44)
        draw_text(screen, "Flowey shows up, laughing.", (90,150), (255,250,0), 36)
        screen.blit(flowey_sprite, (WIDTH // 2 - 45, 260))

class FloweySlash(SceneBase):
    def __init__(self): super().__init__(); self.slash_count = 0; self.last_time = pygame.time.get_ticks()
    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.slash_count += 1
                self.last_time = pygame.time.get_ticks()
                if self.slash_count == 5:
                    self.switch_to_scene(LordFloweyTransformation())
    def render(self, screen):
        screen.fill((0,0,0))
        draw_text(screen, f"SLASH FLOWEY! ({self.slash_count}/5)", (200, 80), (255,255,0), 44)
        screen.blit(flowey_sprite, (WIDTH // 2 - 45, HEIGHT // 2 - 52))
        draw_text(screen, "Press SPACE to Slash", (160, 450), (255,0,0), 36)

class LordFloweyTransformation(SceneBase):
    def __init__(self): super().__init__(); self.timer = 0
    def update(self):
        global theme_music_started
        if not theme_music_started:
            # TODO: play theme music (use pygame.mixer.music.load/play)
            theme_music_started = True
        self.timer += clock.get_time()
        if self.timer > 4400: self.switch_to_scene(LordFloweyBattle())
    def render(self, screen):
        screen.fill((0,0,0))
        for i, soul in enumerate(human_soul_sprites):
            x = WIDTH//2 - 90 + i*60
            screen.blit(soul, (x, 100))
        draw_text(screen, "Flowey absorbs the 6 human souls...", (120, 190), (255,255,255), 42)
        draw_text(screen, "Reminded of Chara, Asgore, Toriel.", (120, 220), (200,250,255), 38)
        draw_text(screen, "FILLED WITH DETERMINATION!", (120, 250), (255,60,10), 44)
        screen.blit(lord_flowey_sprite, (WIDTH // 2 - 90, HEIGHT // 2 - 104))
        draw_text(screen, "Darkness behind him...", (190,530), (255,255,255), 32)

class LordFloweyBattle(SceneBase):
    def __init__(self): super().__init__(); self.timer = 0
    def update(self): self.timer += clock.get_time() # TODO: battle attacks
    def render(self, screen):
        screen.fill((0,0,0))
        for i, soul in enumerate(human_soul_sprites):
            x = WIDTH//2 - 90 + i*60
            screen.blit(soul, (x, 60))
        draw_text(screen, "LORD FLOWEY", (WIDTH//2 - 90, 30), (250,80,60), 64)
        screen.blit(lord_flowey_sprite, (WIDTH // 2 - 90, HEIGHT // 2 - 104))
        draw_text(screen, "< EPIC BATTLE THEME PLAYS >", (WIDTH//2 - 180, HEIGHT - 90), (255,140,30), 36)
        draw_text(screen, "TODO: Implement attacks and fight system!", (80,510), (255,255,255), 32)

def run_game(starting_scene):
    active_scene = starting_scene
    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_f4 = event.key == pygame.K_F4 and (event.mod & pygame.KMOD_ALT)
                if alt_f4: quit_attempt = True
            if quit_attempt:
                active_scene.terminate()
                return
            else:
                filtered_events.append(event)
        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render(screen)
        active_scene = active_scene.next
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_game(FloweyScared())
    pygame.quit()
    sys.exit()
