# Created by: Mr. Coxall
# Modified by: Victoria L
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
        
        self.ghosts = []
        self.ghost_attack_rate = 10
        self.ghost_attack_speed = 15.0
        
        self.soul_move_speed = 15.0
        self.left_button_down = False
        self.right_button_down = False
        
        self.scale_size = 0.75
        self.dead = False
        self.score = 0
        self.ghost_touched = False
        
        background_position = Vector2(self.center_of_screen_x,
                                      self.center_of_screen_y)
        
        self.background = SpriteNode('./assets/sprites/background.png',
                                     position = background_position, 
                                     parent = self,
                                     size = self.size)
        
        soul_position = Vector2(self.center_of_screen_x,190)
        
        self.soul = SpriteNode('./assets/sprites/soul.png',
                               parent = self,
                               position = soul_position,
                               scale = 0.06)
        
        left_button_position = Vector2(self.center_of_screen_x - 450,80)
        
        self.left_button = SpriteNode('./assets/sprites/left_button.png',
                                       parent = self,
                                       position = left_button_position,
                                       alpha = 0.5,
                                       scale = self.scale_size)
                                       
        right_button_position = Vector2(self.center_of_screen_x + 450,80)
        
        self.right_button = SpriteNode('./assets/sprites/right_button.png',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.5,
                                       scale = self.scale_size)
        
        self.score_position = Vector2()
        self.score_position.x = 100
        self.score_position.y = self.size_of_screen_y - 50
        self.score_label = LabelNode(text = 'Score: 0',
                                     font = ('Helvetica', 40),
                                     parent = self,
                                     position = self.score_position)
        
    def update(self):
        
        # move soul if button down
        if self.left_button_down == True:
            self.soul.run_action(Action.move_by(-1*self.soul_move_speed, 0.0, 0.1))
            #soul_move = Action.move_by(-1*self.soul_move_speed, 0.0, 0.1)
        
        #self.soul.run_action(soul_move)
        
        if self.right_button_down == True:
            self.soul.run_action(Action.move_by(self.soul_move_speed, 0.0, 0.1))
            #soul_move = Action.move_by(-1*self.soul_move_speed, 0.0, 0.1)
        
        #self.soul.run_action(soul_move)
        
        #add ghost to screen
        ghost_create_chance = random.randint(1,120)
        if ghost_create_chance <= self.ghost_attack_rate:
            self.add_ghosts()
        
        #if ghost is off screen
        for ghost in self.ghosts:
            if ghost.position.y < + 10:
                ghost.remove_from_parent()
                self.ghosts.remove(ghost)
                if self.dead == False:
                    self.score = self.score - 1
        
        #if ghost touch soul
        if len(self.ghosts) > 0:
            for ghost_hit in self.ghosts:
                if ghost_hit.frame.intersects(self.soul.frame):
                    self.soul.remove_from_parent()
                    ghost_hit.remove_from_parent()
                    self.ghosts.remove(ghost_hit)
                    
                    self.dead = True
                    menu_button_position = Vector2()
                    menu_button_position = self.center_of_screen_x,self.center_of_screen_y
                    self.menu_button = SpriteNode('./assets/sprites/menu.png',
                                                  parent = self,
                                                  position = menu_button_position)
        else:
            pass
        
        # update every frame the current score
        self.score_label.text = 'Score: ' + str(self.score)
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        #check if left or right button is down
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True
        
        for ghost in self.ghosts:
            if ghost.frame.contains_point(touch.location):
                self.ghost_touched = True
        
        
        
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if finger is removed then soul would stop moving
        self.left_button_down = False
        self.right_button_down = False
        
        # if finger is touch ghost remove ghost
        for ghost in self.ghosts:
            if self.ghost_touched == True:
                ghost.remove_from_parent()
                self.ghosts.remove(ghost)
                self.score = self.score + 1
                self.ghost_touched = False
        
        # if menu is tap return to main menu scene
        if self.dead == True:
            # if menu button is pressed, go to game scene
            if self.menu_button.frame.contains_point(touch.location):
                self.dismiss_modal_scene()
        
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
        
    def add_ghosts(self):
        
        #create a ghost
        ghost_start_position = Vector2()
        ghost_start_position.x = random.randint(100, self.size_of_screen_x -       100)
        ghost_start_position.y = self.size_of_screen_y + 200
        
        ghost_end_position = Vector2()
        ghost_end_position.x = random.randint(100, self.size_of_screen_x - 100)
        ghost_end_position.y = -100
        
        self.ghost = (SpriteNode('./assets/sprites/ghost.png',
                                       parent = self,
                                       position = ghost_start_position,
                                       scale = 0.06))
        self.ghosts.append(self.ghost)
        
        ghost_move_action = Action.move_to(ghost_end_position.x,
                                           ghost_end_position.y,
                                           self.ghost_attack_speed,
                                           TIMING_SINODIAL)
        
        self.ghosts[len(self.ghosts)-1].run_action(ghost_move_action)
    
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
    
