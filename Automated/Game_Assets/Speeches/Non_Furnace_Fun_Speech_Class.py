import sys

sys.path.append(".")
from Automated.Game_Assets.Speeches.Speech_Class import SPEECH_CLASS

class NON_FURNACE_FUN_SPEECH_CLASS(SPEECH_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)