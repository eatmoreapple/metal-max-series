import pygame


class Character(pygame.sprite.Sprite):
    interval = 32
    max_interval = interval * 3
    x = y = interval
    down = 0
    left = 1
    right = 2
    up = 3
    speed = 10
    default_area = [0, 0, interval, interval]

    def __init__(self, image_path, area=None):
        super(Character, self).__init__()
        self.source = pygame.image.load(image_path).convert_alpha()
        self.surface = pygame.Surface((self.x, self.y))
        self.dest = [0, 0]
        self.area = area or self.default_area
        self.image = self.surface
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs):
        """
        实现抽象的update方法
        :param args:
        :param kwargs:
        :return:
        """
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.move(self.right)
            self.rect.left += self.speed
        elif pressed[pygame.K_UP]:
            self.move(self.up)
            self.rect.top -= self.speed
        elif pressed[pygame.K_LEFT]:
            self.move(self.left)
            self.rect.left -= self.speed
        elif pressed[pygame.K_DOWN]:
            self.move(self.down)
            self.rect.bottom += self.speed

        self.surface.blit(self.source, self.dest, self.area)

        super(Character, self).update(*args, **kwargs)

    def get_last_direction(self):
        """
        获取上次的方向
        :return:
        """
        return self.area[1] / self.interval

    def move(self, direction):
        """
        根据方向移动
        实则更新area
        :param direction:
        :return:
        """
        # 判断上次的方向是不是和当前的方向一致
        last_direction = self.get_last_direction()
        # 如果不一致, 则重新设置方向
        if last_direction != direction:
            self.area[0] = 0
        else:
            # 如果一致, 则更新方向
            value = self.area[0] + self.interval
            self.area[0] = value if value <= self.max_interval else 0
        self.area[1] = direction * self.interval
        self.area[2], self.area[3] = self.area[0] + self.interval, self.area[1] + self.interval
