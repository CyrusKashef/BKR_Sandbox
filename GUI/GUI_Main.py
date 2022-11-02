import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
from os import getcwd, listdir
from random import randint
import json
import webbrowser

from Data_Files.Models_Dict import MODELS_DICT
from Data_Files.Video_Overview_Dict import VIDEO_OVERVIEW_DICT
from .GUI_Style import STYLE_DICT
from .GUI_Progression import GUI_PROGRESSION_CLASS

############################
### ADDITIONAL GUI CLASS ###
############################

def ADDITIONAL_GUI(gif_image, label_message, button_message):
    def update_gif(ind):
        '''Updates The Gif Frame'''
        frame = frames[ind]
        ind += 1
        if ind == frame_count:
            ind = 0
        bottles_talking_label.configure(image=frame)
        bottles_talking_label.after(60, update_gif, ind)
    # SETUP
    BACKGROUND_COLOR = "#BFBF00"
    FONT_TYPE = "LITHOGRAPH-BOLD"
    FONT_SIZE = 12
    # CREATE WINDOW
    this_window = tk.Tk()
    this_window.winfo_toplevel().title("Banjo-Kazooie Randomizer Pop-Up")
    this_window.config(background=BACKGROUND_COLOR)
    # TALKING SPRITE
    frame_count = 10
    frames = [tk.PhotoImage(master=this_window, file=(f"{getcwd()}/GUI/Sprites/{gif_image}.gif"), format = 'gif -index %i' %(i)) for i in range(frame_count)]
    bottles_talking_label = tk.Label(this_window, background=BACKGROUND_COLOR)
    bottles_talking_label.pack(padx=5, pady=2)
    # LABEL
    this_label = tk.Label(this_window, text=label_message, background=BACKGROUND_COLOR, font=(FONT_TYPE, FONT_SIZE))
    this_label.config(anchor='center')
    this_label.pack(padx=5, pady=2)
    # BUTTONS
    close_button = tk.Button(this_window, text=button_message, background=BACKGROUND_COLOR, command=this_window.destroy, font=(FONT_TYPE, FONT_SIZE))
    close_button.config(anchor='center')
    close_button.pack(padx=5, pady=2)
    # END WINDOW
    this_window.protocol("WM_DELETE_WINDOW", this_window.destroy)
    this_window.after(0, update_gif, 0)
    this_window.mainloop()

