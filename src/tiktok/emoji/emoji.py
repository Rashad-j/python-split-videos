import os
import subprocess
import PIL.Image
from PIL import Image, ImageDraw, ImageFont

class Emoji:
    def __init__(self) -> None:
        pass
    def generateViaMagick(self, emoji, size, color = "white", output_file = "emoji/emoji.png"):
        """
        size is of format 50x50
        raise error or return 0 upon succcess
        """
        resutl = subprocess.run([
            os.path.join(os.environ['MAGICK_HOME'],  'magick.exe'),
            'convert', '-font', 'Symbola', '-size', f'{size}',
            '-gravity', 'center', '-fill', f'{color}', '-background', 'rgba(0,0,0,0)', f'label:{emoji}', output_file])
        return resutl.returncode

    def show(self, output_file):
        image = PIL.Image.open(output_file)
        image.show()

    def readAsImage(self, file = "emoji/emoji.png"):
        return PIL.Image.open(file)

    def generateViaSymbola(self):
        back_ground_color = (255, 255, 255)
        font_color = (0, 0, 0)

        normal_text = "My input text"
        # normal_font = ImageFont.truetype("PatuaOne-Regular.ttf", 36)
        unicode_text = u"👇"
        unicode_font = ImageFont.truetype("fonts/Symbola.ttf", 36)
        im = Image.new("RGB", (400, 400), back_ground_color)
        draw = ImageDraw.Draw(im)
        draw.text((80, 80), "other " + unicode_text, font=unicode_font, fill=font_color)
        im.show()

    def generateViaNoto(self, im, emoji, location, font_size):
        font = "fonts/seguiemj.ttf"
        fnt = ImageFont.truetype(font, size = font_size, layout_engine=ImageFont.LAYOUT_BASIC)
        draw = ImageDraw.Draw(im)
        draw.text(location, emoji, embedded_color=True, font=fnt )
        return im

# emoji = Emoji()
# # emoji.generate('👇👇👇👇👇👇👇👇', "400x100", "yellow")
# # emoji.generateViaSymbola()
# im = Image.new("RGBA", (900, 900), (100, 100, 100, 100))
# emoji.generateViaNoto(im, "😎", (0, 32), 150)