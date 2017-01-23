# Created by: Mr. Coxall
# Modified by: Victoria Le
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
from game_scene import *
from help_scene import *
class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        #add background color
        self.background = SpriteNode('./assets/sprites/background.png',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
        
        game_title_position = self.size/2
        game_title_position.y = game_title_position.y + 200
        self.game_title = SpriteNode('./assets/sprites/game_title.png',
                                     position = game_title_position, 
                                     parent = self, 
                                     size = self.size)
        
        
        self.start_button = SpriteNode('./assets/sprites/start.png',
                                       parent = self,
                                       position = self.size/2)
                                       
        menu_button_position = self.size/2
        menu_button_position.y = menu_button_position.y - 200
        self.menu_button = SpriteNode('./assets/sprites/menu.png',
                                       parent = self,
                                       position = menu_button_position)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
        
        if self.menu_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
        
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
    
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
