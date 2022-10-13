import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
from os import getcwd

from Models_Dict import MODELS_DICT

class GUI_MAIN_CLASS():
    def __init__(self, bk_rando_version):
        ### CONSTANTS ###
        self._GENERIC_BACKGROUND_COLOR = "#BFBF00"
        self._WHITE_COLOR = "#FFFFFF"
        self._BLACK_COLOR = "#000000"
        self._BLUE_COLOR = "#0040AA"
        self._RED_COLOR = "#990000"
        self._GOLD_COLOR = "#BFBF00"
        self._FONT_TYPE = "LITHOGRAPH-BOLD"
        self._LARGE_FONT_SIZE = 22
        self._MEDIUM_FONT_SIZE = 16
        self._SMALL_FONT_SIZE = 10

        ### VARIABLES ###
        self._bk_rando_version = bk_rando_version
        self._app_window = tk.Tk()
        self._app_window.winfo_toplevel().title(f"Banjo-Kazooie Randomizer v{self._bk_rando_version}")
        self._cwd = getcwd()
    
    #################
    ### GUI STYLE ###
    #################

    def _gui_style(self):
        self._tab_control = ttk.Notebook(self._app_window)
        style = ttk.Style()
        style.theme_create(
            "Tabs_Font",
            parent="alt",
            settings={
                "TNotebook": {
                    "configure": {
                        "tabmargins": [2, 5, 2, 0],
                        "background": self._GENERIC_BACKGROUND_COLOR,
                        },
                    },
                "TNotebook.Tab": {
                    "configure": {
                        "padding": [5, 5],
                        "foreground": self._WHITE_COLOR,
                        "background": self._RED_COLOR,
                        "anchor": tk.CENTER,
                        "font": ("Arial bold", 10),
                        },
                    "map": {
                        "foreground": [("selected", self._WHITE_COLOR)],
                        "background": [("selected", self._BLUE_COLOR)],
                        "expand": [("selected", [1, 1, 1, 0])],
                        }
                    },
                "Horizontal.TProgressbar": {
                    "configure": {
                        "troughcolor": self._RED_COLOR,
                        "background": self._BLUE_COLOR,
                        "anchor": tk.CENTER,
                        "padding": [10, 10],
                        "width": 20,
                        },
                    },
                }
        )
        style.theme_use("Tabs_Font")
    
    ###################
    ### GENERAL TAB ###
    ###################

    def _select_rom_file(self):
        pass

    def _select_randomized_rom_destination(self):
        pass

    def _generate_randomizer_settings_code(self):
        pass

    def _apply_randomizer_settings_code(self):
        pass

    def _create_general_tab(self):
        self._general_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._general_tab, text="General")
        self._general_frame = tk.LabelFrame(self._general_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR)
        self._general_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self._create_select_rom_frame()
        self._create_seed_frame()
        self._create_settings_code_frame()
    
    def _create_select_rom_frame(self):
        self._rom_frame = tk.LabelFrame(self._general_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._rom_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # DISCLAIMER
        self._rom_file_disclaimer_label = tk.Label(self._rom_frame, text="ROMs must be v1.0 NTSC of Banjo-Kazooie, ending in .z64", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._rom_file_disclaimer_label.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky='w')
        # FOLDER BUTTON
        self._folder_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Open_File.png")
        self._select_rom_button = tk.Button(self._rom_frame, text='Select Original ROM File', image=self._folder_image, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, command=self._select_rom_file)
        self._select_rom_button.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        # ORIGINAL ROM TEXT
        self._original_rom_file_label = tk.Label(self._rom_frame, text="Original ROM:", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._original_rom_file_label.grid(row=1, column=2, padx=5, pady=5, sticky='w')
        # ORIGINAL ROM ENTRY
        self._original_rom_file_entry = tk.StringVar(self._rom_frame)
        self._original_rom_file_display = tk.Entry(self._rom_frame, textvariable=self._original_rom_file_entry, state='readonly', width=35, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._original_rom_file_display.grid(row=1, column=3, columnspan=2, padx=10, pady=5)
        # FOLDER BUTTON
        self._select_rando_rom_button = tk.Button(self._rom_frame, text='Select Randomized ROM Destination', image=self._folder_image, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, command=self._select_randomized_rom_destination)
        self._select_rando_rom_button.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        # RANDOMIZED ROM TEXT
        self._randomized_rom_file_label = tk.Label(self._rom_frame, text="New ROM Dest:", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._randomized_rom_file_label.grid(row=2, column=2, padx=5, pady=5, sticky='w')
        # RANDOMIZED ROM ENTRY
        self._randomized_rom_file_entry = tk.StringVar(self._rom_frame)
        self._randomized_rom_file_display = tk.Entry(self._rom_frame, textvariable=self._randomized_rom_file_entry, state='readonly', width=35, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._randomized_rom_file_display.grid(row=2, column=3, columnspan=2, padx=10, pady=5)
    
    def _create_seed_frame(self):
        self._seed_frame = tk.LabelFrame(self._general_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._seed_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # RANDOM SEED BUTTON
        self._seed_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Seed.png")
        self._random_seed_button = tk.Button(self._seed_frame, text='Random Seed Button', image=self._seed_image, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, command=self._select_rom_file)
        self._random_seed_button.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        # SEED TEXT
        self._seed_label = tk.Label(self._seed_frame, text="Seed:", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._seed_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        # SEED VALUE
        self._seed_value = tk.StringVar(self._seed_frame)
        self._seed_entry = tk.Entry(self._seed_frame, textvariable=self._seed_value, width=43, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._seed_entry.grid(row=0, column=2, padx=10, pady=5)
    
    def _create_settings_code_frame(self):
        self._settings_code_frame = tk.LabelFrame(self._general_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._settings_code_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # GENERATE SETTINGS CODE BUTTON
        self._generate_setting_code_button = tk.Button(self._settings_code_frame, text='Generate\nSettings\nCode', command=self._generate_randomizer_settings_code, foreground=self._WHITE_COLOR, background=self._BLUE_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._generate_setting_code_button.grid(row=0, column=0, padx=5, pady=5)
        # APPLY SETTINGS CODE BUTTON
        self._apply_setting_code_button = tk.Button(self._settings_code_frame, text='Apply\nSettings\nCode', command=self._apply_randomizer_settings_code, foreground=self._WHITE_COLOR, background=self._RED_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._apply_setting_code_button.grid(row=0, column=1, padx=5, pady=5)
        # SETTINGS CODE TEXT
        self._settings_code_label = tk.Label(self._settings_code_frame, text="Settings Code:", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, anchor="w", justify="left", font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._settings_code_label.grid(row=0, column=2, padx=5, pady=5, sticky='w')
        # SETTINGS CODE ENTRY
        self._settings_code_value = tk.StringVar(self._settings_code_frame)
        self._settings_code_entry = tk.Entry(self._settings_code_frame, textvariable=self._settings_code_value, width=30, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._settings_code_entry.grid(row=0, column=3, padx=5, pady=5)
    
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
        self._player_model_frame = tk.LabelFrame(self._player_model_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._player_model_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # MODEL SELECTION
        self._model_selection_options = ["Banjo-Kazooie", "Other Model"]
        self._model_selection_value = tk.StringVar(self._player_model_frame)
        self._model_selection_value.set(self._model_selection_options[0])
        self._model_selection_dropdown = ttk.Combobox(self._player_model_frame, textvariable=self._model_selection_value, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._model_selection_dropdown['values'] = self._model_selection_options
        self._model_selection_dropdown['state'] = 'readonly'
        self._model_selection_dropdown.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self._create_bk_color_selection_frame()
        self._create_other_model_selection_frame()
        # TRACE(S)
        self._model_selection_value.trace('w', self._model_select)
    
    def _create_bk_color_selection_frame(self):
        self._bk_model_preset_options = ["Default", "Mario & Luigi"]
        self._bk_model_preset_value = tk.StringVar(self._player_model_frame)
        self._bk_model_preset_value.set(self._bk_model_preset_options[0])
        self._bk_model_dropdown = ttk.Combobox(self._player_model_frame, textvariable=self._bk_model_preset_value, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE), width=30)
        self._bk_model_dropdown['values'] = self._bk_model_preset_options
        self._bk_model_dropdown['state'] = 'readonly'
        self._bk_model_dropdown.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self._bk_color_frame = tk.LabelFrame(self._player_model_frame, text="BK Model Colors", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        # Banjo Fur
        self._banjo_fur_text = tk.Label(self._bk_color_frame, text="Banjo's Fur", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_fur_text.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self._banjo_fur_value = tk.StringVar(self._bk_color_frame)
        self._banjo_fur_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_fur_value, width=9)
        self._banjo_fur_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        # Banjo Skin
        self._banjo_skin_text = tk.Label(self._bk_color_frame, text="Banjo's Skin", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_skin_text.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self._banjo_skin_value = tk.StringVar(self._bk_color_frame)
        self._banjo_skin_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_skin_value, width=9)
        self._banjo_skin_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        # Banjo Eyes
        self._banjo_eyes_text = tk.Label(self._bk_color_frame, text="Banjo's Eye Color", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_eyes_text.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self._banjo_eyes_value = tk.StringVar(self._bk_color_frame)
        self._banjo_eyes_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_eyes_value, width=9)
        self._banjo_eyes_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        # Banjo Eyelids
        self._banjo_eyelids_text = tk.Label(self._bk_color_frame, text="Banjo's Eyelids", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_eyelids_text.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self._banjo_eyelids_value = tk.StringVar(self._bk_color_frame)
        self._banjo_eyelids_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_eyelids_value, width=9)
        self._banjo_eyelids_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        # Banjo Shorts
        self._banjo_shorts_text = tk.Label(self._bk_color_frame, text="Banjo's Shorts", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_shorts_text.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self._banjo_shorts_value = tk.StringVar(self._bk_color_frame)
        self._banjo_shorts_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_shorts_value, width=9)
        self._banjo_shorts_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        # Banjo Nose
        self._banjo_nose_text = tk.Label(self._bk_color_frame, text="Banjo's Nose", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._banjo_nose_text.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self._banjo_nose_value = tk.StringVar(self._bk_color_frame)
        self._banjo_nose_entry = tk.Entry(self._bk_color_frame, textvariable=self._banjo_nose_value, width=9)
        self._banjo_nose_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        # Kazooie Primary
        self._kazooie_primary_text = tk.Label(self._bk_color_frame, text="Kazooie's Feathers Primary", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._kazooie_primary_text.grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self._kazooie_primary_value = tk.StringVar(self._bk_color_frame)
        self._kazooie_primary_entry = tk.Entry(self._bk_color_frame, textvariable=self._kazooie_primary_value, width=9)
        self._kazooie_primary_entry.grid(row=0, column=3, padx=5, pady=5, sticky='w')
        # Kazooie Secondary
        self._kazooie_secondary_text = tk.Label(self._bk_color_frame, text="Kazooie's Feathers Secondary", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._kazooie_secondary_text.grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self._kazooie_secondary_value = tk.StringVar(self._bk_color_frame)
        self._kazooie_secondary_entry = tk.Entry(self._bk_color_frame, textvariable=self._kazooie_secondary_value, width=9)
        self._kazooie_secondary_entry.grid(row=1, column=3, padx=5, pady=5, sticky='w')
        # Kazooie Tuff
        self._kazooie_tuff_text = tk.Label(self._bk_color_frame, text="Kazooie's Feather Tuff", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._kazooie_tuff_text.grid(row=2, column=2, padx=5, pady=5, sticky='w')
        self._kazooie_tuff_value = tk.StringVar(self._bk_color_frame)
        self._kazooie_tuff_entry = tk.Entry(self._bk_color_frame, textvariable=self._kazooie_tuff_value, width=9)
        self._kazooie_tuff_entry.grid(row=2, column=3, padx=5, pady=5, sticky='w')
        # Kazooie Eyes
        self._kazooie_eyes_text = tk.Label(self._bk_color_frame, text="Kazooie's Eye Color", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._kazooie_eyes_text.grid(row=3, column=2, padx=5, pady=5, sticky='w')
        self._kazooie_eyes_value = tk.StringVar(self._bk_color_frame)
        self._kazooie_eyes_entry = tk.Entry(self._bk_color_frame, textvariable=self._kazooie_eyes_value, width=9)
        self._kazooie_eyes_entry.grid(row=3, column=3, padx=5, pady=5, sticky='w')
        # Kazooie Beak/Legs
        self._kazooie_beak_legs_text = tk.Label(self._bk_color_frame, text="Kazooie's Beak & Legs", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._kazooie_beak_legs_text.grid(row=4, column=2, padx=5, pady=5, sticky='w')
        self._kazooie_beak_legs_value = tk.StringVar(self._bk_color_frame)
        self._kazooie_beak_legs_entry = tk.Entry(self._bk_color_frame, textvariable=self._kazooie_beak_legs_value, width=9)
        self._kazooie_beak_legs_entry.grid(row=4, column=3, padx=5, pady=5, sticky='w')
        # Shark Tooth
        self._shark_tooth_text = tk.Label(self._bk_color_frame, text="Shark Tooth", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._shark_tooth_text.grid(row=0, column=4, padx=5, pady=5, sticky='w')
        self._shark_tooth_value = tk.StringVar(self._bk_color_frame)
        self._shark_tooth_entry = tk.Entry(self._bk_color_frame, textvariable=self._shark_tooth_value, width=9)
        self._shark_tooth_entry.grid(row=0, column=5, padx=5, pady=5, sticky='w')
        # Mouths
        self._mouths_text = tk.Label(self._bk_color_frame, text="BK's Mouths", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._mouths_text.grid(row=1, column=4, padx=5, pady=5, sticky='w')
        self._mouths_value = tk.StringVar(self._bk_color_frame)
        self._mouths_entry = tk.Entry(self._bk_color_frame, textvariable=self._mouths_value, width=9)
        self._mouths_entry.grid(row=1, column=5, padx=5, pady=5, sticky='w')
        # Backpack
        self._backpack_text = tk.Label(self._bk_color_frame, text="Backpack", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._backpack_text.grid(row=2, column=4, padx=5, pady=5, sticky='w')
        self._backpack_value = tk.StringVar(self._bk_color_frame)
        self._backpack_entry = tk.Entry(self._bk_color_frame, textvariable=self._backpack_value, width=9)
        self._backpack_entry.grid(row=2, column=5, padx=5, pady=5, sticky='w')
        # Turbo Talon Trainers
        self._turbo_talon_trainers_text = tk.Label(self._bk_color_frame, text="Turbo Talon Trainers", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._turbo_talon_trainers_text.grid(row=3, column=4, padx=5, pady=5, sticky='w')
        self._turbo_talon_trainers_value = tk.StringVar(self._bk_color_frame)
        self._turbo_talon_trainers_entry = tk.Entry(self._bk_color_frame, textvariable=self._turbo_talon_trainers_value, width=9)
        self._turbo_talon_trainers_entry.grid(row=3, column=5, padx=5, pady=5, sticky='w')
        # Wading Boots
        self._wading_boots_text = tk.Label(self._bk_color_frame, text="Wading Boots", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE))
        self._wading_boots_text.grid(row=4, column=4, padx=5, pady=5, sticky='w')
        self._wading_boots_value = tk.StringVar(self._bk_color_frame)
        self._wading_boots_entry = tk.Entry(self._bk_color_frame, textvariable=self._wading_boots_value, width=9)
        self._wading_boots_entry.grid(row=4, column=5, padx=5, pady=5, sticky='w')
        self._bk_color_frame.grid(row=2, column=0, columnspan=6, padx=5, pady=5, sticky='w')

    def _create_other_model_selection_frame(self):
        self._other_model_frame = tk.LabelFrame(self._player_model_frame, text="Possible Other Models", foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._MEDIUM_FONT_SIZE))
        self._other_model_dict = {}
        for model_count, model_name in enumerate(sorted(MODELS_DICT)):
            self._other_model_dict[model_name] = tk.IntVar()
            temp_checkbutton = tk.Checkbutton(self._other_model_frame, text=model_name, variable=self._other_model_dict[model_name], foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._SMALL_FONT_SIZE), width=13, anchor="w")
            temp_checkbutton.grid(row=(model_count // 5) + 1, column=(model_count % 5), padx=0, pady=0, sticky='w')
    
    def _create_level_model_tab(self):
        self._level_model_tab = ttk.Frame(self._models_tab_control)
        self._models_tab_control.add(self._level_model_tab, text="Levels")
        self._level_model_frame = tk.LabelFrame(self._level_model_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._level_model_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Level Model Colors
        # Colorblind Options
        # Skyboxes
    
    def _create_sprites_tab(self):
        self._sprites_tab = ttk.Frame(self._models_tab_control)
        self._models_tab_control.add(self._sprites_tab, text="Sprites")
        self._sprites_frame = tk.LabelFrame(self._sprites_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._sprites_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Talking Sprites
        # Honeycomb Sprites
        # Pause Font
        # Timer
    
    def _create_model_swaps_tab(self):
        self._model_swaps_tab = ttk.Frame(self._models_tab_control)
        self._models_tab_control.add(self._model_swaps_tab, text="Model Swaps")
        self._model_swaps_frame = tk.LabelFrame(self._model_swaps_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._model_swaps_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    ##################
    ### SOUNDS TAB ###
    ##################

    def _create_sounds_tab(self):
        self._sounds_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._sounds_tab, text="Sounds")
        self._sounds_tab_control = ttk.Notebook(self._sounds_tab, width=self._app_window.winfo_width())
        self._create_sound_effects_tab()
        self._create_short_jingle_tab()
        self._create_long_jingle_tab()
        self._create_mini_game_music_tab()
        self._create_level_music_tab()
        self._sounds_tab_control.pack(expand=1, fill="both")
    
    def _create_sound_effects_tab(self):
        self._sound_effects_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._sound_effects_tab, text="Sound Effects")
        self._sound_effects_frame = tk.LabelFrame(self._sound_effects_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._sound_effects_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_short_jingle_tab(self):
        self._short_jingle_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._short_jingle_tab, text="Short Jingle")
        self._short_jingle_frame = tk.LabelFrame(self._short_jingle_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._short_jingle_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_long_jingle_tab(self):
        self._long_jingle_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._long_jingle_tab, text="Long Jingle")
        self._long_jingle_frame = tk.LabelFrame(self._long_jingle_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._long_jingle_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_mini_game_music_tab(self):
        self._mini_game_music_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._mini_game_music_tab, text="Mini-Game Music")
        self._mini_game_music_frame = tk.LabelFrame(self._mini_game_music_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._mini_game_music_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_level_music_tab(self):
        self._level_music_tab = ttk.Frame(self._sounds_tab_control)
        self._sounds_tab_control.add(self._level_music_tab, text="Level Music")
        self._level_music_frame = tk.LabelFrame(self._level_music_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._level_music_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
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
        self._enemy_selection_frame = tk.LabelFrame(self._enemy_selection_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._enemy_selection_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_enemy_vulnerability_tab(self):
        self._enemy_vulnerability_tab = ttk.Frame(self._enemies_tab_control)
        self._enemies_tab_control.add(self._enemy_vulnerability_tab, text="Vulnerability")
        self._enemy_vulnerability_frame = tk.LabelFrame(self._enemy_vulnerability_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._enemy_vulnerability_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_enemy_other_tab(self):
        self._enemy_other_tab = ttk.Frame(self._enemies_tab_control)
        self._enemies_tab_control.add(self._enemy_other_tab, text="Enemies Other")
        self._enemy_other_frame = tk.LabelFrame(self._enemy_other_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
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
        self._create_capacities_tab()
        self._create_moves_tab()
        self._create_progression_other_tab()
        self._progression_tab_control.pack(expand=1, fill="both")
    
    def _create_requirements_tab(self):
        self._requirements_tab = ttk.Frame(self._progression_tab_control)
        self._progression_tab_control.add(self._requirements_tab, text="Requirements")
        self._requirements_frame = tk.LabelFrame(self._requirements_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._requirements_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Jigsaw Puzzles
        # Note Doors
        # Win Condition
    
    def _create_collectables_tab(self):
        self._collectables_tab = ttk.Frame(self._progression_tab_control)
        self._progression_tab_control.add(self._collectables_tab, text="Collectables")
        self._collectables_frame = tk.LabelFrame(self._collectables_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._collectables_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Jiggies
        # Tokens
        # Honeycombs
        # Jinjos
        # Extra Lives
        # Notes
        # Blue Eggs
        # Red Feathers
        # Gold Feathers
    
    def _create_capacities_tab(self):
        self._capacities_tab = ttk.Frame(self._progression_tab_control)
        self._progression_tab_control.add(self._capacities_tab, text="Capacities")
        self._capacities_frame = tk.LabelFrame(self._capacities_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._capacities_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_moves_tab(self):
        self._moves_tab = ttk.Frame(self._progression_tab_control)
        self._progression_tab_control.add(self._moves_tab, text="Moves")
        self._moves_frame = tk.LabelFrame(self._moves_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._moves_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_progression_other_tab(self):
        self._progression_other_tab = ttk.Frame(self._progression_tab_control)
        self._progression_tab_control.add(self._progression_other_tab, text="Progress Other")
        self._progression_other_frame = tk.LabelFrame(self._progression_other_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._progression_other_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    #################
    ### WARPS TAB ###
    #################

    def _create_warps_tab(self):
        self._warps_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._warps_tab, text="Warps")
        self._warps_frame = tk.LabelFrame(self._warps_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
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
        self._spiral_mountain_frame = tk.LabelFrame(self._spiral_mountain_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._spiral_mountain_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_gruntildas_lair_tab(self):
        self._gruntildas_lair_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._gruntildas_lair_tab, text="GL")
        self._gruntildas_lair_frame = tk.LabelFrame(self._gruntildas_lair_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._gruntildas_lair_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_mumbos_mountain_tab(self):
        self._mumbos_mountain_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._mumbos_mountain_tab, text="MM")
        self._mumbos_mountain_frame = tk.LabelFrame(self._mumbos_mountain_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._mumbos_mountain_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_treasure_trove_cove_tab(self):
        self._treasure_trove_cove_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._treasure_trove_cove_tab, text="TTC")
        self._treasure_trove_cove_frame = tk.LabelFrame(self._treasure_trove_cove_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._treasure_trove_cove_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_clankers_cavern_tab(self):
        self._clankers_cavern_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._clankers_cavern_tab, text="CC")
        self._clankers_cavern_frame = tk.LabelFrame(self._clankers_cavern_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._clankers_cavern_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_bubblegloop_swamp_tab(self):
        self._bubblegloop_swamp_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._bubblegloop_swamp_tab, text="BGS")
        self._bubblegloop_swamp_frame = tk.LabelFrame(self._bubblegloop_swamp_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._bubblegloop_swamp_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_freezeezy_peak_tab(self):
        self._freezeezy_peak_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._freezeezy_peak_tab, text="FP")
        self._freezeezy_peak_frame = tk.LabelFrame(self._freezeezy_peak_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._freezeezy_peak_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_gobis_valley_tab(self):
        self._gobis_valley_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._gobis_valley_tab, text="GV")
        self._gobis_valley_frame = tk.LabelFrame(self._gobis_valley_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._gobis_valley_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_mad_monster_mansion_tab(self):
        self._mad_monster_mansion_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._mad_monster_mansion_tab, text="MMM")
        self._mad_monster_mansion_frame = tk.LabelFrame(self._mad_monster_mansion_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._mad_monster_mansion_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_rusty_bucket_bay_tab(self):
        self._rusty_bucket_bay_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._rusty_bucket_bay_tab, text="RBB")
        self._rusty_bucket_bay_frame = tk.LabelFrame(self._rusty_bucket_bay_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._rusty_bucket_bay_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_click_clock_wood_tab(self):
        self._click_clock_wood_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._click_clock_wood_tab, text="CCW")
        self._click_clock_wood_frame = tk.LabelFrame(self._click_clock_wood_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._click_clock_wood_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_final_battle_tab(self):
        self._final_battle_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._final_battle_tab, text="Final Battle")
        self._final_battle_frame = tk.LabelFrame(self._final_battle_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._final_battle_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    ###########################
    ### QUALITY OF LIFE TAB ###
    ###########################

    def _create_quality_of_life_tab(self):
        self._quality_of_life_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._quality_of_life_tab, text="Quality Of Life")
        self._quality_of_life_tab_control = ttk.Notebook(self._quality_of_life_tab, width=self._app_window.winfo_width())
        self._create_speedrunner_tab()
        self._create_quality_of_life_other_tab()
        self._quality_of_life_tab_control.pack(expand=1, fill="both")
    
    def _create_speedrunner_tab(self):
        self._speedrunner_tab = ttk.Frame(self._quality_of_life_tab_control)
        self._quality_of_life_tab_control.add(self._speedrunner_tab, text="Speedrunner")
        self._speedrunner_frame = tk.LabelFrame(self._speedrunner_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._speedrunner_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_quality_of_life_other_tab(self):
        self._quality_of_life_other_tab = ttk.Frame(self._quality_of_life_tab_control)
        self._quality_of_life_tab_control.add(self._quality_of_life_other_tab, text="QoL Other")
        self._quality_of_life_other_frame = tk.LabelFrame(self._quality_of_life_other_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._quality_of_life_other_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
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
    
    def _create_custom_asset_tab(self):
        self._custom_asset_tab = ttk.Frame(self._developer_tab_control)
        self._developer_tab_control.add(self._custom_asset_tab, text="Custom Assets")
        self._custom_asset_frame = tk.LabelFrame(self._custom_asset_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._custom_asset_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
    
    def _create_developer_other_tab(self):
        self._developer_other_tab = ttk.Frame(self._developer_tab_control)
        self._developer_tab_control.add(self._developer_other_tab, text="Dev Other")
        self._developer_other_frame = tk.LabelFrame(self._developer_other_tab, foreground=self._BLACK_COLOR, background=self._GOLD_COLOR, font=(self._FONT_TYPE, self._LARGE_FONT_SIZE))
        self._developer_other_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Starting Area
    
    ######################
    ### BOTTOM OPTIONS ###
    ######################

    def _load_configuration(self):
        pass

    def _save_current_configuration(self):
        pass

    def _open_file(self, temp):
        pass

    def _open_overview_video(self):
        pass

    def _submit(self):
        pass

    def _create_bottom_options(self):
        self._config_and_submit = tk.LabelFrame(self._app_window)
        self._config_and_submit["borderwidth"] = 0
        self._config_and_submit["highlightthickness"] = 0
        self._config_and_submit.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Load
        self._load_config_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Load_Config.png")
        self._load_config_button = tk.Button(self._config_and_submit, text='Load Config', command=self._load_configuration, image=self._load_config_image, background=self._GENERIC_BACKGROUND_COLOR)
        self._load_config_button.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Save
        self._save_config_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Save_Config.png")
        self._save_config_button = tk.Button(self._config_and_submit, text='Save Config', command=self._save_current_configuration, image=self._save_config_image, background=self._GENERIC_BACKGROUND_COLOR)
        self._save_config_button.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Read Me
        self._read_me_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Read_Me.png")
        self._read_me = tk.Button(self._config_and_submit, text='Open ReadMe', command=(lambda: self._open_file(f"{self._cwd}/ReadMe.txt")), image=self._read_me_image, background=self._GENERIC_BACKGROUND_COLOR)
        self._read_me.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Overview Video Playlist
        self._overview_video_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Overview_Video.png")
        self._overview_video = tk.Button(self._config_and_submit, text='Open Overview Video Playlist', command=self._open_overview_video, image=self._overview_video_image, background=self._GENERIC_BACKGROUND_COLOR)
        self._overview_video.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Submit
        self._submit_image = tk.PhotoImage(file=f"{self._cwd}/GUI/Sprites/Submit.png")
        self._submit_button = tk.Button(self._config_and_submit, text='Submit', command=self._submit, image=self._submit_image, background=self._GENERIC_BACKGROUND_COLOR)
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
        self._app_window.protocol("WM_DELETE_WINDOW", self._app_window.destroy)
        self._app_window.mainloop()

if __name__ == '__main__':
    user_app = GUI_MAIN_CLASS("3.0.0 - October 11th, 2022")
    user_app._run_gui()