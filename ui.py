import pygame
import numpy as np

class window:

    def __init__(self,width, height, caption="My window"):

        self.display = None

        self.width = width
        self.height = height
        self.caption = caption

        self.X_start, self.X_end = (self.width // 10, 3 * self.height // 4), (self.width, 3 *(self.height) // 4)
        self.Y_start, self.Y_end = (self.width // 10, 0), (self.width // 10, self.height)

        self.blocks = []
        self.block_start_coords = [(self.width // 4, self.X_start[1]), (self.width // 3, self.X_start[1])]

        self.collisions = 0

    def add_block(self, block):
        if len(self.blocks) < 2:
            block.set_coords(self.block_start_coords[len(self.blocks)][0], self.block_start_coords[len(self.blocks)][1] - block.get_dimensions()[1])
            block.set_kinetic_energy()
            block.set_momentum()
            self.blocks.append(block)

    def add_blocks(self):
        self.blocks.sort(key = lambda block: block.mass) # lambda argument : expression // simple nameless function for one time use
        index = 0
        for block in self.blocks:
            #Always put the smaller block on the left and the larger on the right
            block_width, block_height = block.get_dimensions()
            block_x, block_y = block.get_coords()
            pygame.draw.rect(self.display, block.colour, pygame.Rect(block_x, block_y, block_width, block_height)) 
            block.set_coords(block_x, block_y)
            index += 1

    def move_blocks(self):
        
        for block in self.blocks:
            if block.x >= self.Y_start[0]:
                block.move()
            else:
                block.speed *= -1
                block.move()
                self.collisions += 1            

    def check_collision(self):
        # Assuming perfectly elastic collisions with the blocks
        # We can assume that both p and ke are both conserved
        # ie m1v1 + m2v2 = m1v1' + m2v2' and 
        # 0.5 * m1 * v1^2 + 0.5 * m2 * v2^2 = 0.5 * m1 * v1'^2 + 0.5 * m2 * v2'^2
        if self.blocks[0].x + self.blocks[0].get_dimensions()[0] >= self.blocks[1].x and self.blocks[0].x <= self.blocks[1].x + self.blocks[1].get_dimensions()[0]:

            total_energy = self.blocks[0].get_kinetic_energy() + self.blocks[1].get_kinetic_energy()
            total_momentum = self.blocks[1].speed * self.blocks[1].mass + self.blocks[0].speed * self.blocks[0].mass
    
            m_1, m_2 = self.blocks[0].mass, self.blocks[1].mass
            v_1_initial, v_2_initial = self.blocks[0].speed, self.blocks[1].speed
            v1_final = (m_1 * v_1_initial - m_2 * v_1_initial + 2 * m_2 * v_2_initial) / (m_1 + m_2)
            self.blocks[0].speed = v1_final

            v2_final = (total_momentum - (self.blocks[0].speed * self.blocks[0].mass)) / self.blocks[1].mass
            self.blocks[1].speed = v2_final

            self.blocks[0].momentum = self.blocks[0].speed * self.blocks[0].mass
            self.blocks[1].momentum = self.blocks[1].speed * self.blocks[1].mass

            self.blocks[0].set_kinetic_energy()
            self.blocks[1].set_kinetic_energy()

            self.collisions += 1


    def setup_display_text(self):

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f'Collisions: {self.collisions}', True, (13,45,33), (2,23,222))

        textRect = text.get_rect()
        textRect.center = (self.width - textRect.width, textRect.height)

        self.display.blit(text, textRect)


    def setup_display(self):

        pygame.init()
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

        # Draw blocks
        self.add_blocks()

        # Get user to start simulation
        running = True
        started = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
            self.display.fill((0, 0, 0)) 

            # Draw text on screen
            self.setup_display_text()
            # Draw x axis
            pygame.draw.line(self.display, (255,255,255),self.X_start, self.X_end) 
            # Draw y axis
            pygame.draw.line(self.display, (255,255,255), self.Y_start, self.Y_end)
            #Move the blocks and draw again
            self.move_blocks()
            self.check_collision()
            self.add_blocks()   
            
            pygame.display.update()

        pygame.quit()
    

    




        




        
