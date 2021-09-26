import os
import asyncio
from datetime import datetime
from config import captcha_words
from random import choice
from PIL import Image, ImageDraw, ImageFont
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ICaptcha:

    def __init__(self):
        self.color = (0, 0, 0)
        self.width = 900
        self.height = 400

    async def generate_text(self, img, text):
        fnt = await self.fonts_list()
        draw = ImageDraw.Draw(img)
        # position = [75, 150]
        position = [70, 150]

        for c in text:
            selectedFontIndex = random.randint(0, len(fnt) - 1)
            selectedFont = fnt[selectedFontIndex]

            draw.text((position[0], position[1]), c, font=selectedFont, fill=self.color)

            char_size = draw.textsize(c, font=selectedFont)
            position[0] += char_size[0] * 0.9
            position[1] = 60 + random.randint(-50, 50)

    async def fonts_list(self):
        fnt = []
        font_folder = os.path.join(BASE_DIR, 'fonts/')
        font_path = os.listdir(font_folder)

        for filepath in font_path:
            filename, file_extension = os.path.splitext(filepath)
            if file_extension.lower() == '.otf' or file_extension.lower() == '.ttf':
                font_size = random.randint(110, 150)
                fnt += [ImageFont.truetype(font_folder + filename + file_extension, font_size)]

        return fnt

    async def generateRandomLines(self, img):
        draw = ImageDraw.Draw(img)
        for i in range(random.randint(3, 10)):
            p1 = await self.generateRandomCoordinates()
            p2 = await self.generateRandomCoordinates()
            draw.line([p1, p2], fill=self.color, width=random.randint(1, 2))

    async def generateRandomPoints(self, img):
        draw = ImageDraw.Draw(img)
        for i in range(random.randint(200, 1000)):
            p1 = await self.generateRandomCoordinates()
            p2 = (p1[0] + random.randint(1, 3), p1[1] + random.randint(1, 3))
            draw.rectangle([p1, p2], fill=self.color)

    async def generateRandomCoordinates(self):
        coordinates = (random.randint(0, self.width), random.randint(0, self.height))
        return coordinates

    async def getcaptcha(self):
        current_datetime = str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')
        captcha_list = choice(captcha_words)
        keyword = choice(captcha_list)
        img = Image.new('RGB', (self.width, self.height), color=(255, 255, 255))
        file_img = os.path.join(BASE_DIR, f'captcha_img\\{current_datetime}.jpg')

        await self.generate_text(img, keyword)
        await self.generateRandomLines(img)
        await self.generateRandomPoints(img)

        img.save(file_img, quality=0)

        return keyword, captcha_list, file_img
