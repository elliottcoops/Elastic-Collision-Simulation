import ui
import block
import random

def run():
    window = ui.window(1500,700,"Collision display")

    small_block = block.block(10,get_random_colour(), 0)
    window.add_block(small_block)

    large_block = block.block(100000,get_random_colour(), -0.05)
    window.add_block(large_block)

    window.setup_display()
    window.display()

def get_random_colour():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))