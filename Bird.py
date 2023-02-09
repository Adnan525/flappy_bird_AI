from main import BIRD_IMGS

class Bird:
    IMGS = BIRD_IMGS
    # how much the bird will tilt when going up and down
    MAX_ROTATION = 25
    # how much will rotate in each frame
    ROT_VEL = 20
    # how many frames to show each image
    # will control how fast the bird will be flapping its wings
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0 # base position
        self.tick_count = 0 # keep track of when we last jumped
        self.vel = 0
        self.height = self.y
        self.img_count = 0 # keep track of which image we are shwoing
        self.img = self.IMGS[0] # base image

    def jump(self):
        # pygame window has top left as origin
        # going down is positive
        # goiung up is negative
        self.vel = -10.5
        # to check when we will check direction
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        # for downward acceleration
        # self.tick_count = time
        # 
        d = self.vel*self.tick_count + 0.5*self.tick_count**2

        # terminal velocity
        if d >= 16:
            d = 16

        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        # loop through the 3 images
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # if bird is nose diving, don't flap wings
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect