import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("게임 시작 화면")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# 폰트
font = pygame.font.SysFont(None, 40)

# 버튼 클래스
class Button:
    def __init__(self, text, x, y, w, h, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = font.render(text, True, BLACK)
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect)
        screen.blit(self.text, (self.rect.x + 20, self.rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

# 콜백 함수
def start_game():
    print("게임 시작!")

def open_options():
    print("옵션 열림!")

def quit_game():
    print("게임 종료!")
    pygame.quit()
    sys.exit()

# 버튼 생성
buttons = [
    Button("Start Game", 220, 150, 200, 50, start_game),
    Button("Options", 220, 230, 200, 50, open_options),
    Button("Quit", 220, 310, 200, 50, quit_game),
]

# 메인 루프
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons:
            button.handle_event(event)

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

pygame.quit()
