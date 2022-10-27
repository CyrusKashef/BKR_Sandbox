import tkinter as tk
from tkinter import ttk, HORIZONTAL
from threading import Thread
import sys

sys.path.append(".")
from Automated.Automated_Class import AUTOMATED_CLASS

class GUI_PROGRESSION_CLASS():
    def __init__(self, gui_main):
        ### CONSTANTS ###
        self._GENERIC_BACKGROUND_COLOR = "#BFBF00"

        ### VARIABLES ###
        self._gui_main = gui_main
        self._progress_bar_window = tk.Toplevel(gui_main._app_window)
        self._progress_bar_window.winfo_toplevel().title("Banjo-Kazooie Randomizer Progress Bar")
        self._progress_bar_window.config(background=gui_main._GOLD_COLOR)
        self._progress_bar_value = 0
    
    ##############################
    ### CUSTOM TKINTER CLASSES ###
    ##############################

    class App_Variable_Label():
        '''A text box that can altered after creation'''
        def __init__(self, window, label_text, background_color):
            '''Initializes variable label'''
            self.text = tk.StringVar()
            self.text.set(label_text)
            self.label = tk.Label(window, textvariable=self.text, background=background_color, font=("Arial", 12), padx=5, pady=5)

        def set_text(self, new_text):
            '''Changes the text'''
            self.text.set(new_text)

        def pack_label(self):
            '''Displays label'''
            self.label.pack()
    
    class App_progress_bar():
        '''A progress bar'''
        def __init__(self, window, bar_length=390, bar_mode='determinate'):
            '''Initializes progress bar'''
            self._progress_bar = ttk.Progressbar(window, style="bk.Horizontal.TProgressbar", orient=HORIZONTAL, length=bar_length, mode=bar_mode)
            self._progress_bar.config(maximum=100)

        def update_bar(self, percentage):
            '''Updates progress bar percentage'''
            self._progress_bar['value'] = percentage

        def pack_bar(self):
            '''Displays progress bar'''
            self._progress_bar.pack(padx=5, pady=5)
    
    #############
    ### SETUP ###
    #############

    def _setup(self):
        self._automated_obj = AUTOMATED_CLASS(self._gui_main._cwd,
                                              self._gui_main._original_rom_file_entry.get(),
                                              self._gui_main._randomized_rom_file_entry.get() + "Banjo-Kazooie-NEW.z64")

    ##############################
    ### EXTRACT AND DECOMPRESS ###
    ##############################

    def _extract_and_decompress(self):
        print("Extraction & Decompression Start")
        self._automated_obj._extract_and_decompress_asset_category("Object Model Files")
        self._automated_obj._extract_and_decompress_asset_category("Level Model Files")
        self._automated_obj._extract_and_decompress_asset_category("Sprite/Texture Files")
        self._automated_obj._extract_and_decompress_asset_category("Music Files")
        self._automated_obj._extract_and_decompress_all_asm()
        self._automated_obj._clean_up("Compressed")
        print("Extraction & Decompression Complete")
    
    ###########################
    ### COMPRESS AND INSERT ###
    ###########################

    def _compress_and_insert(self):
        print("Compression & Insertion Start")
        skip_pointer_list = []
        for iid in self._gui_main._custom_asset_table.get_children():
            item_values = self._gui_main._custom_asset_table.item(iid)["values"]
            if(item_values[2] == "Remove"):
                skip_pointer_list.append(int(str(item_values[0]), 16))
        self._automated_obj._compress_and_insert_asset_category("Object Model Files", skip_pointer_list=skip_pointer_list)
        self._automated_obj._compress_and_insert_asset_category("Level Model Files", skip_pointer_list=skip_pointer_list)
        self._automated_obj._compress_and_insert_asset_category("Sprite/Texture Files", skip_pointer_list=skip_pointer_list)
        self._automated_obj._compress_and_insert_asset_category("Music Files", skip_pointer_list=skip_pointer_list)
        self._automated_obj._compress_and_insert_all_asm()
        self._automated_obj._clean_up("All")
        print("Compression & Insertion Complete")
    
    ######################
    ### CHECKSUM & CRC ###
    ######################
    
    def _core_checksums(self):
        print("Adjusting Core Checksums Start")
        self._automated_obj._remove_known_anti_tampering()
        self._automated_obj._core_checksums()
        print("Adjusting Core Checksums Complete")
    
    def _adjust_crc(self):
        print("Adjusting CRC Start")
        self._automated_obj._adjust_crc()
        print("Adjusting CRC Complete")

    ###############################
    ### RANDOMIZATION PROCESSES ###
    ###############################

    def _randomization_process(self):
        ### SETTING UP
        self._progress_bar_label.set_text("Setting up...")
        try:
            self._setup()
        except Exception as e:
            print("Setup Error")
            raise e
        self._progress_bar.update_bar(5)

        ### Extract And Decompress
        self._progress_bar_label.set_text("Extract And Decompress...")
        try:
            self._extract_and_decompress()
        except Exception as e:
            print("Extract And Decompress Error")
            raise e
        self._progress_bar.update_bar(20)

        ### Assembly Modifications
        self._progress_bar_label.set_text("Assembly Modifications...")
        try:
            pass
        except Exception as e:
            print("Assembly Modifications Error")
            raise e
        self._progress_bar.update_bar(30)

        ### Music Modifications
        self._progress_bar_label.set_text("Music Modifications...")
        try:
            pass
        except Exception as e:
            print("Music Modifications Error")
            raise e
        self._progress_bar.update_bar(40)

        ### Model Modifications
        self._progress_bar_label.set_text("Model Modifications...")
        try:
            pass
        except Exception as e:
            print("Model Modifications Error")
            raise e
        self._progress_bar.update_bar(50)

        ### Setup Modifications
        self._progress_bar_label.set_text("Setup Modifications...")
        try:
            pass
        except Exception as e:
            print("Setup Modifications Error")
            raise e
        self._progress_bar.update_bar(65)

        ### Core Checksums
        self._progress_bar_label.set_text("Core Checksums...")
        try:
            self._core_checksums()
        except Exception as e:
            print("Core Checksums Error")
            raise e
        self._progress_bar.update_bar(75)

        ### Compress And Insert
        self._progress_bar_label.set_text("Compress And Insert...")
        try:
            self._compress_and_insert()
        except Exception as e:
            print("Compress And Insert Error")
            raise e
        self._progress_bar.update_bar(95)

        ### Adjust CRC
        self._progress_bar_label.set_text("Adjust CRC...")
        try:
            self._adjust_crc()
        except Exception as e:
            print("Adjust CRC Error")
            raise e
        self._progress_bar.update_bar(100)
        self._warning_label.set_text("Oomenacka!")
        self._progress_bar_label.set_text(f"Mumbo Spell Done! Let Player Close Window!")

    ###############################
    ### PROGRESSION WINDOW MAIN ###
    ###############################

    def _update_mumbo_gif(self, ind):
        '''Updates The Gif Frame'''
        frame = self._frames[ind]
        ind += 1
        if ind == self._frame_count:
            ind = 0
        self._mumbo_talking_label.configure(image=frame)
        self._mumbo_talking_label.after(60, self._update_mumbo_gif, ind)

    def _main(self):
        '''Creates the progress bar gui and runs the main functions with threading'''
        ########################
        ### PROGRESS BAR GUI ###
        ########################
        # Label
        self._warning_label = self.App_Variable_Label(window=self._progress_bar_window, label_text="Bear And Bird Cannot Close Window.\nMust Complete ROM Transformation.\nHope This Works...", background_color=self._GENERIC_BACKGROUND_COLOR)
        self._warning_label.pack_label()
        # Mumbo Jumbo Talking
        self._frame_count = 10
        self._frames = [tk.PhotoImage(master=self._progress_bar_window, file=(f"{self._gui_main._cwd}/GUI/Sprites/Mumbo_Jumbo_Speaking.gif"), format = 'gif -index %i' %(i)) for i in range(self._frame_count)]
        self._mumbo_talking_label = tk.Label(self._progress_bar_window, background=self._GENERIC_BACKGROUND_COLOR)
        self._mumbo_talking_label.pack()
        # Variable Label
        self._progress_bar_label = self.App_Variable_Label(window=self._progress_bar_window, label_text="Progress Bar", background_color=self._GENERIC_BACKGROUND_COLOR)
        self._progress_bar_label.pack_label()
        # Progress Bar
        self._progress_bar = self.App_progress_bar(self._progress_bar_window)
        self._progress_bar.pack_bar()
        # Threading
        randomization_process_thread = Thread(target=self._randomization_process)
        randomization_process_thread.start()
        ##########################
        ### GUI WINDOW OPTIONS ###
        ##########################
        ### Close Window ##
        self._progress_bar_window.protocol("WM_DELETE_WINDOW", self._progress_bar_window.destroy)
        ### Update Window ###
        self._progress_bar_window.after(0, self._update_mumbo_gif, 0)
        ### Main Loop ###
        self._progress_bar_window.mainloop()