class GUI_MAIN_CLASS():
    def __init__(self, bk_rando_version):
        ### CONSTANTS ###
        self._GENERIC_BACKGROUND_COLOR = "#BFBF00"
        self._WHITE_COLOR = "#FFFFFF"
        self._BLACK_COLOR = "#000000"
        self._GRAY_COLOR = "#808080"
        self._BLUE_COLOR = "#0040AA"
        self._RED_COLOR = "#990000"
        self._GOLD_COLOR = "#BFBF00"
        self._FONT_TYPE = "LITHOGRAPH-BOLD"
        self._LARGE_FONT_SIZE = 22
        self._MEDIUM_FONT_SIZE = 16
        self._SMALL_MEDIUM_FONT_SIZE = 13
        self._SMALL_FONT_SIZE = 10

        ### VARIABLES ###
        self._bk_rando_version = bk_rando_version
        self._app_window = tk.Tk()
        self._app_window.winfo_toplevel().title(f"Banjo-Kazooie Randomizer v{self._bk_rando_version}")
        self._cwd = getcwd() + "/"
        self._bk_model_preset_folder = f"{self._cwd}Automated/Game_Assets/Models/Specific_Models/Important_Characters/BK_Model_Presets/"
    
    #################
    ### GUI STYLE ###
    #################

    def _gui_style(self):
        self._tab_control = ttk.Notebook(self._app_window)
        self._style = ttk.Style()
        for theme_name in STYLE_DICT:
            self._style.theme_create(theme_name,
                parent="alt",
                settings={
                    "TNotebook": {
                        "configure": {
                            "tabmargins": [2, 5, 2, 0],
                            "background": STYLE_DICT[theme_name]["Background_Color"],
                            },
                        },
                    "TNotebook.Tab": {
                        "configure": {
                            "padding": [5, 5],
                            "foreground": STYLE_DICT[theme_name]["Not_Selected_Tab_Font_Color"],
                            "background": STYLE_DICT[theme_name]["Not_Selected_Tab_Color"],
                            "anchor": 'CENTER',
                            "font": ("Arial bold", 10),
                            "focuscolor": STYLE_DICT[theme_name]["Selected_Tab_Color"],
                            },
                        "map": {
                            "foreground": [("selected", STYLE_DICT[theme_name]["Not_Selected_Tab_Font_Color"])],
                            "background": [("selected", STYLE_DICT[theme_name]["Selected_Tab_Color"])],
                            "expand": [("selected", [1, 1, 1, 0])],
                            }
                        },
                    "Horizontal.TProgressbar": {
                        "configure": {
                            "troughcolor": STYLE_DICT[theme_name]["Progressbar_Background"],
                            "background": STYLE_DICT[theme_name]["Progressbar_Foreground"],
                            "anchor": 'CENTER',
                            "padding": [10, 10],
                            "width": 20,
                            },
                        },
                    "TCombobox": {
                        "configure": {
                            "foreground": STYLE_DICT[theme_name]["Background_Font_Color"],
                            "background": STYLE_DICT[theme_name]["Background_Color"],
                            }
                        },
                    "TLabel": {
                        "configure": {
                            "foreground": STYLE_DICT[theme_name]["Background_Font_Color"],
                            "background": STYLE_DICT[theme_name]["Background_Color"],
                            "font": (self._FONT_TYPE, self._MEDIUM_FONT_SIZE),
                            }
                        },
                    "TLabelframe": {
                        "configure": {
                            "foreground": STYLE_DICT[theme_name]["Background_Font_Color"],
                            "background": STYLE_DICT[theme_name]["Background_Color"],
                            "font": (self._FONT_TYPE, self._LARGE_FONT_SIZE),
                            "borderwidth": 1,
                            "relief": "raised",
                            }
                        },
                    "TLabelframe.Label": {
                        "configure": {
                            "foreground": STYLE_DICT[theme_name]["Background_Font_Color"],
                            "background": STYLE_DICT[theme_name]["Background_Color"],
                            "font": (self._FONT_TYPE, self._MEDIUM_FONT_SIZE),
                            "borderwidth": 1,
                            "relief": "raised",
                            }
                        },
                    "TFrame": {
                        "configure": {
                            "foreground": STYLE_DICT[theme_name]["Background_Font_Color"],
                            "background": STYLE_DICT[theme_name]["Background_Color"],
                            "font": (self._FONT_TYPE, self._LARGE_FONT_SIZE),
                            "borderwidth": 1,
                            "relief": "raised",
                            }
                        },
                    "TButton": {
                        "configure": {
                            "foreground": STYLE_DICT[theme_name]["Background_Font_Color"],
                            "background": STYLE_DICT[theme_name]["Background_Color"],
                            "anchor": 'CENTER',
                            "borderwidth": 1,
                            "relief": "raised",
                            "focuscolor": STYLE_DICT[theme_name]["Background_Color"],
                            }
                        },
                    "TCheckbutton": {
                        "configure": {
                            "foreground": STYLE_DICT[theme_name]["Background_Font_Color"],
                            "background": STYLE_DICT[theme_name]["Background_Color"],
                            "anchor": 'w',
                            "borderwidth": 1,
                            "relief": "raised",
                            "font": (self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE),
                            "takefocus": False,
                            }
                        },
                    "Treeview": {
                        "configure": {
                            "foreground": STYLE_DICT[theme_name]["Treeview_Font_Color"],
                            "background": STYLE_DICT[theme_name]["Treeview_Color"],
                            "rowheight": 25,
                            "fieldbackground": STYLE_DICT[theme_name]["Background_Color"],
                            },
                        "map": {
                            "foreground": [("selected", STYLE_DICT[theme_name]["Treeview_Color"])],
                            "background": [("selected", STYLE_DICT[theme_name]["Treeview_Font_Color"])],
                            }
                        },
                    "Treeview.Heading": {
                        "configure": {
                            "background": STYLE_DICT[theme_name]["Treeview_Font_Color"],
                            "foreground": STYLE_DICT[theme_name]["Treeview_Color"],
                            "rowheight": 25,
                            "fieldbackground": STYLE_DICT[theme_name]["Background_Color"],
                            }
                        }
                    })
        self._set_style("Banjo-Kazooie Jiggy")
    
    def _set_style(self, selected_style):
        self._style.theme_use(selected_style)
    
    ###################
    ### GENERAL TAB ###
    ###################

    def _select_rom_file(self):
        print("Selecting Original ROM file")
        filename = tkinter.filedialog.askopenfilename(initialdir=self._cwd, title="Select The BK ROM File", filetype =(("Rom Files","*.z64"),("all files","*.*")) )
        if(not filename):
            return
        self._original_rom_file_entry.set(filename)
        self._original_rom_file_display.xview_moveto(1)

    def _select_randomized_rom_destination(self):
        print("Selecting Original ROM file")
        new_directory = tkinter.filedialog.askdirectory(initialdir=self._cwd, title="Select Randomized ROM File Location")
        if(not new_directory):
            return
        self._randomized_rom_file_entry.set(new_directory + "/")
        self._randomized_rom_file_display.xview_moveto(1)
    
    def _random_seed_value(self):
        print("Random Seed Value")
        self._seed_value.set(str(randint(10000000, 19940303)))

    def _generate_randomizer_settings_code(self):
        pass

    def _apply_randomizer_settings_code(self):
        pass
    
    def _gui_style_change(self, *args):
        self._set_style(self._gui_style_value.get())

    def _create_general_tab(self):
        self._general_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._general_tab, text="General")
        self._general_frame = ttk.Frame(self._general_tab)
        self._general_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self._create_select_rom_frame()
        self._create_seed_frame()
        self._create_settings_code_frame()
        self._create_gui_style_frame()
    
    def _create_select_rom_frame(self):
        self._rom_frame = ttk.Frame(self._general_tab)
        self._rom_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # DISCLAIMER
        self._rom_file_disclaimer_label = ttk.Label(self._rom_frame, text="ROMs must be v1.0 NTSC of Banjo-Kazooie, ending in .z64", anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._rom_file_disclaimer_label.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky='w')
        # FOLDER BUTTON
        self._folder_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Open_File.png")
        self._select_rom_button = ttk.Button(self._rom_frame, text='Select Original ROM File', image=self._folder_image, command=self._select_rom_file)
        self._select_rom_button.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        # ORIGINAL ROM TEXT
        self._original_rom_file_label = ttk.Label(self._rom_frame, text="Original ROM:", anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._original_rom_file_label.grid(row=1, column=2, padx=5, pady=5, sticky='w')
        # ORIGINAL ROM ENTRY
        self._original_rom_file_entry = tk.StringVar(self._rom_frame)
        self._original_rom_file_display = tk.Entry(self._rom_frame, textvariable=self._original_rom_file_entry, state='readonly', width=35, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._original_rom_file_display.grid(row=1, column=3, columnspan=2, padx=10, pady=5)
        self._original_rom_file_display.xview_moveto(1)
        # FOLDER BUTTON
        self._select_rando_rom_button = ttk.Button(self._rom_frame, text='Select Randomized ROM Destination', image=self._folder_image, command=self._select_randomized_rom_destination)
        self._select_rando_rom_button.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        # RANDOMIZED ROM TEXT
        self._randomized_rom_file_label = ttk.Label(self._rom_frame, text="New ROM Dest:", anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._randomized_rom_file_label.grid(row=2, column=2, padx=5, pady=5, sticky='w')
        # RANDOMIZED ROM ENTRY
        self._randomized_rom_file_entry = tk.StringVar(self._rom_frame)
        self._randomized_rom_file_display = tk.Entry(self._rom_frame, textvariable=self._randomized_rom_file_entry, state='readonly', width=35, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._randomized_rom_file_display.grid(row=2, column=3, columnspan=2, padx=10, pady=5)
        self._randomized_rom_file_display.xview_moveto(1)
    
    def _create_seed_frame(self):
        self._seed_frame = ttk.Frame(self._general_tab)
        self._seed_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # RANDOM SEED BUTTON
        self._seed_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Seed.png")
        self._random_seed_button = ttk.Button(self._seed_frame, text='Random Seed Button', image=self._seed_image, command=self._random_seed_value)
        self._random_seed_button.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        # SEED TEXT
        self._seed_label = ttk.Label(self._seed_frame, text="Seed:", anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._seed_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        # SEED VALUE
        self._seed_value = tk.StringVar(self._seed_frame)
        self._seed_entry = tk.Entry(self._seed_frame, textvariable=self._seed_value, width=43, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._seed_entry.grid(row=0, column=2, padx=10, pady=5)
    
    def _create_settings_code_frame(self):
        self._settings_code_frame = ttk.Frame(self._general_tab)
        self._settings_code_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # GENERATE SETTINGS CODE BUTTON
        self._generate_setting_code_button = tk.Button(self._settings_code_frame, text='Generate\nSettings\nCode', width=7, command=self._generate_randomizer_settings_code, foreground=self._WHITE_COLOR, background=self._BLUE_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._generate_setting_code_button.grid(row=0, column=0, padx=5, pady=5)
        # APPLY SETTINGS CODE BUTTON
        self._apply_setting_code_button = tk.Button(self._settings_code_frame, text='Apply\nSettings\nCode', width=7, command=self._apply_randomizer_settings_code, foreground=self._WHITE_COLOR, background=self._RED_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._apply_setting_code_button.grid(row=0, column=1, padx=5, pady=5)
        # SETTINGS CODE TEXT
        self._settings_code_label = ttk.Label(self._settings_code_frame, text="Settings Code:", anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._settings_code_label.grid(row=0, column=2, padx=5, pady=5, sticky='w')
        # SETTINGS CODE ENTRY
        self._settings_code_value = tk.StringVar(self._settings_code_frame)
        self._settings_code_entry = tk.Entry(self._settings_code_frame, textvariable=self._settings_code_value, width=30, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._settings_code_entry.grid(row=0, column=3, padx=5, pady=5)
        # APPLY PRESET BUTTON
        self._save_preset_button = tk.Button(self._settings_code_frame, text='Save\nPreset\nFile', width=7, command=self._save_current_configuration, foreground=self._WHITE_COLOR, background=self._BLUE_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._save_preset_button.grid(row=1, column=0, padx=5, pady=5)
        # APPLY PRESET BUTTON
        self._apply_preset_button = tk.Button(self._settings_code_frame, text='Apply\nPreset\nFile', width=7, command=(lambda: self._load_configuration(ask_open_filename=False, file_name=(self._preset_value.get()).replace(" ", "_"))), foreground=self._WHITE_COLOR, background=self._RED_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._apply_preset_button.grid(row=1, column=1, padx=5, pady=5)
        # PRESET TEXT
        self._preset_label = ttk.Label(self._settings_code_frame, text="Use Preset:", anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._preset_label.grid(row=1, column=2, padx=5, pady=5, sticky='w')
        # PRESETS
        self._preset_options = [file_name.replace(".json", "").replace("_", " ") for file_name in listdir(f"{self._cwd}GUI/Configurations/")]
        self._preset_value = tk.StringVar(self._settings_code_frame)
        self._preset_value.set("[Select Preset]")
        self._preset_dropdown = ttk.Combobox(self._settings_code_frame, textvariable=self._preset_value, width=29, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._preset_dropdown['values'] = self._preset_options
        self._preset_dropdown['state'] = 'readonly'
        self._preset_dropdown.grid(row=1, column=3, padx=5, pady=5, sticky='w')

    def _create_gui_style_frame(self):
        self._gui_style_frame = ttk.Frame(self._general_tab)
        self._gui_style_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # LABEL
        self._gui_style_label = ttk.Label(self._gui_style_frame, text="GUI Theme:")
        self._gui_style_label.config(anchor='center')
        self._gui_style_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        # DROPDOWN
        self._gui_style_options = [theme_name for theme_name in STYLE_DICT]
        self._gui_style_value = tk.StringVar(self._gui_style_frame)
        self._gui_style_value.set(self._gui_style_options[0])
        self._gui_style_dropdown = ttk.Combobox(self._gui_style_frame, textvariable=self._gui_style_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._gui_style_dropdown['values'] = self._gui_style_options
        self._gui_style_dropdown['state'] = 'readonly'
        self._gui_style_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        # TRACE
        self._gui_style_value.trace('w', self._gui_style_change)
    
    ##################
    ### MODELS TAB ###
    ##################

    def _model_select(self, *args):
        if(self._model_selection_value.get() == "Banjo-Kazooie"):
            self._other_model_frame.grid_remove()
            self._bk_model_dropdown.grid(row=1, column=0, padx=5, pady=5, sticky='w')
            self._bk_color_frame.grid(row=2, column=0, columnspan=6, padx=5, pady=5, sticky='w')
        elif(self._model_selection_value.get() == "Other Model"):
            self._bk_color_frame.grid_remove()
            self._bk_model_dropdown.grid_remove()
            self._other_model_frame.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky='w')
        else:
            print("Model Select Option Does Not Exist")
            raise SystemError("Model Select Option Does Not Exist")

    def _create_models_tab(self):
        self._models_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._models_tab, text="Models")
        self._models_tab_control = ttk.Notebook(self._models_tab, width=self._app_window.winfo_width())
        self._create_player_model_tab()
        self._create_level_model_tab()
        self._create_sprites_tab()
        self._create_model_swaps_tab()
        self._models_tab_control.pack(expand=1, fill="both")
    
    def _create_player_model_tab(self):
        self._player_model_tab = ttk.Frame(self._models_tab_control)
        self._models_tab_control.add(self._player_model_tab, text="Player")
        self._player_model_frame = ttk.Frame(self._player_model_tab)
        self._player_model_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # MODEL SELECTION
        self._model_selection_options = ["Banjo-Kazooie", "Other Model"]
        self._model_selection_value = tk.StringVar(self._player_model_frame)
        self._model_selection_value.set(self._model_selection_options[0])
        self._model_selection_dropdown = ttk.Combobox(self._player_model_frame, textvariable=self._model_selection_value, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._model_selection_dropdown['values'] = self._model_selection_options
        self._model_selection_dropdown['state'] = 'readonly'
        self._model_selection_dropdown.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self._create_bk_color_selection_frame()
        self._create_other_model_selection_frame()
        # TRACE(S)
        self._model_selection_value.trace('w', self._model_select)
    
    def _update_bk_model_colors(self, *args):
        if(self._bk_model_preset_value.get() in ["Random Preset", "Random Colors"]):
            self._banjo_fur_value.set("?")
            self._banjo_skin_value.set("?")
            self._banjo_eyes_value.set("?")
            self._banjo_eyelids_value.set("?")
            self._banjo_shorts_value.set("?")
            self._banjo_nose_value.set("?")
            self._kazooie_primary_value.set("?")
            self._kazooie_secondary_value.set("?")
            self._kazooie_tuff_value.set("?")
            self._kazooie_eyes_value.set("?")
            self._kazooie_beak_legs_value.set("?")
            self._shark_tooth_value.set("?")
            self._mouths_value.set("?")
            self._backpack_value.set("?")
            self._turbo_talon_trainers_value.set("?")
            self._wading_boots_value.set("?")
        else:
            file_name = f"{self._bk_model_preset_folder}{(self._bk_model_preset_value.get()).replace(' ', '_')}.json"
            with open(file_name, "r") as json_file:
                json_data = json.load(json_file)
            self._banjo_fur_value.set(json_data["Banjo_Fur"]["Color_Ratio"])
            self._banjo_skin_value.set(json_data["Banjo_Skin"]["Color_Ratio"])
            self._banjo_eyes_value.set(json_data["Banjo_Eyes"]["Color_Ratio"])
            self._banjo_eyelids_value.set(json_data["Banjo_Eyelids"]["Color_Ratio"])
            self._banjo_shorts_value.set(json_data["Banjo_Shorts"]["Color_Ratio"])
            self._banjo_nose_value.set(json_data["Banjo_Nose"]["Color_Ratio"])
            self._kazooie_primary_value.set(json_data["Kazooie_Feathers_Primary"]["Color_Ratio"])
            self._kazooie_secondary_value.set(json_data["Kazooie_Feathers_Secondary"]["Color_Ratio"])
            self._kazooie_tuff_value.set(json_data["Kazooie_Head_Feather"]["Color_Ratio"])
            self._kazooie_eyes_value.set(json_data["Kazooie_Eyes"]["Color_Ratio"])
            self._kazooie_beak_legs_value.set(json_data["Kazooie_Beak/Legs"]["Color_Ratio"])
            self._shark_tooth_value.set(json_data["Banjo_Necklace_Tooth"]["Color_Ratio"])
            self._mouths_value.set(json_data["Mouths"]["Color_Ratio"])
            self._backpack_value.set(json_data["Backpack"]["Color_Ratio"])
            self._turbo_talon_trainers_value.set(json_data["Turbo_Talon_Trainers"]["Color_Ratio"])
            self._wading_boots_value.set(json_data["Wading_Boots"]["Color_Ratio"])
    
    def _create_bk_color_selection_frame(self):
        self._bk_model_preset_options = [file_name.replace(".json", "").replace("_", " ")
                                         for file_name in listdir(self._bk_model_preset_folder)]
        self._bk_model_preset_options.remove("Default")
        self._bk_model_preset_options.insert(0, "Default")
        self._bk_model_preset_options.insert(1, "Random Preset")
        self._bk_model_preset_options.insert(2, "Random Colors")
        self._bk_model_preset_value = tk.StringVar(self._player_model_frame)
        self._bk_model_preset_value.set(self._bk_model_preset_options[0])
        self._bk_model_dropdown = ttk.Combobox(self._player_model_frame, textvariable=self._bk_model_preset_value, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE), width=30)
        self._bk_model_dropdown['values'] = self._bk_model_preset_options
        self._bk_model_dropdown['state'] = 'readonly'
        self._bk_model_dropdown.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self._bk_color_frame = ttk.LabelFrame(self._player_model_frame, text="BK Model Colors")
        # Banjo Fur
        self._banjo_fur_text = ttk.Label(self._bk_color_frame, text="Banjo's Fur", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_fur_text.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self._banjo_fur_value = tk.StringVar(self._bk_color_frame)
        self._banjo_fur_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_fur_value, width=9)
        self._banjo_fur_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        # Banjo Skin
        self._banjo_skin_text = ttk.Label(self._bk_color_frame, text="Banjo's Skin", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_skin_text.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self._banjo_skin_value = tk.StringVar(self._bk_color_frame)
        self._banjo_skin_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_skin_value, width=9)
        self._banjo_skin_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        # Banjo Eyes
        self._banjo_eyes_text = ttk.Label(self._bk_color_frame, text="Banjo's Eye Color", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_eyes_text.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self._banjo_eyes_value = tk.StringVar(self._bk_color_frame)
        self._banjo_eyes_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_eyes_value, width=9)
        self._banjo_eyes_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        # Banjo Eyelids
        self._banjo_eyelids_text = ttk.Label(self._bk_color_frame, text="Banjo's Eyelids", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_eyelids_text.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self._banjo_eyelids_value = tk.StringVar(self._bk_color_frame)
        self._banjo_eyelids_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_eyelids_value, width=9)
        self._banjo_eyelids_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        # Banjo Shorts
        self._banjo_shorts_text = ttk.Label(self._bk_color_frame, text="Banjo's Shorts", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_shorts_text.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self._banjo_shorts_value = tk.StringVar(self._bk_color_frame)
        self._banjo_shorts_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_shorts_value, width=9)
        self._banjo_shorts_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        # Banjo Nose
        self._banjo_nose_text = ttk.Label(self._bk_color_frame, text="Banjo's Nose", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_nose_text.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self._banjo_nose_value = tk.StringVar(self._bk_color_frame)
        self._banjo_nose_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_nose_value, width=9)
        self._banjo_nose_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        # Kazooie Primary
        self._kazooie_primary_text = ttk.Label(self._bk_color_frame, text="Kazooie's Feathers Primary", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._kazooie_primary_text.grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self._kazooie_primary_value = tk.StringVar(self._bk_color_frame)
        self._kazooie_primary_entry = tk.Entry(self._bk_color_frame, textvariable=self._kazooie_primary_value, width=9)
        self._kazooie_primary_entry.grid(row=0, column=3, padx=5, pady=5, sticky='w')
        # Kazooie Secondary
        self._kazooie_secondary_text = ttk.Label(self._bk_color_frame, text="Kazooie's Feathers Secondary", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._kazooie_secondary_text.grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self._kazooie_secondary_value = tk.StringVar(self._bk_color_frame)
        self._kazooie_secondary_entry = tk.Entry(self._bk_color_frame, textvariable=self._kazooie_secondary_value, width=9)
        self._kazooie_secondary_entry.grid(row=1, column=3, padx=5, pady=5, sticky='w')
        # Kazooie Tuff
        self._kazooie_tuff_text = ttk.Label(self._bk_color_frame, text="Kazooie's Feather Tuff", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._kazooie_tuff_text.grid(row=2, column=2, padx=5, pady=5, sticky='w')
        self._kazooie_tuff_value = tk.StringVar(self._bk_color_frame)
        self._kazooie_tuff_entry = tk.Entry(self._bk_color_frame, textvariable=self._kazooie_tuff_value, width=9)
        self._kazooie_tuff_entry.grid(row=2, column=3, padx=5, pady=5, sticky='w')
        # Kazooie Eyes
        self._kazooie_eyes_text = ttk.Label(self._bk_color_frame, text="Kazooie's Eye Color", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._kazooie_eyes_text.grid(row=3, column=2, padx=5, pady=5, sticky='w')
        self._kazooie_eyes_value = tk.StringVar(self._bk_color_frame)
        self._kazooie_eyes_entry = tk.Entry(self._bk_color_frame, textvariable=self._kazooie_eyes_value, width=9)
        self._kazooie_eyes_entry.grid(row=3, column=3, padx=5, pady=5, sticky='w')
        # Kazooie Beak/Legs
        self._kazooie_beak_legs_text = ttk.Label(self._bk_color_frame, text="Kazooie's Beak & Legs", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._kazooie_beak_legs_text.grid(row=4, column=2, padx=5, pady=5, sticky='w')
        self._kazooie_beak_legs_value = tk.StringVar(self._bk_color_frame)
        self._kazooie_beak_legs_entry = tk.Entry(self._bk_color_frame, textvariable=self._kazooie_beak_legs_value, width=9)
        self._kazooie_beak_legs_entry.grid(row=4, column=3, padx=5, pady=5, sticky='w')
        # Shark Tooth
        self._shark_tooth_text = ttk.Label(self._bk_color_frame, text="Shark Tooth", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._shark_tooth_text.grid(row=0, column=4, padx=5, pady=5, sticky='w')
        self._shark_tooth_value = tk.StringVar(self._bk_color_frame)
        self._shark_tooth_entry = tk.Entry(self._bk_color_frame, textvariable=self._shark_tooth_value, width=9)
        self._shark_tooth_entry.grid(row=0, column=5, padx=5, pady=5, sticky='w')
        # Mouths
        self._mouths_text = ttk.Label(self._bk_color_frame, text="B&K's Mouths", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._mouths_text.grid(row=1, column=4, padx=5, pady=5, sticky='w')
        self._mouths_value = tk.StringVar(self._bk_color_frame)
        self._mouths_entry = tk.Entry(self._bk_color_frame, textvariable=self._mouths_value, width=9)
        self._mouths_entry.grid(row=1, column=5, padx=5, pady=5, sticky='w')
        # Backpack
        self._backpack_text = ttk.Label(self._bk_color_frame, text="Backpack", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._backpack_text.grid(row=2, column=4, padx=5, pady=5, sticky='w')
        self._backpack_value = tk.StringVar(self._bk_color_frame)
        self._backpack_entry = tk.Entry(self._bk_color_frame, textvariable=self._backpack_value, width=9)
        self._backpack_entry.grid(row=2, column=5, padx=5, pady=5, sticky='w')
        # Turbo Talon Trainers
        self._turbo_talon_trainers_text = ttk.Label(self._bk_color_frame, text="Turbo Talon Trainers", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._turbo_talon_trainers_text.grid(row=3, column=4, padx=5, pady=5, sticky='w')
        self._turbo_talon_trainers_value = tk.StringVar(self._bk_color_frame)
        self._turbo_talon_trainers_entry = tk.Entry(self._bk_color_frame, textvariable=self._turbo_talon_trainers_value, width=9)
        self._turbo_talon_trainers_entry.grid(row=3, column=5, padx=5, pady=5, sticky='w')
        # Wading Boots
        self._wading_boots_text = ttk.Label(self._bk_color_frame, text="Wading Boots", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._wading_boots_text.grid(row=4, column=4, padx=5, pady=5, sticky='w')
        self._wading_boots_value = tk.StringVar(self._bk_color_frame)
        self._wading_boots_entry = tk.Entry(self._bk_color_frame, textvariable=self._wading_boots_value, width=9)
        self._wading_boots_entry.grid(row=4, column=5, padx=5, pady=5, sticky='w')
        self._bk_color_frame.grid(row=2, column=0, columnspan=6, padx=5, pady=5, sticky='w')
        # TRACE(S)
        self._update_bk_model_colors()
        self._bk_model_preset_value.trace('w', self._update_bk_model_colors)

    def _create_other_model_selection_frame(self):
        self._other_model_frame = ttk.Frame(self._player_model_frame)
        self._other_model_dict = {}
        for model_count, model_name in enumerate(sorted(MODELS_DICT)):
            self._other_model_dict[model_name] = tk.IntVar()
            temp_checkbutton = ttk.Checkbutton(self._other_model_frame, text=model_name, variable=self._other_model_dict[model_name], width=13)
            temp_checkbutton.grid(row=(model_count // 5) + 1, column=(model_count % 5), padx=0, pady=0, sticky='w')
    
    def _create_level_model_tab(self):
        self._level_model_tab = ttk.Frame(self._models_tab_control)
        self._models_tab_control.add(self._level_model_tab, text="Levels")
        self._level_model_frame = ttk.Frame(self._level_model_tab)
        self._level_model_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Level Model Colors
        self._level_model_color_text = ttk.Label(self._level_model_frame, text="Level Model Colors:", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._level_model_color_text.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self._level_model_color_options = ["Default", "Random Colors", "Random Preset", "Order Determined Preset"]
        self._level_model_color_value = tk.StringVar(self._level_model_frame)
        self._level_model_color_value.set(self._level_model_color_options[0])
        self._level_model_color_dropdown = ttk.Combobox(self._level_model_frame, textvariable=self._level_model_color_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=20)
        self._level_model_color_dropdown['values'] = self._level_model_color_options
        self._level_model_color_dropdown['state'] = 'readonly'
        self._level_model_color_dropdown.grid(row=0, column=1, padx=5, pady=5)
        # Skyboxes
        self._skybox_text = ttk.Label(self._level_model_frame, text="Skybox Colors:", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._skybox_text.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self._skybox_options = ["Default", "Random Colors", "Random Skybox"]
        self._skybox_value = tk.StringVar(self._level_model_frame)
        self._skybox_value.set(self._skybox_options[0])
        self._skybox_dropdown = ttk.Combobox(self._level_model_frame, textvariable=self._skybox_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=20)
        self._skybox_dropdown['values'] = self._skybox_options
        self._skybox_dropdown['state'] = 'readonly'
        self._skybox_dropdown.grid(row=1, column=1, padx=5, pady=5)
    
    def _create_sprites_tab(self):
        self._sprites_tab = ttk.Frame(self._models_tab_control)
        self._models_tab_control.add(self._sprites_tab, text="Sprites")
        self._sprites_frame = ttk.Frame(self._sprites_tab)
        self._sprites_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Talking Sprites
        self._talking_sprites_text = ttk.Label(self._sprites_frame, text="Talking Sprites:", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._talking_sprites_text.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self._talking_sprites_options = ["Default", "Shuffle Talking Sprites", "Random Talking Sprites"]
        self._talking_sprites_value = tk.StringVar(self._sprites_frame)
        self._talking_sprites_value.set(self._talking_sprites_options[0])
        self._talking_sprites_dropdown = ttk.Combobox(self._sprites_frame, textvariable=self._talking_sprites_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=26)
        self._talking_sprites_dropdown['values'] = self._talking_sprites_options
        self._talking_sprites_dropdown['state'] = 'readonly'
        self._talking_sprites_dropdown.grid(row=0, column=1, padx=5, pady=5)
        # Pause Font
        self._pause_font_text = ttk.Label(self._sprites_frame, text="Pause Font:", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._pause_font_text.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self._pause_font_options = ["Default", "Random Pause Font"]
        self._pause_font_value = tk.StringVar(self._sprites_frame)
        self._pause_font_value.set(self._pause_font_options[0])
        self._pause_font_dropdown = ttk.Combobox(self._sprites_frame, textvariable=self._pause_font_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=26)
        self._pause_font_dropdown['values'] = self._pause_font_options
        self._pause_font_dropdown['state'] = 'readonly'
        self._pause_font_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        # Honeycomb Sprites
        self._honeycomb_sprites_text = ttk.Label(self._sprites_frame, text="Honeycomb Sprites:", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._honeycomb_sprites_text.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self._honeycomb_sprites_options = ["Default", "Shuffle Honeycomb Sprites", "Random Honeycomb Sprites"]
        self._honeycomb_sprites_value = tk.StringVar(self._sprites_frame)
        self._honeycomb_sprites_value.set(self._honeycomb_sprites_options[0])
        self._honeycomb_sprites_dropdown = ttk.Combobox(self._sprites_frame, textvariable=self._honeycomb_sprites_value, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=26)
        self._honeycomb_sprites_dropdown['values'] = self._honeycomb_sprites_options
        self._honeycomb_sprites_dropdown['state'] = 'readonly'
        self._honeycomb_sprites_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        # Timer Sprite
        self._timer_sprite_text = ttk.Label(self._sprites_frame, text="Timer Sprite:", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._timer_sprite_text.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self._timer_sprite_options = ["Default", "Beta Timer Sprite", "Random Timer Sprite"]
        self._timer_sprite_value = tk.StringVar(self._sprites_frame)
        self._timer_sprite_value.set(self._timer_sprite_options[0])
        self._timer_sprite_dropdown = ttk.Combobox(self._sprites_frame, textvariable=self._timer_sprite_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=26)
        self._timer_sprite_dropdown['values'] = self._timer_sprite_options
        self._timer_sprite_dropdown['state'] = 'readonly'
        self._timer_sprite_dropdown.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    
    def _create_model_swaps_tab(self):
        self._model_swaps_tab = ttk.Frame(self._models_tab_control)
        self._models_tab_control.add(self._model_swaps_tab, text="Model Swaps")
        self._model_swaps_frame = ttk.Frame(self._model_swaps_tab)
        self._model_swaps_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # LIST MODEL SWAPS
    
    ##################
    ### SOUNDS TAB ###
    ##################

    def _create_sounds_tab(self):
        self._sounds_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._sounds_tab, text="Sounds")
        self._sounds_tab_control = ttk.Notebook(self._sounds_tab, width=self._app_window.winfo_width())
        self._create_sound_effects_tab()
        self._create_characters_talking_tab()
        self._create_short_jingle_tab()
        self._create_long_jingle_tab()
        self._create_mini_game_music_tab()
        self._create_level_music_tab()
        self._sounds_tab_control.pack(expand=1, fill="both")
    
    def _create_sound_effects_tab(self):
        self._sound_effects_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._sound_effects_tab, text="Sound Effects")
        self._sound_effects_frame = ttk.Frame(self._sound_effects_tab)
        self._sound_effects_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # LIST SOUND EFFECTS
    
    def _create_characters_talking_tab(self):
        self._characters_talking_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._characters_talking_tab, text="Characters Talking")
        self._characters_talking_frame = ttk.Frame(self._characters_talking_tab)
        self._characters_talking_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # LIST CHARACTER TALKING SOUNDS
    
    def _create_short_jingle_tab(self):
        self._short_jingle_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._short_jingle_tab, text="Short Jingle")
        self._short_jingle_frame = ttk.Frame(self._short_jingle_tab)
        self._short_jingle_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # LIST SHORT JINGLE SOUNDS
    
    def _create_long_jingle_tab(self):
        self._long_jingle_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._long_jingle_tab, text="Long Jingle")
        self._long_jingle_frame = ttk.Frame(self._long_jingle_tab)
        self._long_jingle_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # LIST LONG JINGLE SOUNDS
    
    def _create_mini_game_music_tab(self):
        self._mini_game_music_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._mini_game_music_tab, text="Mini-Game Music")
        self._mini_game_music_frame = ttk.Frame(self._mini_game_music_tab)
        self._mini_game_music_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # LIST MINI-GAME SOUNDS
    
    def _create_level_music_tab(self):
        self._level_music_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._level_music_tab, text="Level Music")
        self._level_music_frame = ttk.Frame(self._level_music_tab)
        self._level_music_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # LIST LEVEL MUSIC SOUNDS
    
    ###################
    ### ENEMIES TAB ###
    ###################

    def _create_enemies_tab(self):
        self._enemies_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._enemies_tab, text="Enemies")
        self._enemies_tab_control = ttk.Notebook(self._enemies_tab, width=self._app_window.winfo_width())
        self._create_enemy_selection_tab()
        self._create_enemy_vulnerability_tab()
        self._create_enemy_other_tab()
        self._enemies_tab_control.pack(expand=1, fill="both")
    
    def _create_enemy_selection_tab(self):
        self._enemy_selection_tab = ttk.Frame(self._enemies_tab_control)
        self._enemies_tab_control.add(self._enemy_selection_tab, text="Selection")
        self._enemy_selection_frame = ttk.Frame(self._enemy_selection_tab)
        self._enemy_selection_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # LIST ENEMIES
    
    def _create_enemy_vulnerability_tab(self):
        self._enemy_vulnerability_tab = ttk.Frame(self._enemies_tab_control)
        self._enemies_tab_control.add(self._enemy_vulnerability_tab, text="Vulnerability")
        self._enemy_vulnerability_frame = ttk.Frame(self._enemy_vulnerability_tab)
        self._enemy_vulnerability_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # VULNERABILITY OPTIONS
        # HINTS FOR VULNERABILITIES?
    
    def _create_enemy_other_tab(self):
        self._enemy_other_tab = ttk.Frame(self._enemies_tab_control)
        self._enemies_tab_control.add(self._enemy_other_tab, text="Enemies Other")
        self._enemy_other_frame = ttk.Frame(self._enemy_other_tab)
        self._enemy_other_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    #######################
    ### PROGRESSION TAB ###
    #######################

    def _create_progression_tab(self):
        self._progression_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._progression_tab, text="Progression")
        self._progression_tab_control = ttk.Notebook(self._progression_tab, width=self._app_window.winfo_width())
        self._create_requirements_tab()
        self._create_collectables_tab()
        self._create_carrying_items_tab()
        self._create_moves_tab()
        self._create_cheats_tab()
        self._progression_tab_control.pack(expand=1, fill="both")
    
    def _create_alternate_win_condition_frame(self):
        self._win_conidition_frame = ttk.Frame(self._requirements_frame)
        self._win_conidition_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self._win_condition_text = ttk.Label(self._win_conidition_frame, text="Alternate Ending Credits Condition:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._win_condition_text.grid(row=0, column=0, padx=5, pady=2, sticky='w')
        self._win_condition_options = ["Default Win Condition", "Jiggy Count", "Note Count", "Token Count", "Empty Honeycomb Count"]
        self._win_condition_value = tk.StringVar(self._win_conidition_frame)
        self._win_condition_value.set(self._win_condition_options[0])
        self._win_condition_dropdown = ttk.Combobox(self._win_conidition_frame, textvariable=self._win_condition_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=25)
        self._win_condition_dropdown['values'] = self._win_condition_options
        self._win_condition_dropdown['state'] = 'readonly'
        self._win_condition_dropdown.grid(row=0, column=1, padx=5)

    def _create_jigsaw_puzzles_frame(self):
        self._jigsaw_puzzles_frame = ttk.Frame(self._requirements_frame)
        self._jigsaw_puzzles_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Progression Costs
        self._jigsaw_puzzles_requirement_text = ttk.Label(self._jigsaw_puzzles_frame, text="Puzzle Progression:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._jigsaw_puzzles_requirement_text.grid(row=0, column=0, padx=5, pady=2, sticky='w')
        self._jigsaw_puzzles_requirement_options = ["Default Costs", "Final Puzzle Only (Open Worlds)", "Scaling Item Costs", "Random Item Costs"]
        self._jigsaw_puzzles_requirement_value = tk.StringVar(self._jigsaw_puzzles_frame)
        self._jigsaw_puzzles_requirement_value.set(self._jigsaw_puzzles_requirement_options[0])
        self._jigsaw_puzzles_requirement_dropdown = ttk.Combobox(self._jigsaw_puzzles_frame, textvariable=self._jigsaw_puzzles_requirement_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=25)
        self._jigsaw_puzzles_requirement_dropdown['values'] = self._jigsaw_puzzles_requirement_options
        self._jigsaw_puzzles_requirement_dropdown['state'] = 'readonly'
        self._jigsaw_puzzles_requirement_dropdown.grid(row=0, column=1, columnspan=2, padx=5)
        # Which Item?
        self._jigsaw_puzzles_item_text = ttk.Label(self._jigsaw_puzzles_frame, text="Puzzle Item Requirement:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._jigsaw_puzzles_item_text.grid(row=1, column=0, padx=5, pady=2, sticky='w')
        self._jigsaw_puzzles_item_options = ["Jiggies (Default)"]
        self._jigsaw_puzzles_item_value = tk.StringVar(self._jigsaw_puzzles_frame)
        self._jigsaw_puzzles_item_value.set(self._jigsaw_puzzles_item_options[0])
        self._jigsaw_puzzles_item_dropdown = ttk.Combobox(self._jigsaw_puzzles_frame, textvariable=self._jigsaw_puzzles_item_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=25)
        self._jigsaw_puzzles_item_dropdown['values'] = self._jigsaw_puzzles_item_options
        self._jigsaw_puzzles_item_dropdown['state'] = 'readonly'
        self._jigsaw_puzzles_item_dropdown.grid(row=1, column=1, columnspan=2, padx=5)
        # Costs
        self._puzzle_requirement_text = ttk.Label(self._jigsaw_puzzles_frame, text="Final Puzzle Cost", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._puzzle_requirement_text.grid(row=2, column=0, padx=5, pady=2, sticky='w')
        self._jiggy_lower_limit_text = ttk.Label(self._jigsaw_puzzles_frame, text="Lower Limit:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._jiggy_lower_limit_text.grid(row=2, column=1, padx=5, pady=2)
        self._puzzle_lower_limit_value = tk.StringVar()
        self._puzzle_lower_limit_value.set("")
        self._puzzle_lower_limit_entry = tk.Entry(self._jigsaw_puzzles_frame, textvariable=self._puzzle_lower_limit_value, width=8, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._puzzle_lower_limit_entry.grid(row=2, column=2, padx=5, pady=2)
        self._jiggy_upper_limit_text = ttk.Label(self._jigsaw_puzzles_frame, text="Upper Limit:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._jiggy_upper_limit_text.grid(row=2, column=3, padx=5, pady=2)
        self._puzzle_upper_limit_value = tk.StringVar()
        self._puzzle_upper_limit_value.set("")
        self._puzzle_upper_limit_entry = tk.Entry(self._jigsaw_puzzles_frame, textvariable=self._puzzle_upper_limit_value, width=8, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._puzzle_upper_limit_entry.grid(row=2, column=4, padx=5, pady=2)

    def _create_note_doors_frame(self):
        self._note_doors_frame = ttk.Frame(self._requirements_frame)
        self._note_doors_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Progression Costs
        self._note_doors_requirement_text = ttk.Label(self._note_doors_frame, text="Door Progression:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._note_doors_requirement_text.grid(row=0, column=0, padx=5, pady=2, sticky='w')
        self._note_doors_requirement_options = ["Default Costs", "Free (No Note Doors)", "Final Note Door Only (Open Lair)", "Scaling Item Counts", "Random Item Counts"]
        self._note_doors_requirement_value = tk.StringVar(self._note_doors_frame)
        self._note_doors_requirement_value.set(self._note_doors_requirement_options[0])
        self._note_doors_requirement_dropdown = ttk.Combobox(self._note_doors_frame, textvariable=self._note_doors_requirement_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=25)
        self._note_doors_requirement_dropdown['values'] = self._note_doors_requirement_options
        self._note_doors_requirement_dropdown['state'] = 'readonly'
        self._note_doors_requirement_dropdown.grid(row=0, column=1, columnspan=2, padx=5)
        # Which Item?
        self._note_doors_item_text = ttk.Label(self._note_doors_frame, text="Door Item Requirement:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._note_doors_item_text.grid(row=1, column=0, padx=5, pady=2, sticky='w')
        self._note_doors_item_options = ["Notes (Default)", "Jiggies", "Empty Honeycombs", "Mumbo Tokens"]
        self._note_doors_item_value = tk.StringVar(self._note_doors_frame)
        self._note_doors_item_value.set(self._note_doors_item_options[0])
        self._note_doors_item_dropdown = ttk.Combobox(self._note_doors_frame, textvariable=self._note_doors_item_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=25)
        self._note_doors_item_dropdown['values'] = self._note_doors_item_options
        self._note_doors_item_dropdown['state'] = 'readonly'
        self._note_doors_item_dropdown.grid(row=1, column=1, columnspan=2, padx=5)
        # Costs
        self._door_requirement_text = ttk.Label(self._note_doors_frame, text="Final Door Requirement", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._door_requirement_text.grid(row=2, column=0, padx=5, pady=2, sticky='w')
        self._note_lower_limit_text = ttk.Label(self._note_doors_frame, text="Lower Limit:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._note_lower_limit_text.grid(row=2, column=1, padx=5, pady=2)
        self._door_lower_limit_value = tk.StringVar()
        self._door_lower_limit_value.set("")
        self._door_lower_limit_entry = tk.Entry(self._note_doors_frame, textvariable=self._door_lower_limit_value, width=8, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._door_lower_limit_entry.grid(row=2, column=2, padx=5, pady=2)
        self._note_upper_limit_text = ttk.Label(self._note_doors_frame, text="Upper Limit:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._note_upper_limit_text.grid(row=2, column=3, padx=5, pady=2)
        self._door_upper_limit_value = tk.StringVar()
        self._door_upper_limit_value.set("")
        self._door_upper_limit_entry = tk.Entry(self._note_doors_frame, textvariable=self._door_upper_limit_value, width=8, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._door_upper_limit_entry.grid(row=2, column=4, padx=5, pady=2)

    def _create_mumbo_costs_frame(self):
        self._mumbo_costs_frame = ttk.Frame(self._requirements_frame)
        self._mumbo_costs_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Progression Costs
        self._mumbo_costs_requirement_text = ttk.Label(self._mumbo_costs_frame, text="Transformation Progression:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._mumbo_costs_requirement_text.grid(row=0, column=0, padx=5, pady=2, sticky='w')
        self._mumbo_costs_requirement_options = ["Default Costs", "Free (No Transformation Cost)", "Scaling Transformation Costs", "Random Transformation Costs"]
        self._mumbo_costs_requirement_value = tk.StringVar(self._mumbo_costs_frame)
        self._mumbo_costs_requirement_value.set(self._mumbo_costs_requirement_options[0])
        self._mumbo_costs_requirement_dropdown = ttk.Combobox(self._mumbo_costs_frame, textvariable=self._mumbo_costs_requirement_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=25)
        self._mumbo_costs_requirement_dropdown['values'] = self._mumbo_costs_requirement_options
        self._mumbo_costs_requirement_dropdown['state'] = 'readonly'
        self._mumbo_costs_requirement_dropdown.grid(row=0, column=1, columnspan=2, padx=5)
        # Which Item?
        self._mumbo_costs_item_text = ttk.Label(self._mumbo_costs_frame, text="Transformation Item Requirement:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._mumbo_costs_item_text.grid(row=1, column=0, padx=5, pady=2, sticky='w')
        self._mumbo_costs_item_options = ["Notes (Default)", "Jiggies", "Empty Honeycombs", "Mumbo Tokens"]
        self._mumbo_costs_item_value = tk.StringVar(self._mumbo_costs_frame)
        self._mumbo_costs_item_value.set(self._mumbo_costs_item_options[0])
        self._mumbo_costs_item_dropdown = ttk.Combobox(self._mumbo_costs_frame, textvariable=self._mumbo_costs_item_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=25)
        self._mumbo_costs_item_dropdown['values'] = self._mumbo_costs_item_options
        self._mumbo_costs_item_dropdown['state'] = 'readonly'
        self._mumbo_costs_item_dropdown.grid(row=1, column=1, columnspan=2, padx=5)
        # Costs
        self._mumbo_requirement_text = ttk.Label(self._mumbo_costs_frame, text="Final Transformation Requirement", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._mumbo_requirement_text.grid(row=2, column=0, padx=5, pady=2, sticky='w')
        self._token_lower_limit_text = ttk.Label(self._mumbo_costs_frame, text="Lower Limit:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._token_lower_limit_text.grid(row=2, column=1, padx=5, pady=2)
        self._mumbo_lower_limit_value = tk.StringVar()
        self._mumbo_lower_limit_value.set("")
        self._mumbo_lower_limit_entry = tk.Entry(self._mumbo_costs_frame, textvariable=self._mumbo_lower_limit_value, width=8, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._mumbo_lower_limit_entry.grid(row=2, column=2, padx=5, pady=2)
        self._token_upper_limit_text = ttk.Label(self._mumbo_costs_frame, text="Upper Limit:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._token_upper_limit_text.grid(row=2, column=3, padx=5, pady=2)
        self._mumbo_upper_limit_value = tk.StringVar()
        self._mumbo_upper_limit_value.set("")
        self._mumbo_upper_limit_entry = tk.Entry(self._mumbo_costs_frame, textvariable=self._mumbo_upper_limit_value, width=8, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._mumbo_upper_limit_entry.grid(row=2, column=4, padx=5, pady=2)

    def _create_honeycomb_health_frame(self):
        self._honeycomb_health_frame = ttk.Frame(self._requirements_frame)
        self._honeycomb_health_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Which Item?
        self._honeycomb_health_item_text = ttk.Label(self._honeycomb_health_frame, text="Gain Health Item Requirement:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_health_item_text.grid(row=0, column=0, padx=5, pady=2, sticky='w')
        self._honeycomb_health_item_options = ["Notes (Default)", "Jiggies", "Empty Honeycombs", "Mumbo Tokens"]
        self._honeycomb_health_item_value = tk.StringVar(self._honeycomb_health_frame)
        self._honeycomb_health_item_value.set(self._honeycomb_health_item_options[0])
        self._honeycomb_health_item_dropdown = ttk.Combobox(self._honeycomb_health_frame, textvariable=self._honeycomb_health_item_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=25)
        self._honeycomb_health_item_dropdown['values'] = self._honeycomb_health_item_options
        self._honeycomb_health_item_dropdown['state'] = 'readonly'
        self._honeycomb_health_item_dropdown.grid(row=0, column=1, columnspan=2, padx=5)
        # Starting Health
        self._honeycomb_requirement_text = ttk.Label(self._honeycomb_health_frame, text="Starting Health", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_requirement_text.grid(row=1, column=0, padx=5, pady=2, sticky='w')
        self._honeycomb_lower_limit_text = ttk.Label(self._honeycomb_health_frame, text="Lower Limit:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_lower_limit_text.grid(row=1, column=1, padx=5, pady=2)
        self._honeycomb_lower_limit_value = tk.StringVar()
        self._honeycomb_lower_limit_value.set("")
        self._honeycomb_lower_limit_entry = tk.Entry(self._honeycomb_health_frame, textvariable=self._honeycomb_lower_limit_value, width=8, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_lower_limit_entry.grid(row=1, column=2, padx=5, pady=2)
        self._honeycomb_upper_limit_text = ttk.Label(self._honeycomb_health_frame, text="Upper Limit:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_upper_limit_text.grid(row=1, column=3, padx=5, pady=2)
        self._honeycomb_upper_limit_value = tk.StringVar()
        self._honeycomb_upper_limit_value.set("")
        self._honeycomb_upper_limit_entry = tk.Entry(self._honeycomb_health_frame, textvariable=self._honeycomb_upper_limit_value, width=8, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_upper_limit_entry.grid(row=1, column=4, padx=5, pady=2)
        # Honeycombs To Gain Health
        self._honeycomb_requirement_text = ttk.Label(self._honeycomb_health_frame, text="Honeycombs To Gain Health", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_requirement_text.grid(row=2, column=0, padx=5, pady=2, sticky='w')
        self._honeycomb_lower_limit_text = ttk.Label(self._honeycomb_health_frame, text="Lower Limit:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_lower_limit_text.grid(row=2, column=1, padx=5, pady=2)
        self._honeycomb_lower_limit_value = tk.StringVar()
        self._honeycomb_lower_limit_value.set("")
        self._honeycomb_lower_limit_entry = tk.Entry(self._honeycomb_health_frame, textvariable=self._honeycomb_lower_limit_value, width=8, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_lower_limit_entry.grid(row=2, column=2, padx=5, pady=2)
        self._honeycomb_upper_limit_text = ttk.Label(self._honeycomb_health_frame, text="Upper Limit:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_upper_limit_text.grid(row=2, column=3, padx=5, pady=2)
        self._honeycomb_upper_limit_value = tk.StringVar()
        self._honeycomb_upper_limit_value.set("")
        self._honeycomb_upper_limit_entry = tk.Entry(self._honeycomb_health_frame, textvariable=self._honeycomb_upper_limit_value, width=8, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_upper_limit_entry.grid(row=2, column=4, padx=5, pady=2)

    def _create_requirements_tab(self):
        self._requirements_tab = ttk.Frame(self._progression_tab_control)
        self._progression_tab_control.add(self._requirements_tab, text="Requirements")
        self._requirements_frame = ttk.Frame(self._requirements_tab)
        self._requirements_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self._create_alternate_win_condition_frame()
        self._create_jigsaw_puzzles_frame()
        self._create_note_doors_frame()
        self._create_mumbo_costs_frame()
        self._create_honeycomb_health_frame()
    
    def _create_collectables_tab(self):
        self._collectables_tab = ttk.Frame(self._progression_tab_control)
        self._progression_tab_control.add(self._collectables_tab, text="Collectable Locations")
        self._collectables_frame = ttk.Frame(self._collectables_tab)
        self._collectables_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Shuffle Group
        self._shuffle_type_text = ttk.Label(self._collectables_frame, text="Placement:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._shuffle_type_text.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        self._shuffle_group_text = ttk.Label(self._collectables_frame, text="Shuffle Group:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._shuffle_group_text.grid(row=0, column=3, padx=5, pady=5)
        # Jiggies
        self._jiggy_shuffle_text = ttk.Label(self._collectables_frame, text="Jiggies:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._jiggy_shuffle_text.grid(row=1, column=0, padx=5, pady=3, sticky='w')
        self._jiggy_shuffle_options = ["Default Locations", "Add To Shuffle Pool", "Pseudo Random XYZ Locations", "Only Spawned Jiggies"]
        self._jiggy_shuffle_value = tk.StringVar(self._collectables_frame)
        self._jiggy_shuffle_value.set(self._jiggy_shuffle_options[0])
        self._jiggy_shuffle_dropdown = ttk.Combobox(self._collectables_frame, textvariable=self._jiggy_shuffle_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=28)
        self._jiggy_shuffle_dropdown['values'] = self._jiggy_shuffle_options
        self._jiggy_shuffle_dropdown['state'] = 'readonly'
        self._jiggy_shuffle_dropdown.grid(row=1, column=1, columnspan=2, padx=5)
        self._jiggy_shuffle_group_value = tk.StringVar()
        self._jiggy_shuffle_group_value.set("A")
        self._jiggy_shuffle_group_entry = tk.Entry(self._collectables_frame, textvariable=self._jiggy_shuffle_group_value, width=8)
        self._jiggy_shuffle_group_entry.grid(row=1, column=3, padx=5)
        # Tokens
        self._token_shuffle_text = ttk.Label(self._collectables_frame, text="Mumbo Tokens:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._token_shuffle_text.grid(row=2, column=0, padx=5, pady=3, sticky='w')
        self._token_shuffle_options = ["Default Locations", "Add To Shuffle Pool", "Pseudo Random XYZ Locations", "No Mumbo Tokens"]
        self._token_shuffle_value = tk.StringVar(self._collectables_frame)
        self._token_shuffle_value.set(self._token_shuffle_options[0])
        self._token_shuffle_dropdown = ttk.Combobox(self._collectables_frame, textvariable=self._token_shuffle_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=28)
        self._token_shuffle_dropdown['values'] = self._token_shuffle_options
        self._token_shuffle_dropdown['state'] = 'readonly'
        self._token_shuffle_dropdown.grid(row=2, column=1, columnspan=2, padx=5)
        self._token_shuffle_group_value = tk.StringVar()
        self._token_shuffle_group_value.set("A")
        self._token_shuffle_group_entry = tk.Entry(self._collectables_frame, textvariable=self._token_shuffle_group_value, width=8)
        self._token_shuffle_group_entry.grid(row=2, column=3, padx=5)
        # Honeycombs
        self._honeycomb_shuffle_text = ttk.Label(self._collectables_frame, text="Empty Honeycombs:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._honeycomb_shuffle_text.grid(row=3, column=0, padx=5, pady=3, sticky='w')
        self._honeycomb_shuffle_options = ["Default Locations", "Add To Shuffle Pool", "Pseudo Random XYZ Locations", "Only Spawned Empty Honeycombs"]
        self._honeycomb_shuffle_value = tk.StringVar(self._collectables_frame)
        self._honeycomb_shuffle_value.set(self._honeycomb_shuffle_options[0])
        self._honeycomb_shuffle_dropdown = ttk.Combobox(self._collectables_frame, textvariable=self._honeycomb_shuffle_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=28)
        self._honeycomb_shuffle_dropdown['values'] = self._honeycomb_shuffle_options
        self._honeycomb_shuffle_dropdown['state'] = 'readonly'
        self._honeycomb_shuffle_dropdown.grid(row=3, column=1, columnspan=2, padx=5)
        self._honeycomb_shuffle_group_value = tk.StringVar()
        self._honeycomb_shuffle_group_value.set("A")
        self._honeycomb_shuffle_group_entry = tk.Entry(self._collectables_frame, textvariable=self._honeycomb_shuffle_group_value, width=8)
        self._honeycomb_shuffle_group_entry.grid(row=3, column=3, padx=5)
        # Jinjos
        self._jinjo_shuffle_text = ttk.Label(self._collectables_frame, text="Jinjos:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._jinjo_shuffle_text.grid(row=4, column=0, padx=5, pady=3, sticky='w')
        self._jinjo_shuffle_options = ["Default Locations", "Add To Shuffle Pool", "Pseudo Random XYZ Locations", "No Jinjos"]
        self._jinjo_shuffle_value = tk.StringVar(self._collectables_frame)
        self._jinjo_shuffle_value.set(self._jinjo_shuffle_options[0])
        self._jinjo_shuffle_dropdown = ttk.Combobox(self._collectables_frame, textvariable=self._jinjo_shuffle_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=28)
        self._jinjo_shuffle_dropdown['values'] = self._jinjo_shuffle_options
        self._jinjo_shuffle_dropdown['state'] = 'readonly'
        self._jinjo_shuffle_dropdown.grid(row=4, column=1, columnspan=2, padx=5)
        self._jinjo_shuffle_group_value = tk.StringVar()
        self._jinjo_shuffle_group_value.set("A")
        self._jinjo_shuffle_group_entry = tk.Entry(self._collectables_frame, textvariable=self._jinjo_shuffle_group_value, width=8)
        self._jinjo_shuffle_group_entry.grid(row=4, column=3, padx=5)
        # Extra Lives
        self._extra_life_shuffle_text = ttk.Label(self._collectables_frame, text="Extra Lives:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._extra_life_shuffle_text.grid(row=5, column=0, padx=5, pady=3, sticky='w')
        self._extra_life_shuffle_options = ["Default Locations", "Add To Shuffle Pool", "Pseudo Random XYZ Locations", "Only Spawned Extra Lives"]
        self._extra_life_shuffle_value = tk.StringVar(self._collectables_frame)
        self._extra_life_shuffle_value.set(self._extra_life_shuffle_options[0])
        self._extra_life_shuffle_dropdown = ttk.Combobox(self._collectables_frame, textvariable=self._extra_life_shuffle_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=28)
        self._extra_life_shuffle_dropdown['values'] = self._extra_life_shuffle_options
        self._extra_life_shuffle_dropdown['state'] = 'readonly'
        self._extra_life_shuffle_dropdown.grid(row=5, column=1, columnspan=2, padx=5)
        self._extra_lives_shuffle_group_value = tk.StringVar()
        self._extra_lives_shuffle_group_value.set("A")
        self._extra_lives_shuffle_group_entry = tk.Entry(self._collectables_frame, textvariable=self._extra_lives_shuffle_group_value, width=8)
        self._extra_lives_shuffle_group_entry.grid(row=5, column=3, padx=5)
        # FF Honeycombs
        self._ff_honeycombs_shuffle_text = ttk.Label(self._collectables_frame, text="FF Honeycombs:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._ff_honeycombs_shuffle_text.grid(row=6, column=0, padx=5, pady=3, sticky='w')
        self._ff_honeycombs_shuffle_options = ["Default Locations", "Add To Shuffle Pool", "Pseudo Random XYZ Locations", "Only Spawned Extra Lives"]
        self._ff_honeycombs_shuffle_value = tk.StringVar(self._collectables_frame)
        self._ff_honeycombs_shuffle_value.set(self._ff_honeycombs_shuffle_options[0])
        self._ff_honeycombs_shuffle_dropdown = ttk.Combobox(self._collectables_frame, textvariable=self._ff_honeycombs_shuffle_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=28)
        self._ff_honeycombs_shuffle_dropdown['values'] = self._ff_honeycombs_shuffle_options
        self._ff_honeycombs_shuffle_dropdown['state'] = 'readonly'
        self._ff_honeycombs_shuffle_dropdown.grid(row=6, column=1, columnspan=2, padx=5)
        self._extra_lives_shuffle_group_value = tk.StringVar()
        self._extra_lives_shuffle_group_value.set("A")
        self._extra_lives_shuffle_group_entry = tk.Entry(self._collectables_frame, textvariable=self._extra_lives_shuffle_group_value, width=8)
        self._extra_lives_shuffle_group_entry.grid(row=6, column=3, padx=5)
        # Notes
        self._note_shuffle_text = ttk.Label(self._collectables_frame, text="Notes:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._note_shuffle_text.grid(row=7, column=0, padx=5, pady=3, sticky='w')
        self._note_shuffle_options = ["Default Locations", "Add To Shuffle Pool", "Pseudo Random XYZ Locations", "No Notes"]
        self._note_shuffle_value = tk.StringVar(self._collectables_frame)
        self._note_shuffle_value.set(self._note_shuffle_options[0])
        self._note_shuffle_dropdown = ttk.Combobox(self._collectables_frame, textvariable=self._note_shuffle_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=28)
        self._note_shuffle_dropdown['values'] = self._note_shuffle_options
        self._note_shuffle_dropdown['state'] = 'readonly'
        self._note_shuffle_dropdown.grid(row=7, column=1, columnspan=2, padx=5)
        self._note_shuffle_group_value = tk.StringVar()
        self._note_shuffle_group_value.set("B")
        self._note_shuffle_group_entry = tk.Entry(self._collectables_frame, textvariable=self._note_shuffle_group_value, width=8)
        self._note_shuffle_group_entry.grid(row=7, column=3, padx=5)
        # Blue Eggs
        self._blue_eggs_shuffle_text = ttk.Label(self._collectables_frame, text="Blue Eggs:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._blue_eggs_shuffle_text.grid(row=8, column=0, padx=5, pady=3, sticky='w')
        self._blue_eggs_shuffle_options = ["Default Locations", "Add To Shuffle Pool", "Pseudo Random XYZ Locations", "No Blue Eggs"]
        self._blue_eggs_shuffle_value = tk.StringVar(self._collectables_frame)
        self._blue_eggs_shuffle_value.set(self._blue_eggs_shuffle_options[0])
        self._blue_eggs_shuffle_dropdown = ttk.Combobox(self._collectables_frame, textvariable=self._blue_eggs_shuffle_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=28)
        self._blue_eggs_shuffle_dropdown['values'] = self._blue_eggs_shuffle_options
        self._blue_eggs_shuffle_dropdown['state'] = 'readonly'
        self._blue_eggs_shuffle_dropdown.grid(row=8, column=1, columnspan=2, padx=5)
        self._blue_eggs_shuffle_group_value = tk.StringVar()
        self._blue_eggs_shuffle_group_value.set("B")
        self._blue_eggs_shuffle_group_entry = tk.Entry(self._collectables_frame, textvariable=self._blue_eggs_shuffle_group_value, width=8)
        self._blue_eggs_shuffle_group_entry.grid(row=8, column=3, padx=5)
        # Red Feathers
        self._red_feathers_shuffle_text = ttk.Label(self._collectables_frame, text="Red Feathers:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._red_feathers_shuffle_text.grid(row=9, column=0, padx=5, pady=3, sticky='w')
        self._red_feathers_shuffle_options = ["Default Locations", "Add To Shuffle Pool", "Pseudo Random XYZ Locations", "No Red Feathers"]
        self._red_feathers_shuffle_value = tk.StringVar(self._collectables_frame)
        self._red_feathers_shuffle_value.set(self._red_feathers_shuffle_options[0])
        self._red_feathers_shuffle_dropdown = ttk.Combobox(self._collectables_frame, textvariable=self._red_feathers_shuffle_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=28)
        self._red_feathers_shuffle_dropdown['values'] = self._red_feathers_shuffle_options
        self._red_feathers_shuffle_dropdown['state'] = 'readonly'
        self._red_feathers_shuffle_dropdown.grid(row=9, column=1, columnspan=2, padx=5)
        self._red_feathers_shuffle_group_value = tk.StringVar()
        self._red_feathers_shuffle_group_value.set("B")
        self._red_feathers_shuffle_group_entry = tk.Entry(self._collectables_frame, textvariable=self._red_feathers_shuffle_group_value, width=8)
        self._red_feathers_shuffle_group_entry.grid(row=9, column=3, padx=5)
        # Gold Feathers
        self._gold_feathers_shuffle_text = ttk.Label(self._collectables_frame, text="Gold Feathers:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._gold_feathers_shuffle_text.grid(row=10, column=0, padx=5, pady=3, sticky='w')
        self._gold_feathers_shuffle_options = ["Default Locations", "Add To Shuffle Pool", "Pseudo Random XYZ Locations", "No Gold Feathers"]
        self._gold_feathers_shuffle_value = tk.StringVar(self._collectables_frame)
        self._gold_feathers_shuffle_value.set(self._gold_feathers_shuffle_options[0])
        self._gold_feathers_shuffle_dropdown = ttk.Combobox(self._collectables_frame, textvariable=self._gold_feathers_shuffle_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=28)
        self._gold_feathers_shuffle_dropdown['values'] = self._gold_feathers_shuffle_options
        self._gold_feathers_shuffle_dropdown['state'] = 'readonly'
        self._gold_feathers_shuffle_dropdown.grid(row=10, column=1, columnspan=2, padx=5)
        self._gold_feathers_shuffle_group_value = tk.StringVar()
        self._gold_feathers_shuffle_group_value.set("B")
        self._gold_feathers_shuffle_group_entry = tk.Entry(self._collectables_frame, textvariable=self._gold_feathers_shuffle_group_value, width=8)
        self._gold_feathers_shuffle_group_entry.grid(row=10, column=3, padx=5)
        # Abnormalities
        self._collectable_abnormalities_value = tk.IntVar()
        self._collectable_abnormalities_checkbutton = ttk.Checkbutton(self._collectables_frame, text="Include Abnormal Collectables", variable=self._collectable_abnormalities_value)
        self._collectable_abnormalities_checkbutton.grid(row=11, column=0, columnspan=2, padx=10, pady=5, sticky='w')
        # Softlock
        self._collectable_softlock_value = tk.IntVar()
        self._collectable_softlock_checkbutton = ttk.Checkbutton(self._collectables_frame, text="Include Softlock Collectables", variable=self._collectable_softlock_value)
        self._collectable_softlock_checkbutton.grid(row=11, column=2, columnspan=2, padx=10, pady=5, sticky='w')
    
    def _create_cheato_capacities_frame(self):
        self._cheato_capacities_frame = ttk.Frame(self._capacities_frame)
        self._cheato_capacities_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Labels
        self._before_cheato_text = ttk.Label(self._cheato_capacities_frame, text="Before Cheato", anchor="center", justify="center")
        self._before_cheato_text.grid(row=0, column=1, columnspan=2, padx=5, pady=2)
        self._before_cheato_lower_limit_text = ttk.Label(self._cheato_capacities_frame, text="Lower Limit", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._before_cheato_lower_limit_text.grid(row=1, column=1, padx=5)
        self._before_cheato_upper_limit_text = ttk.Label(self._cheato_capacities_frame, text="Upper Limit", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._before_cheato_upper_limit_text.grid(row=1, column=2, padx=5)
        self._after_cheato_text = ttk.Label(self._cheato_capacities_frame, text="After Cheato", anchor="center", justify="center")
        self._after_cheato_text.grid(row=0, column=3, columnspan=2, padx=5, pady=2)
        self._after_cheato_lower_limit_text = ttk.Label(self._cheato_capacities_frame, text="Lower Limit", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._after_cheato_lower_limit_text.grid(row=1, column=3, padx=5)
        self._after_cheato_upper_limit_text = ttk.Label(self._cheato_capacities_frame, text="Upper Limit", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._after_cheato_upper_limit_text.grid(row=1, column=4, padx=5)
        # Blue Eggs
        self._blue_egg_lower_limit_text = ttk.Label(self._cheato_capacities_frame, text="Blue Eggs", anchor="center", justify="center")
        self._blue_egg_lower_limit_text.grid(row=2, column=0, pady=5, sticky='w')
        self._blue_egg_before_lower_limit_value = tk.StringVar()
        self._blue_egg_before_lower_limit_value.set("")
        self._blue_egg_before_lower_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._blue_egg_before_lower_limit_value, width=8)
        self._blue_egg_before_lower_limit_entry.grid(row=2, column=1, padx=5, pady=2)
        self._blue_egg_before_upper_limit_value = tk.StringVar()
        self._blue_egg_before_upper_limit_value.set("")
        self._blue_egg_before_upper_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._blue_egg_before_lower_limit_value, width=8)
        self._blue_egg_before_upper_limit_entry.grid(row=2, column=2, padx=5, pady=2)
        self._blue_egg_after_lower_limit_value = tk.StringVar()
        self._blue_egg_after_lower_limit_value.set("")
        self._blue_egg_after_lower_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._blue_egg_after_lower_limit_value, width=8)
        self._blue_egg_after_lower_limit_entry.grid(row=2, column=3, padx=5, pady=2)
        self._blue_egg_after_upper_limit_value = tk.StringVar()
        self._blue_egg_after_upper_limit_value.set("")
        self._blue_egg_after_upper_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._blue_egg_after_lower_limit_value, width=8)
        self._blue_egg_after_upper_limit_entry.grid(row=2, column=4, padx=5, pady=2)
        # Red Feathers
        self._red_feather_lower_limit_text = ttk.Label(self._cheato_capacities_frame, text="Red Feathers", anchor="center", justify="center")
        self._red_feather_lower_limit_text.grid(row=3, column=0, pady=5, sticky='w')
        self._red_feather_before_lower_limit_value = tk.StringVar()
        self._red_feather_before_lower_limit_value.set("")
        self._red_feather_before_lower_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._red_feather_before_lower_limit_value, width=8)
        self._red_feather_before_lower_limit_entry.grid(row=3, column=1, padx=5, pady=2)
        self._red_feather_before_upper_limit_value = tk.StringVar()
        self._red_feather_before_upper_limit_value.set("")
        self._red_feather_before_upper_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._red_feather_before_lower_limit_value, width=8)
        self._red_feather_before_upper_limit_entry.grid(row=3, column=2, padx=5, pady=2)
        self._red_feather_after_lower_limit_value = tk.StringVar()
        self._red_feather_after_lower_limit_value.set("")
        self._red_feather_after_lower_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._red_feather_after_lower_limit_value, width=8)
        self._red_feather_after_lower_limit_entry.grid(row=3, column=3, padx=5, pady=2)
        self._red_feather_after_upper_limit_value = tk.StringVar()
        self._red_feather_after_upper_limit_value.set("")
        self._red_feather_after_upper_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._red_feather_after_lower_limit_value, width=8)
        self._red_feather_after_upper_limit_entry.grid(row=3, column=4, padx=5, pady=2)
        # Gold Feathers
        self._gold_feather_lower_limit_text = ttk.Label(self._cheato_capacities_frame, text="Gold Feathers", anchor="center", justify="center")
        self._gold_feather_lower_limit_text.grid(row=4, column=0, pady=5, sticky='w')
        self._gold_feather_before_lower_limit_value = tk.StringVar()
        self._gold_feather_before_lower_limit_value.set("")
        self._gold_feather_before_lower_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._gold_feather_before_lower_limit_value, width=8)
        self._gold_feather_before_lower_limit_entry.grid(row=4, column=1, padx=5, pady=2)
        self._gold_feather_before_upper_limit_value = tk.StringVar()
        self._gold_feather_before_upper_limit_value.set("")
        self._gold_feather_before_upper_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._gold_feather_before_lower_limit_value, width=8)
        self._gold_feather_before_upper_limit_entry.grid(row=4, column=2, padx=5, pady=2)
        self._gold_feather_after_lower_limit_value = tk.StringVar()
        self._gold_feather_after_lower_limit_value.set("")
        self._gold_feather_after_lower_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._gold_feather_after_lower_limit_value, width=8)
        self._gold_feather_after_lower_limit_entry.grid(row=4, column=3, padx=5, pady=2)
        self._gold_feather_after_upper_limit_value = tk.StringVar()
        self._gold_feather_after_upper_limit_value.set("")
        self._gold_feather_after_upper_limit_entry = tk.Entry(self._cheato_capacities_frame, textvariable=self._gold_feather_after_lower_limit_value, width=8)
        self._gold_feather_after_upper_limit_entry.grid(row=4, column=4, padx=5, pady=2)

    def _create_additional_capacity_options_frame(self):
        self._capacities_options_frame = ttk.Frame(self._capacities_frame)
        self._capacities_options_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Guarantee Cheato Increases Carrying Capacity
        self._good_boi_cheato_value = tk.IntVar()
        self._good_boi_cheato_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Guarantee Cheato Increases Capacity", variable=self._good_boi_cheato_value)
        self._good_boi_cheato_checkbutton.grid(row=0, column=0, padx=5, pady=3, sticky='w')
        # Convert Abnormalities To Normalities
        self._convert_abnormal_items_value = tk.IntVar()
        self._convert_abnormal_items_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Normalize All Abnormal Eggs & Feathers", variable=self._convert_abnormal_items_value)
        self._convert_abnormal_items_checkbutton.grid(row=0, column=1, padx=5, pady=3, sticky='w')
        # Start With Maximum Blue Eggs
        self._start_with_max_blue_eggs_value = tk.IntVar()
        self._start_with_max_blue_eggs_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Start With Maximum Blue Eggs", variable=self._start_with_max_blue_eggs_value)
        self._start_with_max_blue_eggs_checkbutton.grid(row=1, column=0, padx=5, pady=3, sticky='w')
        # Infinite Blue Eggs
        self._infinite_blue_eggs_value = tk.IntVar()
        self._infinite_blue_eggs_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Infinite Blue Eggs", variable=self._infinite_blue_eggs_value)
        self._infinite_blue_eggs_checkbutton.grid(row=1, column=1, padx=5, pady=3, sticky='w')
        # Start With Maximum Red Feathers
        self._start_with_max_red_feathers_value = tk.IntVar()
        self._start_with_max_red_feathers_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Start With Maximum Red Feathers", variable=self._start_with_max_red_feathers_value)
        self._start_with_max_red_feathers_checkbutton.grid(row=2, column=0, padx=5, pady=3, sticky='w')
        # Infinite Red Feathers
        self._infinite_red_feathers_value = tk.IntVar()
        self._infinite_red_feathers_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Infinite Red Feathers", variable=self._infinite_red_feathers_value)
        self._infinite_red_feathers_checkbutton.grid(row=2, column=1, padx=5, pady=3, sticky='w')
        # Start With Maximum Gold Feathers
        self._start_with_max_gold_feathers_value = tk.IntVar()
        self._start_with_max_gold_feathers_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Start With Maximum Gold Feathers", variable=self._start_with_max_gold_feathers_value)
        self._start_with_max_gold_feathers_checkbutton.grid(row=3, column=0, padx=5, pady=3, sticky='w')
        # Infinite Gold Feathers
        self._infinite_gold_feathers_value = tk.IntVar()
        self._infinite_gold_feathers_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Infinite Gold Feathers", variable=self._infinite_gold_feathers_value)
        self._infinite_gold_feathers_checkbutton.grid(row=3, column=1, padx=5, pady=3, sticky='w')
        # Start With Conga's Orange
        self._congas_orange_value = tk.IntVar()
        self._congas_orange_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Start With Conga's Orange", variable=self._congas_orange_value)
        self._congas_orange_checkbutton.grid(row=4, column=0, padx=5, pady=3, sticky='w')
        # Start With Blubber's Gold
        self._blubbers_gold_value = tk.IntVar()
        self._blubbers_gold_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Start With Blubber's Gold", variable=self._blubbers_gold_value)
        self._blubbers_gold_checkbutton.grid(row=4, column=1, padx=5, pady=3, sticky='w')
        # Start With Boggy's Presents
        self._boggys_presents_value = tk.IntVar()
        self._boggys_presents_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Start With Boggy's Presents", variable=self._boggys_presents_value)
        self._boggys_presents_checkbutton.grid(row=5, column=0, padx=5, pady=3, sticky='w')
        # Start With Nabnut's Acorns
        self._nabnuts_acorns_value = tk.IntVar()
        self._nabnuts_acorns_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Start With Nabnut's Acorns", variable=self._nabnuts_acorns_value)
        self._nabnuts_acorns_checkbutton.grid(row=5, column=1, padx=5, pady=3, sticky='w')
        # Start With Eyrie's Caterpillars
        self._eyries_caterpillars_value = tk.IntVar()
        self._eyries_caterpillars_checkbutton = ttk.Checkbutton(self._capacities_options_frame, text="Start With Eyrie's Caterpillars", variable=self._eyries_caterpillars_value)
        self._eyries_caterpillars_checkbutton.grid(row=6, column=0, padx=5, pady=3, sticky='w')

    def _create_carrying_items_tab(self):
        self._capacities_tab = ttk.Frame(self._progression_tab_control)
        self._progression_tab_control.add(self._capacities_tab, text="Carrying Items")
        self._capacities_frame = ttk.Frame(self._capacities_tab)
        self._capacities_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self._create_cheato_capacities_frame()
        self._create_additional_capacity_options_frame()
    
    def _create_moves_tab(self):
        self._moves_tab = ttk.Frame(self._progression_tab_control)
        self._progression_tab_control.add(self._moves_tab, text="Moves")
        self._moves_frame = ttk.Frame(self._moves_tab)
        self._moves_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Move Locations
        self._move_location_text = ttk.Label(self._moves_frame, text="Move Locations:", anchor="center", justify="center")
        self._move_location_text.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self._move_location_options = ["Default Locations", "Base Game Location Shuffle", "Psuedo Random Within World Locations", "Psuedo Random Within Game Locations"]
        self._move_location_value = tk.StringVar(self._moves_frame)
        self._move_location_value.set(self._move_location_options[0])
        self._move_location_dropdown = ttk.Combobox(self._moves_frame, textvariable=self._move_location_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=25)
        self._move_location_dropdown['values'] = self._move_location_options
        self._move_location_dropdown['state'] = 'readonly'
        self._move_location_dropdown.grid(row=0, column=1, columnspan=2, padx=5)
        # Starting Moves
        self._starting_moves_text = ttk.Label(self._moves_frame, text="Starting Moves:", anchor="center", justify="left")
        self._starting_moves_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky='w')
        starting_move_diclaimer_text = "Guaranteed Starting Move: Camera"
        self._starting_moves_disclaimer_text = ttk.Label(self._moves_frame, text=starting_move_diclaimer_text, anchor="center", justify="left", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._starting_moves_disclaimer_text.grid(row=2, column=0, columnspan=3, padx=5, sticky='w')
        spiral_mountain_diclaimer_text = "Guaranteed Spiral Mountain Moves: High Jump, Feathery Flap, Flap Flip, Claw Swipe, Roll Attack, Rat-A-Tap Rap"
        self._spiral_mountain_diclaimer_text = ttk.Label(self._moves_frame, text=spiral_mountain_diclaimer_text, anchor="center", justify="left", font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._spiral_mountain_diclaimer_text.grid(row=3, column=0, columnspan=3, padx=5, sticky='w')
        # Additional 3 Slots
        self._starting_move_options = ["Random Option", "No Move", "Climb", "Dive", "Beak Barge", "Talon Trot", "Beak Buster", "Egg Firing", "Flight",
                                       "Shock Spring Jump", "Wonderwing", "Beak Bomb", "Stilt Stride", "Turbo Talon Trot", "Open Note Doors"]
        self._starting_move_slot_1_text = ttk.Label(self._moves_frame, text="Starting Move 1:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._starting_move_slot_1_text.grid(row=4, column=0, padx=5, pady=5)
        self._starting_move_slot_1_value = tk.StringVar(self._moves_frame)
        self._starting_move_slot_1_value.set(self._starting_move_options[0])
        self._starting_move_slot_1_dropdown = ttk.Combobox(self._moves_frame, textvariable=self._starting_move_slot_1_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=17)
        self._starting_move_slot_1_dropdown['values'] = self._starting_move_options
        self._starting_move_slot_1_dropdown['state'] = 'readonly'
        self._starting_move_slot_1_dropdown.grid(row=5, column=0, padx=5)
        self._starting_move_slot_2_text = ttk.Label(self._moves_frame, text="Starting Move 2:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._starting_move_slot_2_text.grid(row=4, column=1, padx=5, pady=5)
        self._starting_move_slot_2_value = tk.StringVar(self._moves_frame)
        self._starting_move_slot_2_value.set(self._starting_move_options[0])
        self._starting_move_slot_2_dropdown = ttk.Combobox(self._moves_frame, textvariable=self._starting_move_slot_2_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=17)
        self._starting_move_slot_2_dropdown['values'] = self._starting_move_options
        self._starting_move_slot_2_dropdown['state'] = 'readonly'
        self._starting_move_slot_2_dropdown.grid(row=5, column=1, padx=5)
        self._starting_move_slot_3_text = ttk.Label(self._moves_frame, text="Starting Move 3:", anchor="center", justify="center", font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE))
        self._starting_move_slot_3_text.grid(row=4, column=2, padx=5, pady=5)
        self._starting_move_slot_3_value = tk.StringVar(self._moves_frame)
        self._starting_move_slot_3_value.set(self._starting_move_options[0])
        self._starting_move_slot_3_dropdown = ttk.Combobox(self._moves_frame, textvariable=self._starting_move_slot_3_value, font=(self._FONT_TYPE, self._SMALL_MEDIUM_FONT_SIZE), width=17)
        self._starting_move_slot_3_dropdown['values'] = self._starting_move_options
        self._starting_move_slot_3_dropdown['state'] = 'readonly'
        self._starting_move_slot_3_dropdown.grid(row=5, column=2, padx=5)
        # Misc Options
        self._misc_moves_options_text = ttk.Label(self._moves_frame, text="Misc Options:", anchor="center", justify="left")
        self._misc_moves_options_text.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky='w')
        self._deactivate_jump_pads_value = tk.IntVar()
        self._deactivate_jump_pads_checkbutton = ttk.Checkbutton(self._moves_frame, text="Deactivate Normally Always Active Shock Jump Pads", variable=self._deactivate_jump_pads_value)
        self._deactivate_jump_pads_checkbutton.grid(row=7, column=0, columnspan=3, padx=5, pady=3, sticky='w')
        self._deactivate_flight_pads_value = tk.IntVar()
        self._deactivate_flight_pads_checkbutton = ttk.Checkbutton(self._moves_frame, text="Deactivate Normally Always Active Flight Pads", variable=self._deactivate_flight_pads_value)
        self._deactivate_flight_pads_checkbutton.grid(row=8, column=0, columnspan=3, padx=5, pady=3, sticky='w')

    def _create_sns_cheats_tab(self):
        self._sns_cheats_tab = ttk.Frame(self._cheats_tab_control)
        self._cheats_tab_control.add(self._sns_cheats_tab, text="SNS")
        self._sns_cheats_frame = ttk.Frame(self._sns_cheats_tab)
        self._sns_cheats_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # CHEAT NOW YOU CAN SEE A NICE ICE KEY WHICH YOU CAN HAVE FOR FREE
        self._ice_key_cheat_value = tk.IntVar()
        self._ice_key_cheat_checkbutton = ttk.Checkbutton(self._sns_cheats_frame, text="Ice Key Cheat", variable=self._ice_key_cheat_value)
        self._ice_key_cheat_checkbutton.grid(row=0, column=0, padx=5, pady=3, sticky='w')
        # CHEAT OUT OF THE SEA IT RISES TO REVEAL MORE SECRET PRIZES
        self._pink_egg_cheat_value = tk.IntVar()
        self._pink_egg_cheat_checkbutton = ttk.Checkbutton(self._sns_cheats_frame, text="Pink Egg Cheat", variable=self._pink_egg_cheat_value)
        self._pink_egg_cheat_checkbutton.grid(row=1, column=0, padx=5, pady=3, sticky='w')
        # CHEAT A DESERT DOOR OPENS WIDE ANCIENT SECRETS WAIT INSIDE
        self._blue_egg_cheat_value = tk.IntVar()
        self._blue_egg_cheat_checkbutton = ttk.Checkbutton(self._sns_cheats_frame, text="Blue Egg Cheat", variable=self._blue_egg_cheat_value)
        self._blue_egg_cheat_checkbutton.grid(row=2, column=0, padx=5, pady=3, sticky='w')
        # CHEAT DONT YOU GO AND TELL HER ABOUT THE SECRET IN HER CELLAR
        self._cyan_egg_cheat_value = tk.IntVar()
        self._cyan_egg_cheat_checkbutton = ttk.Checkbutton(self._sns_cheats_frame, text="Cyan Egg Cheat", variable=self._cyan_egg_cheat_value)
        self._cyan_egg_cheat_checkbutton.grid(row=3, column=0, padx=5, pady=3, sticky='w')
        # CHEAT AMIDST THE HAUNTED GLOOM A SECRET IN THE BATHROOM
        self._green_egg_cheat_value = tk.IntVar()
        self._green_egg_cheat_checkbutton = ttk.Checkbutton(self._sns_cheats_frame, text="Green Egg Cheat", variable=self._green_egg_cheat_value)
        self._green_egg_cheat_checkbutton.grid(row=4, column=0, padx=5, pady=3, sticky='w')
        # CHEAT THIS SECRET YOULL BE GRABBIN IN THE CAPTAINS CABIN
        self._red_egg_cheat_value = tk.IntVar()
        self._red_egg_cheat_checkbutton = ttk.Checkbutton(self._sns_cheats_frame, text="Red Egg Cheat", variable=self._red_egg_cheat_value)
        self._red_egg_cheat_checkbutton.grid(row=5, column=0, padx=5, pady=3, sticky='w')
        # CHEAT NOW BANJO WILL BE ABLE TO SEE IT ON NABNUTS TABLE
        self._yellow_egg_cheat_value = tk.IntVar()
        self._yellow_egg_cheat_checkbutton = ttk.Checkbutton(self._sns_cheats_frame, text="Yellow Egg Cheat", variable=self._yellow_egg_cheat_value)
        self._yellow_egg_cheat_checkbutton.grid(row=6, column=0, padx=5, pady=3, sticky='w')
    
    def _create_open_world_cheats_tab(self):
        self._open_world_cheats_tab = ttk.Frame(self._cheats_tab_control)
        self._cheats_tab_control.add(self._open_world_cheats_tab, text="Open World")
        self._open_world_cheats_frame = ttk.Frame(self._open_world_cheats_tab)
        self._open_world_cheats_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # CHEAT THERES NOWHERE DANKER THAN IN WITH CLANKER
        self._open_third_world_cheat_value = tk.IntVar()
        self._open_third_world_cheat_checkbutton = ttk.Checkbutton(self._open_world_cheats_frame, text="Open Third World Cheat", variable=self._open_third_world_cheat_value)
        self._open_third_world_cheat_checkbutton.grid(row=0, column=0, padx=5, pady=3, sticky='w')
        # CHEAT NOW INTO THE SWAMP YOU CAN STOMP
        self._open_fourth_world_cheat_value = tk.IntVar()
        self._open_fourth_world_cheat_checkbutton = ttk.Checkbutton(self._open_world_cheats_frame, text="Open Fourth World Cheat", variable=self._open_fourth_world_cheat_value)
        self._open_fourth_world_cheat_checkbutton.grid(row=1, column=0, padx=5, pady=3, sticky='w')
        # CHEAT THIS COMES IN HANDY TO OPEN SOMEWHERE SANDY
        self._open_fifth_world_cheat_value = tk.IntVar()
        self._open_fifth_world_cheat_checkbutton = ttk.Checkbutton(self._open_world_cheats_frame, text="Open Fifth World Cheat", variable=self._open_fifth_world_cheat_value)
        self._open_fifth_world_cheat_checkbutton.grid(row=2, column=0, padx=5, pady=3, sticky='w')
        # CHEAT NOW YOU CAN GO AND TRUDGE IN THE SNOW
        self._open_sixth_world_cheat_value = tk.IntVar()
        self._open_sixth_world_cheat_checkbutton = ttk.Checkbutton(self._open_world_cheats_frame, text="Open Sixth World Cheat", variable=self._open_sixth_world_cheat_value)
        self._open_sixth_world_cheat_checkbutton.grid(row=3, column=0, padx=5, pady=3, sticky='w')
        # CHEAT THE MANSION OF GHOSTS ARE NOW YOUR HOSTS
        self._open_seventh_world_cheat_value = tk.IntVar()
        self._open_seventh_world_cheat_checkbutton = ttk.Checkbutton(self._open_world_cheats_frame, text="Open Seventh World Cheat", variable=self._open_seventh_world_cheat_value)
        self._open_seventh_world_cheat_checkbutton.grid(row=4, column=0, padx=5, pady=3, sticky='w')
        # CHEAT WHY NOT TAKE A TRIP INSIDE GRUNTYS RUSTY SHIP
        self._open_eigth_world_cheat_value = tk.IntVar()
        self._open_eigth_world_cheat_checkbutton = ttk.Checkbutton(self._open_world_cheats_frame, text="Open Eigth World Cheat", variable=self._open_eigth_world_cheat_value)
        self._open_eigth_world_cheat_checkbutton.grid(row=5, column=0, padx=5, pady=3, sticky='w')
        # CHEAT THIS ONES GOOD AS YOU CAN ENTER THE WOOD
        self._open_ninth_world_cheat_value = tk.IntVar()
        self._open_ninth_world_cheat_checkbutton = ttk.Checkbutton(self._open_world_cheats_frame, text="Open Ninth World Cheat", variable=self._open_ninth_world_cheat_value)
        self._open_ninth_world_cheat_checkbutton.grid(row=6, column=0, padx=5, pady=3, sticky='w')
    
    def _create_open_note_door_cheats_tab(self):
        self._open_note_door_cheats_tab = ttk.Frame(self._cheats_tab_control)
        self._cheats_tab_control.add(self._open_note_door_cheats_tab, text="Open Note Doors")
        self._open_note_door_cheats_frame = ttk.Frame(self._open_note_door_cheats_tab)
        self._open_note_door_cheats_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # CHEAT GO RIGHT ON THROUGH NOTE DOOR TWO
        self._open_second_note_door_cheat_value = tk.IntVar()
        self._open_second_note_door_cheat_checkbutton = ttk.Checkbutton(self._open_note_door_cheats_frame, text="Open Second World Cheat", variable=self._open_second_note_door_cheat_value)
        self._open_second_note_door_cheat_checkbutton.grid(row=0, column=0, padx=5, pady=3, sticky='w')
        # CHEAT NOTE DOOR THREE GET IN FOR FREE
        self._open_third_note_door_cheat_value = tk.IntVar()
        self._open_third_note_door_cheat_checkbutton = ttk.Checkbutton(self._open_note_door_cheats_frame, text="Open Third World Cheat", variable=self._open_third_note_door_cheat_value)
        self._open_third_note_door_cheat_checkbutton.grid(row=1, column=0, padx=5, pady=3, sticky='w')
        # CHEAT TAKE A TOUR THROUGH NOTE DOOR FOUR
        self._open_fourth_note_door_cheat_value = tk.IntVar()
        self._open_fourth_note_door_cheat_checkbutton = ttk.Checkbutton(self._open_note_door_cheats_frame, text="Open Fourth World Cheat", variable=self._open_fourth_note_door_cheat_value)
        self._open_fourth_note_door_cheat_checkbutton.grid(row=2, column=0, padx=5, pady=3, sticky='w')
        # CHEAT USE THIS CHEAT NOTE DOOR FIVE IS BEAT
        self._open_fifth_note_door_cheat_value = tk.IntVar()
        self._open_fifth_note_door_cheat_checkbutton = ttk.Checkbutton(self._open_note_door_cheats_frame, text="Open Fifth World Cheat", variable=self._open_fifth_note_door_cheat_value)
        self._open_fifth_note_door_cheat_checkbutton.grid(row=3, column=0, padx=5, pady=3, sticky='w')
        # CHEAT THIS TRICKS USED TO OPEN NOTE DOOR SIX
        self._open_sixth_note_door_cheat_value = tk.IntVar()
        self._open_sixth_note_door_cheat_checkbutton = ttk.Checkbutton(self._open_note_door_cheats_frame, text="Open Sixth World Cheat", variable=self._open_sixth_note_door_cheat_value)
        self._open_sixth_note_door_cheat_checkbutton.grid(row=4, column=0, padx=5, pady=3, sticky='w')
        # CHEAT THE SEVENTH NOTE DOOR IS NOW NO MORE
        self._open_seventh_note_door_cheat_value = tk.IntVar()
        self._open_seventh_note_door_cheat_checkbutton = ttk.Checkbutton(self._open_note_door_cheats_frame, text="Open Seventh World Cheat", variable=self._open_seventh_note_door_cheat_value)
        self._open_seventh_note_door_cheat_checkbutton.grid(row=5, column=0, padx=5, pady=3, sticky='w')
    
    def _create_lair_progression_cheats_tab(self):
        self._lair_progression_cheats_tab = ttk.Frame(self._cheats_tab_control)
        self._cheats_tab_control.add(self._lair_progression_cheats_tab, text="Lair Progression")
        self._lair_progression_cheats_frame = ttk.Frame(self._lair_progression_cheats_tab)
        self._lair_progression_cheats_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # CHEAT YOULL CEASE TO GRIPE WHEN UP GOES A PIPE
        self._raises_big_pipe_cheat_value = tk.IntVar()
        self._raises_big_pipe_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Raise Big Pipe Near CC Cheat", variable=self._raises_big_pipe_cheat_value)
        self._raises_big_pipe_cheat_checkbutton.grid(row=0, column=0, padx=5, pady=3, sticky='w')
        # CHEAT BOTH PIPES ARE THERE TO CLANKERS LAIR
        self._raises_two_pipes_cheat_value = tk.IntVar()
        self._raises_two_pipes_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Raises Two Pipes To CC Cheat", variable=self._raises_two_pipes_cheat_value)
        self._raises_two_pipes_cheat_checkbutton.grid(row=0, column=1, padx=5, pady=3, sticky='w')
        # CHEAT YOULL BE AMAZED NOW THE SWAMP PICCY GRILLE IS RAISED
        self._raise_bgs_puzzle_grate_cheat_value = tk.IntVar()
        self._raise_bgs_puzzle_grate_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Raise Grate To BGS Puzzle Cheat", variable=self._raise_bgs_puzzle_grate_cheat_value)
        self._raise_bgs_puzzle_grate_cheat_checkbutton.grid(row=1, column=0, padx=5, pady=3, sticky='w')
        # CHEAT UP YOU GO WITHOUT A HITCH UP TO THE WATER LEVEL SWITCH
        self._water_level_1_cheat_value = tk.IntVar()
        self._water_level_1_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Water Level 1 Cheat", variable=self._water_level_1_cheat_value)
        self._water_level_1_cheat_checkbutton.grid(row=1, column=1, padx=5, pady=3, sticky='w')
        # CHEAT THEY CAUSE TROUBLE BUT NOW THEYRE RUBBLE
        self._remove_breakable_walls_cheat_value = tk.IntVar()
        self._remove_breakable_walls_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Remove Breakable Walls Cheat", variable=self._remove_breakable_walls_cheat_value)
        self._remove_breakable_walls_cheat_checkbutton.grid(row=2, column=0, padx=5, pady=3, sticky='w')
        # CHEAT YOU WONT HAVE TO WAIT NOW THERES NO CRYPT GATE
        self._remove_shed_gate_cheat_value = tk.IntVar()
        self._remove_shed_gate_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Remove Shed Gate Cheat", variable=self._remove_shed_gate_cheat_value)
        self._remove_shed_gate_cheat_checkbutton.grid(row=2, column=1, padx=5, pady=3, sticky='w')
        # CHEAT DONT DESPAIR THE TREE JIGGY PODIUM IS NOW THERE
        self._reveal_ccw_jiggy_pad_cheat_value = tk.IntVar()
        self._reveal_ccw_jiggy_pad_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Reveal CCW Jiggy Pad Cheat", variable=self._reveal_ccw_jiggy_pad_cheat_value)
        self._reveal_ccw_jiggy_pad_cheat_checkbutton.grid(row=3, column=0, padx=5, pady=3, sticky='w')
        # CHEAT THE GRILLE GOES BOOM TO THE SHIP PICTURE ROOM
        self._remove_rbb_puzzle_grate_cheat_value = tk.IntVar()
        self._remove_rbb_puzzle_grate_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Remove RBB Puzzle Grate Cheat", variable=self._remove_rbb_puzzle_grate_cheat_value)
        self._remove_rbb_puzzle_grate_cheat_checkbutton.grid(row=3, column=1, padx=5, pady=3, sticky='w')
        # CHEAT SHES AN UGLY BAT SO LETS REMOVE HER GRILLE AND HAT
        self._bgs_witch_switch_cheat_value = tk.IntVar()
        self._bgs_witch_switch_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="BGS Witch Switch Cheat", variable=self._bgs_witch_switch_cheat_value)
        self._bgs_witch_switch_cheat_checkbutton.grid(row=4, column=0, padx=5, pady=3, sticky='w')
        # CHEAT GRUNTY WILL CRY NOW YOUVE SMASHED HER EYE
        self._break_grunty_statue_eye_cheat_value = tk.IntVar()
        self._break_grunty_statue_eye_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Break Grunty Statue Eye Cheat", variable=self._break_grunty_statue_eye_cheat_value)
        self._break_grunty_statue_eye_cheat_checkbutton.grid(row=4, column=1, padx=5, pady=3, sticky='w')
        # CHEAT THIS SHOULD GET RID OF THE CRYPT COFFIN LID
        self._break_shed_lid_cheat_value = tk.IntVar()
        self._break_shed_lid_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Break Shed Coffin Lid Cheat", variable=self._break_shed_lid_cheat_value)
        self._break_shed_lid_cheat_checkbutton.grid(row=5, column=0, padx=5, pady=3, sticky='w')
        # CHEAT ITS YOUR LUCKY DAY AS THE ICEBALL MELTS AWAY
        self._break_ice_ball_near_cheato_cheat_value = tk.IntVar()
        self._break_ice_ball_near_cheato_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Break Ice Ball To Cheato Cheat", variable=self._break_ice_ball_near_cheato_cheat_value)
        self._break_ice_ball_near_cheato_cheat_checkbutton.grid(row=5, column=1, padx=5, pady=3, sticky='w')
        # CHEAT WEBS STOP YOUR PLAY SO TAKE THEM AWAY
        self._remove_spider_webs_cheat_value = tk.IntVar()
        self._remove_spider_webs_cheat_checkbutton = ttk.Checkbutton(self._lair_progression_cheats_frame, text="Remove Yellow Spider Webs Cheat", variable=self._remove_spider_webs_cheat_value)
        self._remove_spider_webs_cheat_checkbutton.grid(row=6, column=0, padx=5, pady=3, sticky='w')
    
    def _create_learn_moves_cheats_tab(self):
        self._learn_moves_cheats_tab = ttk.Frame(self._cheats_tab_control)
        self._cheats_tab_control.add(self._learn_moves_cheats_tab, text="Open Note Doors")
        self._learn_moves_cheats_frame = ttk.Frame(self._learn_moves_cheats_tab)
        self._learn_moves_cheats_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # CHEAT YOULL BE GLAD TO SEE THE SHOCK JUMP PAD
        self._learn_shock_jump_cheat_value = tk.IntVar()
        self._learn_shock_jump_cheat_checkbutton = ttk.Checkbutton(self._learn_moves_cheats_frame, text="Automatically Learn Shock Jump Cheat", variable=self._learn_shock_jump_cheat_value)
        self._learn_shock_jump_cheat_checkbutton.grid(row=0, column=0, padx=5, pady=3, sticky='w')
        # CHEAT YOU WONT BE SAD NOW YOU CAN USE THE FLY PAD
        self._learn_flight_cheat_value = tk.IntVar()
        self._learn_flight_cheat_checkbutton = ttk.Checkbutton(self._learn_moves_cheats_frame, text="Automatically Learn Flight Cheat", variable=self._learn_flight_cheat_value)
        self._learn_flight_cheat_checkbutton.grid(row=1, column=0, padx=5, pady=3, sticky='w')

    def _create_cheats_tab(self):
        self._cheats_tab = ttk.Frame(self._progression_tab_control)
        self._progression_tab_control.add(self._cheats_tab, text="Cheats")
        self._cheats_tab_control = ttk.Notebook(self._cheats_tab, width=self._app_window.winfo_width())
        # Allow Cheats Without Requirements Or Limits
        self._create_sns_cheats_tab()
        self._create_open_world_cheats_tab()
        self._create_open_note_door_cheats_tab()
        self._create_lair_progression_cheats_tab()
        self._create_learn_moves_cheats_tab()
        self._cheats_tab_control.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    #################
    ### WARPS TAB ###
    #################

    def _create_warps_tab(self):
        self._warps_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._warps_tab, text="Warps")
        self._warps_frame = ttk.Frame(self._warps_tab)
        self._warps_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # self._warps_tab_control = ttk.Notebook(self._warps_tab, width=self._app_window.winfo_width())
        # self._warps_tab_control.pack(expand=1, fill="both")
        # General Shuffling Options
        # Within World Warps
        # World Entrances
        # Cauldrons
    
    ##########################
    ### WORLD SPECIFIC TAB ###
    ##########################

    def _create_world_specific_tab(self):
        self._world_specific_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._world_specific_tab, text="World Specific")
        self._world_specific_tab_control = ttk.Notebook(self._world_specific_tab, width=self._app_window.winfo_width())
        self._create_spiral_mountain_tab()
        self._create_gruntildas_lair_tab()
        self._create_mumbos_mountain_tab()
        self._create_treasure_trove_cove_tab()
        self._create_clankers_cavern_tab()
        self._create_bubblegloop_swamp_tab()
        self._create_freezeezy_peak_tab()
        self._create_gobis_valley_tab()
        self._create_mad_monster_mansion_tab()
        self._create_rusty_bucket_bay_tab()
        self._create_click_clock_wood_tab()
        self._create_final_battle_tab()
        self._world_specific_tab_control.pack(expand=1, fill="both")
    
    def _create_spiral_mountain_tab(self):
        self._spiral_mountain_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._spiral_mountain_tab, text="SM")
        self._spiral_mountain_frame = ttk.Frame(self._spiral_mountain_tab)
        self._spiral_mountain_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_gruntildas_lair_tab(self):
        self._gruntildas_lair_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._gruntildas_lair_tab, text="GL")
        self._gruntildas_lair_frame = ttk.Frame(self._gruntildas_lair_tab)
        self._gruntildas_lair_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_mumbos_mountain_tab(self):
        self._mumbos_mountain_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._mumbos_mountain_tab, text="MM")
        self._mumbos_mountain_frame = ttk.Frame(self._mumbos_mountain_tab)
        self._mumbos_mountain_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_treasure_trove_cove_tab(self):
        self._treasure_trove_cove_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._treasure_trove_cove_tab, text="TTC")
        self._treasure_trove_cove_frame = ttk.Frame(self._treasure_trove_cove_tab)
        self._treasure_trove_cove_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_clankers_cavern_tab(self):
        self._clankers_cavern_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._clankers_cavern_tab, text="CC")
        self._clankers_cavern_frame = ttk.Frame(self._clankers_cavern_tab)
        self._clankers_cavern_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_bubblegloop_swamp_tab(self):
        self._bubblegloop_swamp_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._bubblegloop_swamp_tab, text="BGS")
        self._bubblegloop_swamp_frame = ttk.Frame(self._bubblegloop_swamp_tab)
        self._bubblegloop_swamp_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_freezeezy_peak_tab(self):
        self._freezeezy_peak_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._freezeezy_peak_tab, text="FP")
        self._freezeezy_peak_frame = ttk.Frame(self._freezeezy_peak_tab)
        self._freezeezy_peak_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_gobis_valley_tab(self):
        self._gobis_valley_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._gobis_valley_tab, text="GV")
        self._gobis_valley_frame = ttk.Frame(self._gobis_valley_tab)
        self._gobis_valley_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_mad_monster_mansion_tab(self):
        self._mad_monster_mansion_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._mad_monster_mansion_tab, text="MMM")
        self._mad_monster_mansion_frame = ttk.Frame(self._mad_monster_mansion_tab)
        self._mad_monster_mansion_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_rusty_bucket_bay_tab(self):
        self._rusty_bucket_bay_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._rusty_bucket_bay_tab, text="RBB")
        self._rusty_bucket_bay_frame = ttk.Frame(self._rusty_bucket_bay_tab)
        self._rusty_bucket_bay_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_click_clock_wood_tab(self):
        self._click_clock_wood_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._click_clock_wood_tab, text="CCW")
        self._click_clock_wood_frame = ttk.Frame(self._click_clock_wood_tab)
        self._click_clock_wood_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_final_battle_tab(self):
        self._final_battle_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._final_battle_tab, text="Final Battle")
        self._final_battle_frame = ttk.Frame(self._final_battle_tab)
        self._final_battle_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    ###########################
    ### QUALITY OF LIFE TAB ###
    ###########################

    def _create_quality_of_life_tab(self):
        self._quality_of_life_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._quality_of_life_tab, text="Quality Of Life")
        self._quality_of_life_tab_control = ttk.Notebook(self._quality_of_life_tab, width=self._app_window.winfo_width())
        self._create_speedrunner_tab()
        self._create_brentilda_hints_tab()
        self._create_quality_of_life_other_tab()
        self._quality_of_life_tab_control.pack(expand=1, fill="both")
    
    def _create_speedrunner_tab(self):
        self._speedrunner_tab = ttk.Frame(self._quality_of_life_tab_control)
        self._quality_of_life_tab_control.add(self._speedrunner_tab, text="Speedrunner")
        self._speedrunner_frame = ttk.Frame(self._speedrunner_tab)
        self._speedrunner_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Exit To Witch's Lair
        self._exit_to_witchs_lair_value = tk.IntVar()
        self._exit_to_witchs_lair_checkbutton = ttk.Checkbutton(self._speedrunner_frame, text="Enable Exit To Witch's Lair", variable=self._exit_to_witchs_lair_value)
        self._exit_to_witchs_lair_checkbutton.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        # Skippable Cutscenes
        self._skippable_cutscenes_value = tk.IntVar()
        self._skippable_cutscenes_checkbutton = ttk.Checkbutton(self._speedrunner_frame, text="Skippable Cutscenes", variable=self._skippable_cutscenes_value)
        self._skippable_cutscenes_checkbutton.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        # Speedrunner Text
        self._speedrunner_text_value = tk.IntVar()
        self._speedrunner_text_checkbutton = ttk.Checkbutton(self._speedrunner_frame, text="Speedrunner Text", variable=self._speedrunner_text_value)
        self._speedrunner_text_checkbutton.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        # Remove Jiggy Fanfare
        self._remove_jiggy_fanfare_value = tk.IntVar()
        self._remove_jiggy_fanfare_checkbutton = ttk.Checkbutton(self._speedrunner_frame, text="Remove Jiggy Jig Fanfare", variable=self._remove_jiggy_fanfare_value)
        self._remove_jiggy_fanfare_checkbutton.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        # Remove Note Door Fanfare
        self._remove_note_door_fanfare_value = tk.IntVar()
        self._remove_note_door_fanfare_checkbutton = ttk.Checkbutton(self._speedrunner_frame, text="Remove Note Door Fanfare", variable=self._remove_note_door_fanfare_value)
        self._remove_note_door_fanfare_checkbutton.grid(row=4, column=0, padx=5, pady=5, sticky='w')
    
    def _create_brentilda_hints_tab(self):
        self._brentilda_hint_tab = ttk.Frame(self._quality_of_life_tab_control)
        self._quality_of_life_tab_control.add(self._brentilda_hint_tab, text="Brentilda")
        self._brentilda_hint_frame = ttk.Frame(self._brentilda_hint_tab)
        self._brentilda_hint_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Brentilda Locations
        self._brentilda_location_frame = ttk.Frame(self._brentilda_hint_frame)
        self._brentilda_location_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self._brentilda_location_text = ttk.Label(self._brentilda_location_frame, text="Brentilda Locations:", anchor="center", justify="center")
        self._brentilda_location_text.grid(row=0, column=0, padx=5, pady=5)
        self._brentilda_location_options = ["Default Locations", "Next To Corresponding World", "Scattered Around The Lair"]
        self._brentilda_location_value = tk.StringVar(self._brentilda_location_frame)
        self._brentilda_location_value.set(self._brentilda_location_options[0])
        self._brentilda_location_dropdown = ttk.Combobox(self._brentilda_location_frame, textvariable=self._brentilda_location_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=25)
        self._brentilda_location_dropdown['values'] = self._brentilda_location_options
        self._brentilda_location_dropdown['state'] = 'readonly'
        self._brentilda_location_dropdown.grid(row=0, column=1, padx=5)
        # World Teachable Moves
        self._world_teachable_moves_frame = ttk.Frame(self._brentilda_hint_frame)
        self._world_teachable_moves_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self._world_teachable_moves_text = ttk.Label(self._world_teachable_moves_frame, text="Possible Move Hints:")
        self._world_teachable_moves_text.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self._world_move_count_value = tk.IntVar()
        self._world_move_count_checkbutton = ttk.Checkbutton(self._world_teachable_moves_frame, text="Tell Me How Many Moves Are In The World", variable=self._world_move_count_value)
        self._world_move_count_checkbutton.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self._world_move_value = tk.IntVar()
        self._world_move_checkbutton = ttk.Checkbutton(self._world_teachable_moves_frame, text="Tell Me A Move That Is In The World", variable=self._world_move_value)
        self._world_move_checkbutton.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self._world_move_location_value = tk.IntVar()
        self._world_move_location_checkbutton = ttk.Checkbutton(self._world_teachable_moves_frame, text="Tell Me Where In The World I Could Find A Move", variable=self._world_move_location_value)
        self._world_move_location_checkbutton.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        # World Item Count
        self._world_item_count_frame = ttk.Frame(self._brentilda_hint_frame)
        self._world_item_count_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Jiggies
        self._world_jiggy_count_text = ttk.Label(self._world_item_count_frame, text="Jiggy Count Hint:", anchor="center", justify="center")
        self._world_jiggy_count_text.grid(row=0, column=0, padx=5, sticky='w')
        self._world_jiggy_count_options = ["No Jiggy Hint", "Vague Jiggy Count Hint", "Detailed Jiggy Count Hint"]
        self._world_jiggy_count_value = tk.StringVar(self._world_item_count_frame)
        self._world_jiggy_count_value.set(self._world_jiggy_count_options[0])
        self._world_jiggy_count_dropdown = ttk.Combobox(self._world_item_count_frame, textvariable=self._world_jiggy_count_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=25)
        self._world_jiggy_count_dropdown['values'] = self._world_jiggy_count_options
        self._world_jiggy_count_dropdown['state'] = 'readonly'
        self._world_jiggy_count_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        # Honeycombs
        self._world_honeycomb_count_text = ttk.Label(self._world_item_count_frame, text="Empty Honeycomb Count Hint:", anchor="center", justify="center")
        self._world_honeycomb_count_text.grid(row=1, column=0, padx=5, sticky='w')
        self._world_honeycomb_count_options = ["No Honeycomb Hint", "Vague Honeycomb Count Hint", "Detailed Honeycomb Count Hint"]
        self._world_honeycomb_count_value = tk.StringVar(self._world_item_count_frame)
        self._world_honeycomb_count_value.set(self._world_honeycomb_count_options[0])
        self._world_honeycomb_count_dropdown = ttk.Combobox(self._world_item_count_frame, textvariable=self._world_honeycomb_count_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=25)
        self._world_honeycomb_count_dropdown['values'] = self._world_honeycomb_count_options
        self._world_honeycomb_count_dropdown['state'] = 'readonly'
        self._world_honeycomb_count_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        # Tokens
        self._world_token_count_text = ttk.Label(self._world_item_count_frame, text="Mumbo Token Count Hint:", anchor="center", justify="center")
        self._world_token_count_text.grid(row=2, column=0, padx=5, sticky='w')
        self._world_token_count_options = ["No Token Hint", "Vague Token Count Hint", "Detailed Token Count Hint"]
        self._world_token_count_value = tk.StringVar(self._world_item_count_frame)
        self._world_token_count_value.set(self._world_token_count_options[0])
        self._world_token_count_dropdown = ttk.Combobox(self._world_item_count_frame, textvariable=self._world_token_count_value, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE), width=25)
        self._world_token_count_dropdown['values'] = self._world_token_count_options
        self._world_token_count_dropdown['state'] = 'readonly'
        self._world_token_count_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky='w')
    
    def _create_quality_of_life_other_tab(self):
        self._quality_of_life_other_tab = ttk.Frame(self._quality_of_life_tab_control)
        self._quality_of_life_tab_control.add(self._quality_of_life_other_tab, text="QoL Other")
        self._quality_of_life_other_frame = ttk.Frame(self._quality_of_life_other_tab)
        self._quality_of_life_other_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Infinite Lives
        self._infinite_lives_value = tk.IntVar()
        self._infinite_lives_checkbutton = ttk.Checkbutton(self._quality_of_life_other_frame, text="Infinite Lives", variable=self._infinite_lives_value)
        self._infinite_lives_checkbutton.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        # Constant Jiggy Display
        self._constant_jiggy_display_value = tk.IntVar()
        self._constant_jiggy_display_checkbutton = ttk.Checkbutton(self._quality_of_life_other_frame, text="Always Display Jiggy Total", variable=self._constant_jiggy_display_value)
        self._constant_jiggy_display_checkbutton.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        # Constant Note Display
        self._constant_note_display_value = tk.IntVar()
        self._constant_note_display_checkbutton = ttk.Checkbutton(self._quality_of_life_other_frame, text="Always Display Note Total", variable=self._constant_note_display_value)
        self._constant_note_display_checkbutton.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        # Pause Menu Move Tracker
        self._pause_menu_move_tracker_value = tk.IntVar()
        self._pause_menu_move_tracker_checkbutton = ttk.Checkbutton(self._quality_of_life_other_frame, text="Move Tracker In Pause Menu", variable=self._pause_menu_move_tracker_value)
        self._pause_menu_move_tracker_checkbutton.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        # XBOX Note Saving
        self._note_saving_value = tk.IntVar()
        self._note_saving_checkbutton = ttk.Checkbutton(self._quality_of_life_other_frame, text="XBOX Note Saving", variable=self._note_saving_value)
        self._note_saving_checkbutton.grid(row=4, column=0, padx=5, pady=5, sticky='w')
    
    #####################
    ### DEVELOPER TAB ###
    #####################

    def _create_developer_tab(self):
        self._developer_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._developer_tab, text="Developer")
        self._developer_tab_control = ttk.Notebook(self._developer_tab, width=self._app_window.winfo_width())
        self._create_custom_asset_tab()
        self._create_developer_other_tab()
        self._developer_tab_control.pack(expand=1, fill="both")
    
    def _create_custom_asset_table(self):
        self._custom_asset_table = ttk.Treeview(self._custom_asset_frame, selectmode='browse', height=5)
        self._custom_asset_table.grid(row=0, column=0, rowspan=3, columnspan=4, padx=5, pady=5)
        self._custom_asset_table["columns"] = ("1", "2", "3", "4")
        self._custom_asset_table['show']='headings'
        self._custom_asset_table.column("1", width=90, anchor='c')
        self._custom_asset_table.column("2", width=200, anchor='c')
        self._custom_asset_table.column("3", width=90, anchor='c')
        self._custom_asset_table.column("4", width=200, anchor='c')
        self._custom_asset_table.heading("1", text="Pointer Address") # Required
        self._custom_asset_table.heading("2", text="Original Name") # Auto Generated
        self._custom_asset_table.heading("3", text="Action") # Replace/Remove
        self._custom_asset_table.heading("4", text="New File") # Optional
    
    def _update_original_asset_display(self, *args):
        known_pointer_table = {"Test": "Test Level"}
        if(self._asset_pointer_address_value.get() == ""):
            self._original_asset_value.set("")
        elif(self._asset_pointer_address_value.get() in known_pointer_table):
            self._original_asset_value.set(known_pointer_table[self._asset_pointer_address_entry.get()])
        else:
            self._original_asset_value.set("Unknown")

    def _select_new_asset_filename(self):
        print("Selecting New Asset")
        filename = tkinter.filedialog.askopenfilename(initialdir=self._cwd, title="Select The New Asset File", filetype =(("Bin Files","*.bin"),("all files","*.*")) )
        if(not filename):
            return
        self._new_asset_filename_entry.set(filename)
        self._new_asset_filename_display.xview_moveto(1)

    def _entry_boxes(self):
        # POINTER ADDRESS
        self._asset_pointer_address_text = ttk.Label(self._custom_asset_frame, text="Pointer\nAddress", anchor="center", justify="center")
        self._asset_pointer_address_text.grid(row=3, column=0, padx=5, pady=5)
        self._asset_pointer_address_value = tk.StringVar()
        self._asset_pointer_address_value.set("")
        self._asset_pointer_address_entry = tk.Entry(self._custom_asset_frame, textvariable=self._asset_pointer_address_value, width=8)
        self._asset_pointer_address_entry.grid(row=4, column=0, padx=5, pady=5)
        # ORIGINAL NAME
        self._original_asset_text = ttk.Label(self._custom_asset_frame, text="Original File", anchor="center", justify="center")
        self._original_asset_text.grid(row=3, column=1, padx=5)
        self._original_asset_value = tk.StringVar()
        self._original_asset_value.set("")
        self._original_asset_display = tk.Entry(self._custom_asset_frame, textvariable=self._original_asset_value, state='readonly', font=("Arial", 12))
        self._original_asset_display.grid(row=4, column=1, padx=5)
        # ACTION
        self._new_asset_action_text = ttk.Label(self._custom_asset_frame, text="Action", anchor="center", justify="center")
        self._new_asset_action_text.grid(row=3, column=2, padx=5)
        self._new_asset_action_options = ["Replace", "Remove"]
        self._new_asset_action_value = tk.StringVar(self._custom_asset_frame)
        self._new_asset_action_value.set(self._new_asset_action_options[0])
        self._new_asset_action_dropdown = ttk.Combobox(self._custom_asset_frame, textvariable=self._new_asset_action_value, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE), width=8)
        self._new_asset_action_dropdown['values'] = self._new_asset_action_options
        self._new_asset_action_dropdown['state'] = 'readonly'
        self._new_asset_action_dropdown.grid(row=4, column=2, padx=5)
        # NEW FILE
        self._new_asset_filename_text = ttk.Label(self._custom_asset_frame, text="New File", anchor="center", justify="center")
        self._new_asset_filename_text.grid(row=3, column=3, padx=5)
        self._new_asset_filename_entry = tk.StringVar(self._custom_asset_frame)
        self._new_asset_filename_display = tk.Entry(self._custom_asset_frame, textvariable=self._new_asset_filename_entry, state='readonly')
        self._new_asset_filename_display.grid(row=4, column=3, padx=5)
        self._new_asset_filename_button = tk.Button(self._custom_asset_frame, text='Select\nNew File', command=self._select_new_asset_filename, foreground=self._WHITE_COLOR, background=self._BLUE_COLOR, width=10)
        self._new_asset_filename_button.grid(row=4, column=4, padx=5)
        # TRACE(S)
        self._asset_pointer_address_value.trace('w', self._update_original_asset_display)

    def _remove_row(self):
        selected_row = self._custom_asset_table.selection()[0]
        self._custom_asset_table.delete(selected_row)
    
    def _create_remove_row_button(self):
        self._remove_row_button = tk.Button(self._custom_asset_frame, text='Remove Row', command=self._remove_row, foreground=self._WHITE_COLOR, background=self._RED_COLOR, width=10)
        self._remove_row_button.grid(row=0, column=4, padx=5)

    def _default_remove_assets_rows(self, *arg):
        DEFAULT_ASSET_REMOVE_LIST = [
            {"Pointer": "10378", "Original": "Invisible Walls?"},
            {"Pointer": "10548", "Original": "Test Map 1"},
            {"Pointer": "10550", "Original": "Test Map 2"},
        ]
        for item_count, item, in enumerate(DEFAULT_ASSET_REMOVE_LIST):
            self._custom_asset_table.insert(parent="", index='end', iid=item_count, values=(item["Pointer"], item["Original"], "Remove", ""))

    def _add_row(self, *arg):
        table_len = len(self._custom_asset_table.get_children())
        self._custom_asset_table.insert(parent="", index='end', iid=table_len, values=(self._asset_pointer_address_value.get(),
                                                                                       self._original_asset_value.get(),
                                                                                       self._new_asset_action_value.get(),
                                                                                       self._new_asset_filename_entry.get()))
        self._asset_pointer_address_value.set("")
        self._original_asset_value.set("")
        self._new_asset_action_value.set("Replace")
        self._new_asset_filename_entry.set("")
    
    def _create_add_row_button(self):
        self._add_row_button = tk.Button(self._custom_asset_frame, text='Add Row', command=self._add_row, foreground=self._WHITE_COLOR, background=self._RED_COLOR, width=10)
        self._add_row_button.grid(row=2, column=4, padx=5)

    def _create_custom_asset_tab(self):
        self._custom_asset_tab = ttk.Frame(self._developer_tab_control)
        self._developer_tab_control.add(self._custom_asset_tab, text="Custom Assets")
        self._custom_asset_frame = ttk.Frame(self._custom_asset_tab)
        self._custom_asset_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self._create_custom_asset_table()
        self._default_remove_assets_rows()
        self._create_remove_row_button()
        self._create_add_row_button()
        self._entry_boxes()

    def _create_developer_other_tab(self):
        self._developer_other_tab = ttk.Frame(self._developer_tab_control)
        self._developer_tab_control.add(self._developer_other_tab, text="Dev Other")
        self._developer_other_frame = ttk.Frame(self._developer_other_tab)
        self._developer_other_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Starting Area
        # Keep Decompressed Files
        # Disable Cheat Sheets
        # TRACE(S)
    
    ######################
    ### BOTTOM OPTIONS ###
    ######################

    def _load_configuration(self, ask_open_filename=True, file_name="Last_Used_Configuration"):
        if(file_name == "[Select_Preset]"):
            ADDITIONAL_GUI("Bottles_Speaking", "If You Want To Use A Preset, Select From The Dropdown.\nI Recommend The 'Recommended' Preset For A First Playthrough.", "Close")
            print("No Preset Selected To Apply")
            return
        elif(ask_open_filename):
            try:
                config_dir = f"{self._cwd}GUI/Configurations/"
                filename = tkinter.filedialog.askopenfilename(initialdir=config_dir, title="Select A JSON Config File", filetypes =(("Json Files","*.json"),("all files","*.*")))
                with open(filename, "r") as json_file:
                    json_data = json.load(json_file)
            except FileNotFoundError as e:
                print("JSON File Was Not Found Or Operation Was Canceled.\nLeaving The Settings As They Are.")
                print(e)
                return
            except Exception as e:
                print("Error Occurred During Random Configuration.\nLeaving The Settings As They Are.")
                print(e)
                return
        else:
            try:
                filename = f"{self._cwd}GUI/Configurations/{file_name}.json"
                with open(filename, "r") as json_file:
                    json_data = json.load(json_file)
            except FileNotFoundError:
                ADDITIONAL_GUI("Bottles_Speaking", "If you want a video guide, click Brentilda's icon.\nI will apply the recommended first playthrough settings!", "Close")
                print("Last Used Configuration File Not Found. Implementing The Default Settings!")
                return
            except Exception:
                print("Error Occurred During Random Configuration. Leaving Settings As They Are.")
                return
        self._apply_json_data(json_data)

    def _apply_json_data(self, json_data):
        setting_not_found = []
        # GENERAL
        try:
            self._original_rom_file_entry.set(json_data["Original_ROM_File"])
        except KeyError:
            setting_not_found.append("Original_ROM_File")
        try:
            self._randomized_rom_file_entry.set(json_data["New_ROM_File"])
        except KeyError:
            setting_not_found.append("New_ROM_File")
        try:
            self._gui_style_value.set(json_data["GUI_Style"])
        except KeyError:
            setting_not_found.append("GUI_Style")

    def _save_current_configuration(self, button_press=True):
        current_config = {
            "Original_ROM_File": self._original_rom_file_entry.get(),
            "New_ROM_File": self._randomized_rom_file_entry.get(),
            "New_ROM_File": self._randomized_rom_file_entry.get(),
            "GUI_Style": self._gui_style_value.get(),
        }
        if(button_press):
            try:
                config_dir = f"{self._cwd}GUI/Configurations/"
                json_file = tkinter.filedialog.asksaveasfile(initialdir=config_dir, filetypes=(("Json Files","*.json"),("all files","*.*")), defaultextension=json)
                json.dump(current_config, json_file, indent=4)
            except Exception as e:
                print("Save Configuration Button Error")
                print(e)
        else:
            config_file = f"{self._cwd}GUI/Configurations/Last_Used_Configuration.json"
            with open(config_file, "w+") as json_file: 
                json.dump(current_config, json_file, indent=4)

    def _open_file(self, temp):
        # Opens A File
        pass

    def _open_overview_video(self):
        webbrowser.open(VIDEO_OVERVIEW_DICT[self._tab_control.index(self._tab_control.select())])

    def _submit(self):
        self._save_current_configuration(button_press=False)
        progression_app = GUI_PROGRESSION_CLASS(self)
        progression_app._main()

    def _create_bottom_options(self):
        self._config_and_submit = ttk.Frame(self._app_window)
        # self._config_and_submit["borderwidth"] = 0
        # self._config_and_submit["highlightthickness"] = 0
        self._config_and_submit.pack(expand=tk.TRUE, fill=tk.BOTH)
        # # Load
        # self._load_config_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Load_Config.png")
        # self._load_config_button = ttk.Button(self._config_and_submit, text='Load Config', command=self._load_configuration, image=self._load_config_image)
        # self._load_config_button.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # # Save
        # self._save_config_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Save_Config.png")
        # self._save_config_button = ttk.Button(self._config_and_submit, text='Save Config', command=self._save_current_configuration, image=self._save_config_image)
        # self._save_config_button.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Read Me
        self._read_me_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Read_Me.png")
        self._read_me = ttk.Button(self._config_and_submit, text='Open ReadMe', command=(lambda: self._open_file(f"{self._cwd}/ReadMe.txt")), image=self._read_me_image)
        self._read_me.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Overview Video Playlist
        self._overview_video_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Overview_Video.png")
        self._overview_video = ttk.Button(self._config_and_submit, text='Open Overview Video Playlist', command=self._open_overview_video, image=self._overview_video_image)
        self._overview_video.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Submit
        self._submit_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Submit.png")
        self._submit_button = ttk.Button(self._config_and_submit, text='Submit', command=self._submit, image=self._submit_image)
        self._submit_button.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')

    ###############
    ### RUN GUI ###
    ###############

    def _run_gui(self):
        self._gui_style()
        self._create_general_tab()
        self._create_models_tab()
        self._create_sounds_tab()
        self._create_enemies_tab()
        self._create_progression_tab()
        self._create_warps_tab()
        self._create_world_specific_tab()
        self._create_quality_of_life_tab()
        self._create_developer_tab()
        self._tab_control.pack(expand=1, fill="both")
        self._create_bottom_options()
        self._load_configuration(ask_open_filename=False)
        self._app_window.protocol("WM_DELETE_WINDOW", self._app_window.destroy)
        self._app_window.mainloop()

if __name__ == '__main__':
    user_app = GUI_MAIN_CLASS("3.0.0 - October 11th, 2022")
    user_app._run_gui()