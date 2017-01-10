# Created by: Victoria Le
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
from numpy import random
import sound

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2
        
        self.soul_move_speed = 20.0
        self.left_button_down = False
        self.right_button_down = False
        
        background_position = Vector2(self.center_of_screen_x,
                                      self.center_of_screen_y)
        
        self.background = SpriteNode('./assets/sprites/background.png',
                                     position = background_position, 
                                     parent = self,
                                     size = self.size)
        
        soul_position = Vector2(self.center_of_screen_x,100)
        
        self.soul = SpriteNode('./assets/sprites/ball.png',
                               parent = self,
                               position = soul_position,
                               scale = 0.05)
        
        
        
    def update(self):
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
