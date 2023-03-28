import subprocess, sys, os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
try:
    from pygame import mixer
except ModuleNotFoundError:
    # install pixelsort in current venv
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    from pygame import mixer

mixer.init()

def PlaySound(path, volume):
    mixer.music.load(path)
    mixer.music.set_volume(volume)
    mixer.music.play()

class Play_Sound():
    """
    This node provides a simple interface to apply PixelSort blur to the output image.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "images": ("IMAGE",),
                "path": ("STRING", {"default": 'change_me.mp3'}),
                "volume": ("FLOAT", {"default": 1, "min": 0.0, "max": 1.0, "step": 0.01}),
                },
            "optional": {
                },
            }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "do_sound"

    CATEGORY = "VextraNodes"

    def do_sound(self, images, path, volume):
        PlaySound(path, volume)

NODE_CLASS_MAPPINGS = {
    "Play Sound": Play_Sound
}