####################
### FILE IMPORTS ###
####################

from GUI.GUI_Main import GUI_MAIN_CLASS

#################
### VARIABLES ###
#################

BK_RANDO_VERSION = "3.0.0 - October 27th, 2022"

############
### MAIN ###
############

if __name__ == '__main__':
    user_app = GUI_MAIN_CLASS(BK_RANDO_VERSION)
    user_app._run_gui()