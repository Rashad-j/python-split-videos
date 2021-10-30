# Import everything needed to edit video clips
from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import textwrap


class VideoSplitter:
    def __init__(self) -> None:
        self.output_video_cover = """your video conver text"""
        self.output_video_length = 60
        self.output_mini_duration = 30
        self.output_video_start = 0
        self.output_video_x = 1080  # HD
        self.output_video_y = 1920  # HD
        self.cover_colors = ["white", "yellow", "blue"]
        self.parts_color = ["white", "yellow", "blue"]
        self.input_video_url = ""
        self.tags = """your hashtages"""

    def generateOutput(self):
        # create a black bg
        black_img = Image.new(
            "RGB",
            (self.output_video_x, self.output_video_y),
            (0, 0, 0),
        )
        # input video
        clip = VideoFileClip("tiktok/input/input.mp4")
        # set the desired start
        # clip = clip.subclip(5, 250)
        # get subclips
        clip_duration = int(clip.duration)
        # min possible videos
        min_videos_num = clip_duration // self.output_video_length
        # the final video
        min_videos_num += (
            1
            if ((clip_duration % self.output_video_length) >= self.output_mini_duration)
            else 0
        )
        counter = 0
        for i in range(clip.start, clip_duration, self.output_video_length):
            counter += 1
            start = i
            end = i + self.output_video_length
            if end <= clip_duration:
                out_clip = clip.subclip(start, end)
            else:
                last_video_lenght = clip_duration - i
                if last_video_lenght >= self.output_mini_duration:
                    out_clip = clip.subclip(start, clip_duration)
                else:
                    break
            # set position
            out_clip = out_clip.set_position(("center", "center"))
            # resize to our minimum requirements width
            out_clip = out_clip.resize(width=self.output_video_x)
            # get the clip size
            clip_x, clip_y = out_clip.size
            # get black image with text
            part_txt = f"Part {counter} of {min_videos_num}"
            tmp_black_img = black_img.copy()
            black_bg = self.getBlackBackground(
                tmp_black_img, clip_y, self.output_video_cover, part_txt
            )
            img_clip = ImageClip(black_bg).set_duration(out_clip.duration)
            # Overlay the text clip on the first video clip
            video = CompositeVideoClip([img_clip, out_clip])
            # Write the result to a file (many options available !)
            # video.write_videofile(f"output/edited{counter}.mp4")
            video.write_videofile(f"motivation/output/edited{counter}.mp4", fps=24)
        black_img.close()
        clip.close()

    def getBlackBackground(self, img, clip_y, cover, part_number):
        txt_x = self.output_video_x
        txt_y = (self.output_video_y / 2) - (clip_y / 2)
        txt_y_part = (self.output_video_y / 2) + (clip_y / 2)
        # draw emoji line
        black_img = self.__drawCoverText(img, txt_x, txt_y, cover)
        black_img = self.__drawPartText(black_img, txt_x, txt_y_part, part_number)
        a = np.asarray(black_img)
        return a

    def __drawEmojiLine(self, im, emoji, location, font_size):
        font = "motivation/fonts/emoji/seguiemj.ttf"
        font = ImageFont.truetype(
            font, size=font_size, layout_engine=ImageFont.LAYOUT_RAQM
        )
        draw = ImageDraw.Draw(im)
        draw.text(location, emoji, embedded_color=True, font=font)
        return im

    def __drawCoverText(self, im, x, y, cover, color="white"):
        draw = ImageDraw.Draw(im)
        # quote draw
        font = ImageFont.truetype(
            "motivation/fonts/Patua_One/PatuaOne-Regular.ttf",
            50,
        )
        cover = "\n".join(textwrap.wrap(cover, width=45))
        w, h = draw.textsize(cover, font=font)
        quote_offset = ((x - w) // 2, (y - h) - 50)
        draw.multiline_text(
            quote_offset, cover, font=font, fill="yellow", align="center"
        )
        return im

    def __drawPartText(self, im, x, y, part_txt):
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("motivation/fonts/Lato/Lato-Bold.ttf", 30)
        w_part, h_part = draw.textsize(part_txt, font=font)
        part_offset = ((x - w_part) // 2, (y + h_part) + 60)
        draw.text(part_offset, part_txt, font=font, fill="white")
        im.save("motivation/output/black-bg.png") # save for reference
        return im

    def cropVideo(self):
        pass

    def addCredits(self):
        pass