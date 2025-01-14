'''Copyright 2021, Printzios Lampros, All rights reserved.'''

import tkinter as tk
import math as m
import random as r
import pygame
import os
from PIL import Image, ImageTk

class balloons_game():
    def __init__(self, root):
        pygame.init()
        self.root = root
        self.root.geometry("+0+0")
        self.root.resizable(False, False)
        self.root.title("Balloons Game")
        self.root.iconphoto(True, tk.PhotoImage(file = os.getcwd() + "/Game_Pictures/balloons_game_icon.png"))
        # self.root.iconbitmap(os.getcwd() + "/Game_Pictures/" + "balloons_game_icon.ico")
        self.root_width = self.root.winfo_screenwidth() * 7 / 10
        self.root_height = self.root.winfo_screenheight() * 7 / 10
        self.background = tk.Canvas(self.root, width = self.root_width, height = self.root_height, bg = "yellow")
        self.background.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.instructions_text = [["\t\t\t\t\t\tΕίναι παιχνίδι ενός παίκτη, αν και μπορεί πολύ εύκολα να χρησιμοποιηθεί για\n\
                                            διαγωνισμό μεταξύ πολλών παικτών. Ο στόχος είναι να πετύχεις όσο το δυνατόν\n\
                                            περισσότερα μπαλόνια του σωστού χρώματος (το οποίο αλλάζει κάθε λίγα δευτερόλεπτα)\n\
                                            και να συγκεντρώσεις έτσι το μεγαλύτερο δυνατό σκορ. Το παιχνίδι αποτελείται από\n\
                                            τρία επίπεδα δυσκολίας (easy, medium και hard, με 2, 4 και 6 χρώματα μπαλονιών\n\
                                            αντίστοιχα) και τρεις χρονικές διάρκειες παιχνιδιού (1, 2 και 3 λεπτά). Κερδίζεις\n\
                                            πόντους πετυχαίνοντας με αριστερό κλικ τα μπαλόνια του σωστού χρώματος, ενώ χάνεις\n\
                                            πόντους αν πετύχεις μπαλόνι λάθους χρώματος ή πατήσεις σε άλλο μέρος του χώρου\n\
                                            παιχνιδιού όπου δεν υπάρχει μπαλόνι (τα απρόσεχτα και άσκοπα κλικ τιμωρούνται).\n\
                                            Όσο μικρότερο και γρηγορότερο είναι το μπαλόνι τόσο περισσότερους πόντους λαμβάνεις\n\
                                            σε περίπτωση σωστού στόχου, ενώ σε περίπτωση λάθος στόχου χάνεις πόντους με την\n\
                                            αντίστροφη λογική (δηλαδή καλύτερα να την πάθεις με ένα μικρό και γρήγορο μπαλόνι\n\
                                            από ό,τι με ένα μεγάλο και αργό). Κατά τη διάρκεια του παιχνιδιού μπορείς με δεξί\n\
                                            κλικ να κάνεις παύση και να επιλέξεις μετά αν θα συνεχίσεις, θα επανεκκινήσεις\n\
                                            την πίστα ή θα ξεκινήσεις καινούρια. Τέλος, μπορείς να αλλάξεις αρκετές από τις\n\
                                            προκαθορισμένες παραμέτρους του παιχνιδιού πηγαίνοντας στα \"Game settings\" του\n\
                                            μενού \"Options\".", "Καλή επιτυχία!!!"],\
                                  ["\t\t\t\t\t\tThis is a single player game, although it can easily be used for multiplayer\n\
                                            competition. The goal is to hit as many balloons of the correct color (which\n\
                                            changes every few seconds) as possible and thus accumulate the highest possible\n\
                                            score. The game consists of three levels of difficulty (easy, medium and hard,\n\
                                            with 2, 4 and 6 colors of balloons respectively) and three time durations (1, 2\n\
                                            and 3 minutes). You earn points by left-clicking balloons of the correct color,\n\
                                            while you lose points if you hit a wrong-colored balloon or click on another part\n\
                                            of the playing area where there is no balloon (careless and pointless clicks are\n\
                                            penalized). The smaller and faster the balloon, the more points you get in case of\n\
                                            a correct aim, while in case of a wrong aim you lose points in the reverse logic\n\
                                            (i.e. it is better to make a mistake with a small and fast balloon than with a big\n\
                                            and slow one). During the game you can right-click to pause and then choose whether\n\
                                            to resume the game, restart it, or start a new one. Finally, you can change several\n\
                                            of the default game parameters by going to \"Game settings\" in the \"Options\" menu.", "Good luck!!!"]]
        self.instructions_language = "english"
        self.instructions_languages_matrix = ["greek", "english"]
        self.game_level = "easy"
        self.game_time = "1 min"
        self.music_control = "ON"
        self.sound_control = "ON"
        self.window_size_control = "medium"
        self.window_sizes_control_matrix = ["small", "medium", "large"]
        self.balloons_sizes_matrix = [[40], [40, 80], [20, 50, 80], [20, 40, 60, 80], [20, 40, 60, 80, 100]]
        self.speeds_matrix = [5, 10, 20, 30, 40, 50]
        self.balloons_angles_offset_matrix = [0, 15, 30, 45, 60, 75, 90]
        self.target_color_change_freq_matrix = [5, 10, 15, 20, 30, 60, "?"]
        self.game_levels_matrix = ["easy", "medium", "hard"]
        self.game_times_matrix = ["1 min", "2 min", "3 min"]
        self.set_default_settings()
        self.play_sound("main_menu_sound", "music")
        self.main_menu()
    def main_menu(self, event = None):
        self.background.unbind("<Motion>")
        try:
            self.pause_menu.destroy()
            self.play_sound("main_menu_sound", "music")
        except AttributeError:
            pass
        self.destroy_menu()
        self.copyright_claim = menu_label(self.background, "Created by Printzios Lampros.", "Arial {} bold".format(self.adjust_sizes([10, 12, 14])), "black", self.root_width - self.adjust_sizes([100, 120, 140]), self.root_height - 20)
        self.options_button = menu_button(self.background, "Options", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2, self.root_height / 4 - 30, self.options_menu).button
        self.instructions_button = menu_button(self.background, "Instructions", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2, 2 * self.root_height / 4 - 30, self.instructions_menu).button
        self.new_game_button = menu_button(self.background, "New game", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2, 3 * self.root_height / 4 - 30, self.new_game_menu).button    
    def options_menu(self, event = None):
        if self.min_speed <= self.max_speed:
            self.destroy_menu()
            self.menu_name = "options_menu"
            self.music_label = menu_label(self.background, "Music:", "Arial {} bold".format(self.adjust_sizes([35, 40, 45])), "black", self.root_width / 2 - self.adjust_sizes([50, 60, 70]), self.root_height / 6 - 30)
            self.music_control_button = menu_button(self.background, self.music_control, "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2 + self.adjust_sizes([80, 90, 100]), self.root_height / 6 - 30, self.define_game_options).button
            self.sound_label = menu_label(self.background, "Sound:", "Arial {} bold".format(self.adjust_sizes([35, 40, 45])), "black", self.root_width / 2 - self.adjust_sizes([53, 63, 73]), 2 * self.root_height / 6 - 30)
            self.sound_control_button = menu_button(self.background, self.sound_control, "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2 + self.adjust_sizes([83, 93, 103]), 2 * self.root_height / 6 - 30, self.define_game_options).button
            self.window_size_label = menu_label(self.background, "Window size:", "Arial {} bold".format(self.adjust_sizes([35, 40, 45])), "black", self.root_width / 2 - self.adjust_sizes([80, 110, 100]), 3 * self.root_height / 6 - 30)
            self.window_size_control_button = menu_button(self.background, self.window_size_control, "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2 + self.adjust_sizes([150, 180, 180]), 3 * self.root_height / 6 - 30, self.define_game_options).button
            self.game_settings_label = menu_label(self.background, "Game settings:", "Arial {} bold".format(self.adjust_sizes([35, 40, 45])), "black", self.root_width / 2 - self.adjust_sizes([100, 110, 130]), 4 * self.root_height / 6 - 20)
            self.game_settings_button = menu_button(self.background, "change", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2 + self.adjust_sizes([160, 190, 210]), 4 * self.root_height / 6 - 20, self.game_settings_menu).button
            self.back_button = menu_button(self.background, "back", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "brown", self.root_width / 2, 5 * self.root_height / 6, self.main_menu).button
        else:
            menu_label(self.background, "🤔", "Arial {} bold".format(self.adjust_sizes([35, 40, 45])), "black", self.root_width / 2 + self.adjust_sizes([300, 365, 430]), 4 * self.root_height / 11 - 30)
    def game_settings_menu(self, event = None):
        self.destroy_menu()
        self.menu_name = "game_settings_menu"
        self.balloons_settings_label = menu_label(self.background, "Balloons settings:", "Arial {} bold underline".format(self.adjust_sizes([30, 35, 40])), "black", self.root_width / 2, self.root_height / 11 - 30)
        self.balloons_sizes_label = menu_label(self.background, "Sizes:", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "black", self.root_width / 2 - 20, 2 * self.root_height / 11 - 30)
        self.balloons_sizes_button = menu_button(self.background, len(self.balloons_sizes), "Arial {} bold".format(self.adjust_sizes([20, 25, 30])), "blue", self.root_width / 2 + self.adjust_sizes([50, 65, 80]), 2 * self.root_height / 11 - 30, self.define_game_options).button
        self.balloons_colors_label = menu_label(self.background, "Colors:", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "black", self.root_width / 2 - self.adjust_sizes([60, 70, 80]), 3 * self.root_height / 11 - 30)
        self.balloons_colors_button = menu_button(self.background, "choose", "Arial {} bold".format(self.adjust_sizes([20, 25, 30])), "blue", self.root_width / 2 + self.adjust_sizes([70, 85, 95]), 3 * self.root_height / 11 - 30, self.define_game_options).button
        self.balloons_speeds_label = menu_label(self.background, "Speeds: from      (min) to      (max)", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "black", self.root_width / 2, 4 * self.root_height / 11 - 30)
        self.min_speed_button = menu_button(self.background, self.min_speed, "Arial {} bold".format(self.adjust_sizes([20, 25, 30])), "blue", self.root_width / 2 - self.adjust_sizes([25, 28, 35]), 4 * self.root_height / 11 - 30, self.define_game_options).button
        self.max_speed_button = menu_button(self.background, self.max_speed, "Arial {} bold".format(self.adjust_sizes([20, 25, 30])), "blue", self.root_width / 2 + self.adjust_sizes([150, 180, 215]), 4 * self.root_height / 11 - 30, self.define_game_options).button
        self.balloons_angles_label = menu_label(self.background, "Vertical position offset range (angle): ±      °", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "black", self.root_width / 2, 5 * self.root_height / 11 - 30)
        self.balloons_angles_button = menu_button(self.background, self.balloons_angle_offset, "Arial {} bold".format(self.adjust_sizes([20, 25, 30])), "blue", self.root_width / 2 + self.adjust_sizes([299, 362, 430]), 5 * self.root_height / 11 - 30, self.define_game_options).button
        self.balloons_on_screen_label = menu_label(self.background, "Balloons on screen:", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "black", self.root_width / 2 - self.adjust_sizes([70, 85, 100]),  6 * self.root_height / 11 - 30)
        self.balloons_on_screen_button = menu_button(self.background, self.balloons_on_screen, "Arial {} bold".format(self.adjust_sizes([20, 25, 30])), "blue", self.root_width / 2 + self.adjust_sizes([180, 210, 245]), 6 * self.root_height / 11 - 30, self.define_game_options).button
        self.general_settings_label = menu_label(self.background, "General settings:", "Arial {} bold underline".format(self.adjust_sizes([30, 35, 40])), "black", self.root_width / 2,  7 * self.root_height / 11 - 30)
        self.target_color_change_freq_label = menu_label(self.background, "Change target color every:       seconds", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "black", self.root_width / 2 - 10,  8 * self.root_height / 11 - 30)
        self.target_color_change_freq_button = menu_button(self.background, self.target_color_change_freq, "Arial {} bold".format(self.adjust_sizes([20, 25, 30])), "blue", self.root_width / 2 + self.adjust_sizes([135, 163, 193]), 8 * self.root_height / 11 - 30, self.define_game_options).button
        self.lose_points_on_miss_label = menu_label(self.background, "Lose points on miss:", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "black", self.root_width / 2 - 40,  9 * self.root_height / 11 - 30)
        self.lose_points_on_miss_button = menu_button(self.background, self.lose_points_on_miss, "Arial {} bold".format(self.adjust_sizes([20, 25, 30])), "blue", self.root_width / 2 + self.adjust_sizes([160, 200, 245]), 9 * self.root_height / 11 - 30, self.define_game_options).button
        self.save_and_back_button = menu_button(self.background, "save\nand back", "Arial {} bold".format(self.adjust_sizes([20, 25, 30])), "#006600", self.root_width / 2 - self.adjust_sizes([110, 130, 150]), 10 * self.root_height / 11, self.options_menu).button
        self.default_settings_button = menu_button(self.background, "default\nsettings", "Arial {} bold".format(self.adjust_sizes([20, 25, 30])), "#6600ff", self.root_width / 2 + self.adjust_sizes([100, 120, 140]), 10 * self.root_height / 11, self.set_default_settings).button
    def instructions_menu(self, event = None):
        self.destroy_menu()
        self.menu_name = "instructions_menu"
        self.background.create_text(self.root_width / 2, self.root_height / 10, font = "Courier {} bold underline".format(self.adjust_sizes([30, 35, 40])), fill = "blue", text = "Balloons Game")
        self.background.create_text(self.root_width / 4, 10 * self.root_height / 20, font = "Courier {} bold".format(self.adjust_sizes([15, 17, 20])), fill = "blue", text = self.instructions_text[["greek", "english"].index(self.instructions_language)][0])
        self.background.create_text(4 * self.root_width / 5, 17 * self.root_height / 20, font = "Courier {} bold".format(self.adjust_sizes([25, 30, 35])), fill = "blue", text = self.instructions_text[["greek", "english"].index(self.instructions_language)][1])
        self.change_language_button = menu_button(self.background, self.instructions_language, "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "black", 9 * self.root_width / 10, self.root_height / 10, self.change_instructions_language).button
        self.back_button = menu_button(self.background, "back", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "brown", self.root_width / 2, 9.5 * self.root_height / 10, self.main_menu).button
    def new_game_menu(self, event = None):
        self.destroy_menu()
        self.menu_name = "new_game_menu"
        self.levels_label = menu_label(self.background, "Level:", "Arial {} bold underline".format(self.adjust_sizes([40, 45, 50])), "black", self.root_width / 2, self.root_height / 6 - 30)
        self.easy_level_button = menu_button(self.background, "easy", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2 - self.adjust_sizes([170, 190, 210]), 2 * self.root_height / 6 - 30, self.define_game_options).button
        self.medium_level_button = menu_button(self.background, "medium", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2, 2 * self.root_height / 6 - 30, self.define_game_options).button
        self.hard_level_button = menu_button(self.background, "hard", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2 + self.adjust_sizes([170, 190, 210]), 2 * self.root_height / 6 - 30, self.define_game_options).button
        self.times_label = menu_label(self.background, "Time:", "Arial {} bold underline".format(self.adjust_sizes([40, 45, 50])), "black", self.root_width / 2, 3 * self.root_height / 6 - 30)
        self.minutes_1 = menu_button(self.background, "1 min", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2 - self.adjust_sizes([170, 190, 210]), 4 * self.root_height / 6 - 30, self.define_game_options).button
        self.minutes_2 = menu_button(self.background, "2 min", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2, 4 * self.root_height / 6 - 30, self.define_game_options).button
        self.minutes_3 = menu_button(self.background, "3 min", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 2 + self.adjust_sizes([170, 190, 210]), 4 * self.root_height / 6 - 30, self.define_game_options).button
        self.start_button = menu_button(self.background, "START", "Arial 50 bold".format(self.adjust_sizes([50, 55, 60])), "#006666", self.root_width / 2, 5 * self.root_height / 6 - 20, self.start_game).button
        self.back_button = menu_button(self.background, "back", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "brown", self.root_width / 2, 5 * self.root_height / 5 - 40, self.main_menu).button
        [self.easy_level_button, self.medium_level_button, self.hard_level_button][["easy", "medium", "hard"].index(self.game_level)].configure(fg = "red")
        [self.minutes_1, self.minutes_2, self.minutes_3][["1 min", "2 min", "3 min"].index(self.game_time)].configure(fg = "red")
    def destroy_menu(self, event = None):
        self.background.destroy()
        self.root_width = self.root.winfo_screenwidth() * (7 + self.adjust_sizes([0, 1, 2])) / 10
        self.root_height = self.root.winfo_screenheight() * (7 + self.adjust_sizes([0, 1, 2])) / 10
        self.background = tk.Canvas(self.root, width = self.root_width, height = self.root_height, bg = "yellow", cursor = "cross")
        self.background.grid(row = 0, column = 0, sticky = tk.NSEW)
    def change_instructions_language(self, event = None):
        self.instructions_language = self.alternate_matrix_elements(self.instructions_languages_matrix, self.instructions_language)
        self.instructions_menu()
    def move_cursor(self, event = None):
        try:
            self.background.delete(self.target_cursor)
        except:
            pass
        try:
            self.xcor = event.x
            self.ycor = event.y
        except:
            pass
        self.target_cursor = self.background.create_image(self.xcor, self.ycor, image = self.picture_cursor)
    def adjust_sizes(self, adgust_list):
        return adgust_list[(self.window_sizes_control_matrix).index(self.window_size_control)]
    def define_game_options(self, event):
        if self.menu_name == "options_menu":
            if event.widget == self.music_control_button:
                self.music_control = ["OFF", "ON"][["ON", "OFF"].index(self.music_control)]
                self.music_control_button.configure(text = self.music_control)
                if self.music_control == "OFF":
                    self.stop_music()
                else:
                    self.play_sound("main_menu_sound", "music")
            elif event.widget == self.sound_control_button:
                self.sound_control = ["OFF", "ON"][["ON", "OFF"].index(self.sound_control)]
                self.sound_control_button.configure(text = self.sound_control)
            elif event.widget == self.window_size_control_button:
                self.window_size_control = self.alternate_matrix_elements(self.window_sizes_control_matrix, self.window_size_control)
                self.options_menu()
        if self.menu_name == "game_settings_menu":
            if event.widget == self.balloons_sizes_button: 
                self.balloons_sizes = self.alternate_matrix_elements(self.balloons_sizes_matrix, self.balloons_sizes)
            elif event.widget == self.balloons_colors_button:
                self.balloons_colors_choose()
            elif event.widget == self.min_speed_button:
                self.min_speed = self.alternate_matrix_elements(self.speeds_matrix, self.min_speed)
            elif event.widget == self.max_speed_button:
                self.max_speed = self.alternate_matrix_elements(self.speeds_matrix, self.max_speed)
            elif event.widget == self.balloons_angles_button:
                self.balloons_angle_offset = self.alternate_matrix_elements(self.balloons_angles_offset_matrix, self.balloons_angle_offset)
            elif event.widget == self.balloons_on_screen_button:
                self.balloons_on_screen = ["many", "too many", "few"][["few", "many", "too many"].index(self.balloons_on_screen)]
            elif event.widget == self.target_color_change_freq_button:
                self.target_color_change_freq = self.alternate_matrix_elements(self.target_color_change_freq_matrix, self.target_color_change_freq)
            elif event.widget == self.lose_points_on_miss_button:
                self.lose_points_on_miss = ["no", "yes"][["yes", "no"].index(self.lose_points_on_miss)]
            if event.widget != self.balloons_colors_button:
                self.game_settings_menu()
        if self.menu_name == "colors_menu":
            if event.widget == self.colors_levels_button:
                self.colors_levels_button.configure(text = self.alternate_matrix_elements(self.game_levels_matrix, self.colors_levels_button["text"]))
                for k in range(len(self.colors)):
                    self.colors_buttons[k].configure(bd = 0)
                    if self.colors[k] in self.balloons_colors[(self.game_levels_matrix).index(self.colors_levels_button["text"])]:
                        self.colors_buttons[k].configure(bd = 5, relief = "solid")
            elif event.widget in self.colors_buttons:
                if len(self.balloons_colors[(self.game_levels_matrix).index(self.colors_levels_button["text"])]) != [2, 4, 6][(self.game_levels_matrix).index(self.colors_levels_button["text"])]:
                    self.balloons_colors[(self.game_levels_matrix).index(self.colors_levels_button["text"])].append(event.widget["text"])
                    event.widget.configure(bd = 5, relief = "solid")
            elif event.widget == self.clear_level_colors:
                self.balloons_colors[(self.game_levels_matrix).index(self.colors_levels_button["text"])] = []
                for k in range(len(self.colors)):
                    self.colors_buttons[k].configure(bd = 0)
            elif event.widget == self.confirm_level_colors:
                self.menu_name = "game_settings_menu"
                self.colors_menu.destroy()
                for k in range(3):
                    if len(self.balloons_colors[k]) != 2 * (k + 1):
                        self.balloons_colors[k] = [["blue", "red"], ["blue", "red", "green", "black"], ["blue", "red", "green", "black", "white", "orange"]][k]
        if self.menu_name == "new_game_menu":
            if event.widget["text"] in self.game_levels_matrix:
                [self.easy_level_button, self.medium_level_button, self.hard_level_button][(self.game_levels_matrix).index(self.game_level)].configure(fg = "blue")
                self.game_level = event.widget["text"]
                event.widget.configure(fg = "red")
            elif event.widget["text"] in self.game_times_matrix:
                [self.minutes_1, self.minutes_2, self.minutes_3][(self.game_times_matrix).index(self.game_time)].configure(fg = "blue")
                self.game_time = event.widget["text"]
                event.widget.configure(fg = "red")
    def alternate_matrix_elements(self, matrix, index_element):
        return (matrix[1:] + [matrix[0]])[matrix.index(index_element)]
    def balloons_colors_choose(self, event = None):
        self.menu_name = "colors_menu"
        self.colors_menu = tk.Canvas(self.background, width = self.root_width / 2, height = 2 * self.root_height / 3, bg = "yellow")
        self.colors_menu.place(x = self.root_width / 2, y = self.root_height / 2, anchor = "center")
        self.colors_levels_button = menu_button(self.colors_menu, "easy", "Arial {} bold".format(self.adjust_sizes([40, 45, 50])), "black", self.root_width / 4, self.root_height / 9, self.define_game_options).button
        self.colors_buttons = []
        self.colors = ["blue", "green", "red", "black", "white", "orange", "purple", "pink", "grey"]
        for k in range(len(self.colors)):
            self.colors_buttons.append(menu_button(self.colors_menu, self.colors[k], "Calibri {} bold".format(self.adjust_sizes([30, 35, 40])), self.colors[k], (k % 3 + 1) * self.root_width / 8, (k // 3 + 2) * self.root_height / 9, self.define_game_options).button)
        self.colors_buttons[self.colors.index(self.balloons_colors[0][0])].configure(bd = 5, relief = "solid")
        self.colors_buttons[self.colors.index(self.balloons_colors[0][1])].configure(bd = 5, relief = "solid")
        self.clear_level_colors = menu_button(self.colors_menu, "clear", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "#003300", self.root_width / 8 + 50, 5 * self.root_height / 9, self.define_game_options).button
        self.confirm_level_colors = menu_button(self.colors_menu, "OK", "Arial {} bold".format(self.adjust_sizes([25, 30, 35])), "#0066aa", 3 * self.root_width / 8 - 50, 5 * self.root_height / 9, self.define_game_options).button
    def set_default_settings(self, event = None):
        self.balloons_sizes = [20, 50, 80]
        self.balloons_colors = [["blue", "red"], ["blue", "red", "green", "black"], ["blue", "red", "green", "black", "white", "orange"]]
        self.min_speed, self.max_speed = 5, 30
        self.balloons_angle_offset = 15
        self.balloons_on_screen = "many"
        self.target_color_change_freq = 10
        self.lose_points_on_miss = "yes"
        if event != None:
            self.game_settings_menu()
    def play_sound(self, sound_file, sound_type):
        if sound_type == "music":
            if self.music_control == "ON":
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.load(os.getcwd() + "/Game_Sounds/" + sound_file + ".mp3")
                pygame.mixer.music.play(-1)
        elif sound_type == "sound":
            if self.sound_control == "ON":
                self.sound = pygame.mixer.Sound(os.getcwd() + "/Game_Sounds/" + sound_file + ".wav")
                self.sound.play()
    def stop_music(self):
        pygame.mixer.music.stop()
    def start_game(self, event):
        try:
            self.pause_menu.destroy()
        except AttributeError:
            pass
        self.play_sound("game_sound", "music")
        self.destroy_menu()
        self.picture_cursor = Image.open(os.getcwd() + "/Game_Pictures/" + "target_image.png")
        self.picture_cursor = self.picture_cursor.resize((80, 50), Image.LANCZOS)
        self.picture_cursor = ImageTk.PhotoImage(self.picture_cursor)
        self.background.bind("<Motion>", self.move_cursor)
        self.game_state = "run"
        self.time_seconds = 60 * int(self.game_time.split(" ")[0])
        self.time_seconds_color_change = self.time_seconds
        self.seconds_parts = 100
        self.score = 0
        self.right_hits = 0
        self.wrong_hits = 0
        self.misses = 0
        self.balloons = []
        self.balloons_ports = 10
        self.game_level_balloons_colors = self.balloons_colors[["easy", "medium", "hard"].index(self.game_level)]
        self.choose_color = 0
        self.make_tail = "tail_yes"
        self.create_game_environment()
        self.start_countdown()
    def create_game_environment(self):
        self.line_pointer = 6
        self.background.create_line(self.root_width / self.line_pointer, 0, self.root_width / self.line_pointer, self.root_height, width = 5, fill = "black")
        self.background.create_line((self.line_pointer - 1) * self.root_width / self.line_pointer, 0, (self.line_pointer - 1) * self.root_width / self.line_pointer, self.root_height, width = 5, fill = "black")
        self.background.create_text(self.root_width / (2 * self.line_pointer), self.root_height / (2 * self.line_pointer), font = "Calibri {} bold".format(int(240 / self.line_pointer + self.adjust_sizes([0, 5, 10]))), text = "Clock", fill = "blue")
        self.background.create_rectangle(self.root_width / (8 * self.line_pointer), self.root_height / (2 * self.line_pointer) + 50, 7 * self.root_width / (8 * self.line_pointer), self.root_height / 4 + 50, width = 5, fill = "black")
        self.clock = self.background.create_text(self.root_width / (2 * self.line_pointer), self.root_height * (1 / 8 + 1 / (4 * self.line_pointer)) + 50, font = "Calibri {} bold".format(int(170 / self.line_pointer + self.adjust_sizes([0, 5, 10]))), text = "{}:00.00".format(int(self.game_time.split(" ")[0])), fill = "red")
        self.background.create_text(self.root_width / (2 * self.line_pointer), self.root_height / 2, font = "Calibri {} bold".format(int(240 / self.line_pointer + self.adjust_sizes([0, 5, 10]))), text = "Colour", fill = "blue")
        self.color_indicator = self.background.create_rectangle(self.root_width / (6 * self.line_pointer), self.root_height / 2 + 50, 5 * self.root_width / (6 * self.line_pointer), 3 * self.root_height / 4 + 50, width = 5, fill = "black")
        self.background.create_text((2 * self.line_pointer - 1) * self.root_width / (2 * self.line_pointer), self.root_height / (2 * self.line_pointer), font = "Calibri {} bold".format(int(240 / self.line_pointer + self.adjust_sizes([0, 5, 10]))), text = "Score", fill = "blue")
        self.background.create_rectangle((self.line_pointer - 1) * self.root_width / self.line_pointer + self.root_width / (8 * self.line_pointer), self.root_height / (2 * self.line_pointer) + 50, self.root_width - self.root_width / (8 * self.line_pointer), self.root_height / 4 + 50, width = 5, fill = "black")
        self.score_indicator = self.background.create_text((2 * self.line_pointer - 1) * self.root_width / (2 * self.line_pointer), self.root_height * (1 / 8 + 1 / (4 * self.line_pointer)) + 50, font = "Calibri {} bold".format(int(200 / self.line_pointer + self.adjust_sizes([0, 5, 10]))), text = self.score, fill = "white")
        self.background.create_text((2 * self.line_pointer - 1) * self.root_width / (2 * self.line_pointer), self.root_height * (1 / 8 + 1 / (4 * self.line_pointer)) + self.adjust_sizes([130, 140, 150]), font = "Calibri {} bold".format(self.adjust_sizes([20, 23, 26])), text = "Min score: {}".format(self.min_speed), fill = "black")
        self.background.create_text((2 * self.line_pointer - 1) * self.root_width / (2 * self.line_pointer), self.root_height * (1 / 8 + 1 / (4 * self.line_pointer)) + self.adjust_sizes([150, 163, 176]), font = "Calibri {} bold".format(self.adjust_sizes([20, 23, 26])), text = "Max score: {}".format(int(len(self.balloons_sizes) * self.max_speed)), fill = "black")
        self.background.create_text((2 * self.line_pointer - 1) * self.root_width / (2 * self.line_pointer), self.root_height / 2, font = "Calibri {} bold".format(int(165 / self.line_pointer + self.adjust_sizes([0, 5, 10]))), text = "Comments", fill = "blue")
        self.comments = self.background.create_text((2 * self.line_pointer - 1) * self.root_width / (2 * self.line_pointer), 3 * self.root_height / 4, font = "Calibri {} bold".format(int(168 / self.line_pointer)), text = "", fill = "black")
        self.write_comment("Press the\nButton-2 (wheel)\nto add/remove\nballoons' tales.", self.adjust_sizes([18, 20, 22]), "black")
        self.comment = ""
    def start_countdown(self):
        if self.comment != "Go!!!":
            try:
                self.background.delete(self.countdown_text)
            except AttributeError:
                pass
            self.comment = ["Get ready!!!", "3", "2", "1", "Go!!!"][["", "Get ready!!!", "3", "2", "1"].index(self.comment)]
            self.countdown_text = self.background.create_text(self.root_width / 2, self.root_height / 2, font = "Calibri {} bold".format([80, 120, 120, 120, 80][["Get ready!!!", "3", "2", "1", "Go!!!"].index(self.comment)] + self.adjust_sizes([0, 10, 20])), text = self.comment, fill = "black")
            self.background.after(1000, self.start_countdown)
        else:
            self.background.delete(self.countdown_text)
            self.run_seconds_parts(10)
            self.create_balloons()
            self.background.bind("<Button-1>", self.left_click)
            self.background.bind("<Button-3>", self.pause_game)
            self.background.bind("<Button-2>", self.add_remove_tail)
    def add_remove_tail(self, event):
        self.make_tail = ["tail_no", "tail_yes"][["tail_yes", "tail_no"].index(self.make_tail)]
    def run_seconds_parts(self, parts):
        if self.game_state == "run":
            self.background.delete(self.clock)
            self.clock = self.background.create_text(self.root_width / (2 * self.line_pointer), self.root_height * (1 / 8 + 1 / (4 * self.line_pointer)) + 50, font = "Calibri {} bold".format(int(170 / self.line_pointer + self.adjust_sizes([0, 5, 10]))), text = "{}:{:02d}.{:02d}".format(int(self.time_seconds // 60), int(self.time_seconds % 60), int(self.seconds_parts % 100)), fill = "red")
            if self.seconds_parts % 100 == 0:
                self.run_seconds()
            self.seconds_parts -= int(100 / parts)
            self.background.after(int(1000 / parts), lambda: self.run_seconds_parts(10))
    def run_seconds(self):
        try:
            self.background.delete(self.color_pointing)
            self.background.delete(self.color_indicator)
            self.color_indicator = self.background.create_rectangle(self.root_width / (6 * self.line_pointer), self.root_height / 2 + 50, 5 * self.root_width / (6 * self.line_pointer), 3 * self.root_height / 4 + 50, width = 5, fill = self.target_color)
        except AttributeError:
            pass
        if self.time_seconds == 0:
            self.write_comment("Time\nran out!\nGame over!\n", self.adjust_sizes([25, 27, 29]), "black")
            self.pause_game()
            self.resume_game_button.destroy()
            self.pause_menu.create_text(self.root_width / 4, self.root_height / 8, font = "Calibri {} bold".format(self.adjust_sizes([30, 35, 40])), text = "Final points: {}\nRight hits ratio: {}%".format(self.score, int(self.right_hits / (self.right_hits + self.wrong_hits + self.misses) * 100)), fill = "black")
        else:
            if self.time_seconds == self.time_seconds_color_change:
                if self.target_color_change_freq == "?":
                    self.time_seconds_color_change = self.time_seconds - r.randint(1, 20)
                else:
                    self.time_seconds_color_change = self.time_seconds - self.target_color_change_freq
                self.target_color = self.game_level_balloons_colors[self.choose_color % len(self.game_level_balloons_colors)]
                self.background.delete(self.color_indicator)
                self.color_indicator = self.background.create_rectangle(self.root_width / (6 * self.line_pointer), self.root_height / 2 + 50, 5 * self.root_width / (6 * self.line_pointer), 3 * self.root_height / 4 + 50, width = 20, fill = self.target_color)
                self.color_pointing = self.background.create_text(self.root_width / (2 * self.line_pointer), 3 * self.root_height / 4 + 100, font = "Courier 80 bold", fill = "black", text = "▲")
                self.choose_color += 1
            self.time_seconds -= 1
    def create_balloons(self):
        if self.game_state == "run":
            self.random_balloon_radius = r.choice(self.balloons_sizes)
            self.balloons.append(balloon(self.background, balloon_xcor = self.root_width / self.line_pointer + self.random_balloon_radius + r.randint(0, self.balloons_ports - 1) * ((self.line_pointer - 2) * self.root_width / self.line_pointer - 2 * self.random_balloon_radius) / (self.balloons_ports - 1), balloon_ycor = self.root_height + self.random_balloon_radius,\
                                        balloon_radius = self.random_balloon_radius, balloon_angle = r.randint(90 - self.balloons_angle_offset, 90 + self.balloons_angle_offset), balloon_color = r.choice(self.game_level_balloons_colors + int(len(self.balloons_colors) / 2) * [self.target_color]), balloon_speed = r.choice(list(range(self.min_speed, self.max_speed + 1))), tail_length = r.choice([75, 100, 125, 150]), tail_parts_number = r.randint(5, 10), tail_existence = self.make_tail))
            self.balloons[-1].move_balloon()
            self.background.after(r.choice([[400, 700], [200, 400], [100, 200]][["few", "many", "too many"].index(self.balloons_on_screen)]), self.create_balloons)
    def left_click(self, event):
        if self.game_state == "run":
            self.count_hits = 0
            if event.x >= self.root_width / self.line_pointer and event.x <= (self.line_pointer - 1) * self.root_width / self.line_pointer and event.y >= 0 and event.y <= self.root_height:
                for balloon in self.balloons:
                    if (event.x - balloon.balloon_xcor_new) ** 2 + (event.y - balloon.balloon_ycor_new) ** 2 <= balloon.balloon_radius ** 2:
                        balloon.balloon_hit = 1
                        balloon.pop_balloon(event.x, event.y)
                        self.count_hits += 1
                if self.count_hits == 0:
                    if self.lose_points_on_miss == "yes":
                        self.misses += 1
                        self.change_score((-1 * (int(len(self.balloons_sizes) * self.max_speed / 4 + [0, len(self.balloons_sizes) * self.max_speed / 5, 2 * len(self.balloons_sizes) * self.max_speed / 5][["easy", "medium", "hard"].index(self.game_level)]))), event.x, event.y)
                    self.write_comment("{}\nMiss!".format(r.choice(["😟", "😰"])), 40, "red")
            else:
                self.write_comment("Out of\nlimits!", 40, "black")
    def change_score(self, points, xcor, ycor):
        self.score += points
        self.background.delete(self.score_indicator)
        self.score_indicator = self.background.create_text((2 * self.line_pointer - 1) * self.root_width / (2 * self.line_pointer), self.root_height * (1 / 8 + 1 / (4 * self.line_pointer)) + 50, font = "Calibri {} bold".format(int(200 / self.line_pointer + self.adjust_sizes([0, 5, 10]))), text = self.score, fill = "white")
        self.points_indicator = self.background.create_text(xcor, ycor, font = "Calibri 50 bold", text = [str(points), "+" + str(points)][[points < 0, points >= 0].index(True)], fill = ["red", "green"][[points < 0, points >= 0].index(True)])
        self.background.after(500, lambda item = self.points_indicator: self.background.delete(item))
    def write_comment(self, comment, size, color):
        self.comment = comment
        self.background.delete(self.comments)
        self.comments = self.background.create_text((2 * self.line_pointer - 1) * self.root_width / (2 * self.line_pointer), 3 * self.root_height / 4, font = "Calibri {} bold".format(size), text = self.comment, fill = color)
    def pause_game(self, event = None):
        if self.game_state == "run":
            self.game_state = "stop"
            self.stop_music()
            self.pause_menu = tk.Canvas(self.background, width = self.root_width / 2, height = self.root_height / 2, bg = "yellow")
            self.pause_menu.place(x = self.root_width / 2, y = self.root_height / 2, anchor = "center")
            self.resume_game_button = menu_button(self.pause_menu, "Resume", "Calibri {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 4, self.root_height / 8, self.resume_game).button
            self.restart_game_button = menu_button(self.pause_menu, "Restart", "Calibri {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 4, 2 * self.root_height / 8, self.confirm_choice).button    
            self.new_game_button = menu_button(self.pause_menu, "New game", "Calibri {} bold".format(self.adjust_sizes([30, 35, 40])), "blue", self.root_width / 4, 3 * self.root_height / 8, self.confirm_choice).button    
    def resume_game(self, event):
        self.pause_menu.destroy()
        self.play_sound("game_sound", "music")
        self.game_state = "run"
        self.run_seconds_parts(10)
        for balloon in self.balloons:
            balloon.move_balloon()
        self.create_balloons()
    def confirm_choice(self, event = None):
        self.confirm_menu = tk.Canvas(self.background, width = self.root_width / 3, height = self.root_height / 3, bg = "yellow")
        self.confirm_menu.place(x = self.root_width / 2, y = self.root_height / 2, anchor = "center")
        self.confirm_question_button = menu_label(self.confirm_menu, "Are you sure?", "Arial {} bold".format(self.adjust_sizes([30, 35, 40])), "black", self.root_width / 6, self.root_height / 9)
        self.accept_choice_button = menu_button(self.confirm_menu, "✓", "Calibri {} bold".format(self.adjust_sizes([40, 45, 50])), "green", self.root_width / 6 - 60, 2 * self.root_height / 9, [self.start_game, self.main_menu][[self.restart_game_button, self.new_game_button].index(event.widget)]).button    
        self.deny_choice_button = menu_button(self.confirm_menu, "✗", "Calibri {} bold".format(self.adjust_sizes([40, 45, 50])), "red", self.root_width / 6 + 60, 2 * self.root_height / 9, lambda event: self.confirm_menu.destroy()).button    
    # self.information_box = tk.Text(self.information_box_background, font = 'Calibri 10 bold', width = 38, height = 24)
    # self.information_box.grid(row = 0, column = 0, sticky = tk.N)
    # def write_information_box(self, note, note_color, message):
    #     self.text_pointer = self.information_box.index('end')
    #     self.information_box.insert('end', "\n********************************************\n{}: {}".format(note, message))
    #     self.information_box.tag_add('{}'.format(note), str(float(self.text_pointer) + 1.0), format(float(self.text_pointer) + 1.00 + float(len(note) / 100), ".2f"))
    #     self.information_box.tag_configure('{}'.format(note), foreground = note_color, font = 'Arial 10 bold italic')
    #     self.information_box.see('end')

class menu_button():
    def __init__(self, background, button_text, button_font, button_fg, button_xcor, button_ycor, button_func):
        self.button = tk.Label(background, text = button_text, font = button_font, fg = button_fg, bg = "yellow")
        self.button.place(x = button_xcor, y = button_ycor, anchor = "center")
        self.button.bind("<Enter>", lambda event, button = self.button: [button.configure(font = "Arial {} bold".format(int(button["font"].split(" ")[1]) + 10)), balloons_game.play_sound("hover_button_sound", "sound")])
        self.button.bind("<Leave>", lambda event, button = self.button: button.configure(font = button_font))
        self.button.bind("<Button-1>", lambda event: [button_func(event), balloons_game.play_sound("select_button_sound", "sound")])

class menu_label():
    def __init__(self, background, label_text, label_font, label_fg, label_xcor, label_ycor):
        self.label = tk.Label(background, text = label_text, font = label_font, fg = label_fg, bg = "yellow")
        self.label.place(x = label_xcor, y = label_ycor, anchor = "center")

class balloon():
    def __init__(self, background, balloon_xcor, balloon_ycor, balloon_radius, balloon_angle, balloon_color, balloon_speed, tail_length, tail_parts_number, tail_existence):
        self.background = background
        self.balloon_xcor = balloon_xcor
        self.balloon_ycor = balloon_ycor
        self.balloon_radius = balloon_radius
        self.balloon_angle = m.pi / 180 * balloon_angle
        self.balloon_color = balloon_color
        self.balloon_speed = balloon_speed
        self.tail_length = tail_length
        self.tail_parts_number = tail_parts_number
        self.tail_existence = tail_existence
        self.balloon_hit = 0
        self.timer = 0
        self.angles = [0, 10, 20, 30, 40, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -40, -30, -20, -10]
        if self.tail_existence == "tail_yes":
            self.tail_part_length = self.tail_length / self.tail_parts_number
            self.tail_pointer = 0
            self.balloon_tail = []
            for k in range(self.tail_parts_number):
                self.balloon_tail.append(tail_part(self.background, self.balloon_xcor - (self.balloon_radius + self.tail_part_length / 2) * m.cos(self.balloon_angle) - self.tail_part_length * m.cos(self.balloon_angle) * k,\
                                                self.balloon_ycor + (self.balloon_radius + self.tail_part_length / 2) * m.sin(self.balloon_angle) + self.tail_part_length * m.sin(self.balloon_angle) * k, self.balloon_angle, self.tail_part_length))
        self.balloon_body = circle(self.background, self.balloon_xcor, self.balloon_ycor, self.balloon_radius, self.balloon_color)
    def move_balloon(self, event = None):
        if balloons_game.game_state == "run":
            self.timer += 1
            if self.tail_existence == "tail_yes":
                for k in range(self.tail_parts_number):
                    self.balloon_tail[k].move_tail_part(m.pi / 180 * self.angles[self.tail_pointer] * (-1) ** k, + self.balloon_speed * m.cos(self.balloon_angle) * self.timer, - self.balloon_speed * m.sin(self.balloon_angle) * self.timer)
                self.tail_pointer = (self.tail_pointer + 1) % len(self.angles)
            self.balloon_xcor_new = self.balloon_xcor + self.balloon_speed * m.cos(self.balloon_angle) * self.timer
            self.balloon_ycor_new = self.balloon_ycor - self.balloon_speed * m.sin(self.balloon_angle) * self.timer
            if self.balloon_hit == 0 and self.balloon_xcor_new > balloons_game.root_width / balloons_game.line_pointer - self.balloon_radius and self.balloon_xcor_new < (balloons_game.line_pointer - 1) * balloons_game.root_width / balloons_game.line_pointer + self.balloon_radius and self.balloon_ycor_new > -1 * self.balloon_radius:
                self.background.delete(self.balloon_body.circle)
                self.balloon_body = circle(self.background, self.balloon_xcor_new, self.balloon_ycor_new, self.balloon_radius, self.balloon_color)
                self.background.after(40, self.move_balloon)
            else:
                if self.tail_existence == "tail_yes":
                    for k in range(self.tail_parts_number):
                        self.background.delete(self.balloon_tail[k].line)
                self.background.delete(self.balloon_body.circle)
                del balloons_game.balloons[[balloon.balloon_body for balloon in balloons_game.balloons].index(self.balloon_body)]
    def pop_balloon(self, event_xcor, event_ycor):
        balloons_game.play_sound("pop_balloon_sound", "sound")
        if self.balloon_color == balloons_game.target_color:
            balloons_game.right_hits += 1
            balloons_game.change_score((len(balloons_game.balloons_sizes) - balloons_game.balloons_sizes.index(self.balloon_radius)) * self.balloon_speed, event_xcor, event_ycor)
            balloons_game.write_comment("{}\nNice Hit!\nSize: {}\nSpeed: {}".format(r.choice(["👍", "🙂", "👏", "😎"]), balloons_game.balloons_sizes.index(self.balloon_radius) + 1, self.balloon_speed), balloons_game.adjust_sizes([30, 35, 40]), "green")
        else:
            balloons_game.wrong_hits += 1
            balloons_game.change_score(-1 * (balloons_game.balloons_sizes.index(self.balloon_radius) + 1) * (balloons_game.max_speed - list(range(balloons_game.min_speed, balloons_game.max_speed + 1)).index(self.balloon_speed)), event_xcor, event_ycor)
            balloons_game.write_comment("{}\nBad Hit!\nSize: {}\nSpeed: {}".format(r.choice(["👎", "😞", "😧", "😥"]), balloons_game.balloons_sizes.index(self.balloon_radius) + 1, self.balloon_speed), balloons_game.adjust_sizes([30, 35, 40]), "red")

class tail_part():
    def __init__(self, background, tail_xcor, tail_ycor, angle_initial, length):
        self.background = background
        self.x_initial = tail_xcor
        self.y_initial = tail_ycor
        self.angle_initial = angle_initial
        self.length = length
        self.x_final = self.x_initial + self.length * m.cos(self.angle_initial)
        self.y_final = self.y_initial - self.length * m.sin(self.angle_initial)
        self.fill_lines_gap = 3
        self.line = self.background.create_line(self.x_initial, self.y_initial, self.x_final, self.y_final, width = 6)
    def move_tail_part(self, angle_final, speed_xmovement, speed_ymovement):
        self.background.delete(self.line)
        self.x_initial_new = self.x_initial + (self.length + self.fill_lines_gap) / 2 * m.cos(self.angle_initial) - (self.length + self.fill_lines_gap) / 2 * m.cos(self.angle_initial + angle_final) / m.cos(angle_final) + speed_xmovement
        self.y_initial_new = self.y_initial - (self.length + self.fill_lines_gap) / 2 * m.sin(self.angle_initial) + (self.length + self.fill_lines_gap) / 2 * m.sin(self.angle_initial + angle_final) / m.cos(angle_final) + speed_ymovement
        self.x_final_new = self.x_initial + (self.length + self.fill_lines_gap) / 2 * m.cos(self.angle_initial) + (self.length + self.fill_lines_gap) / 2 * m.cos(self.angle_initial + angle_final) / m.cos(angle_final) + speed_xmovement
        self.y_final_new = self.y_initial - (self.length + self.fill_lines_gap) / 2 * m.sin(self.angle_initial) - (self.length + self.fill_lines_gap) / 2 * m.sin(self.angle_initial + angle_final) / m.cos(angle_final) + speed_ymovement
        self.line = self.background.create_line(self.x_initial_new, self.y_initial_new, self.x_final_new, self.y_final_new, width = 6)

class circle():
    def __init__(self, background, x_centre, y_centre, radius, colour):
        self.background = background
        self.x_centre = x_centre
        self.y_centre = y_centre
        self.radius = radius
        self.colour = colour
        self.circle = self.background.create_oval(self.x_centre - self.radius, self.y_centre - self.radius, self.x_centre + self.radius, self.y_centre + self.radius, fill = self.colour, width = 3)    

root = tk.Tk()
balloons_game = balloons_game(root)
root.mainloop()
