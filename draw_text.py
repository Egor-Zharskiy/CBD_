from PIL import Image, ImageDraw, ImageFont
def draw(n):
    im = Image.new('RGB', (500, 500), color=('#ffffff'))
    font = ImageFont.truetype('D:/!projects/color_Bl/TMS.ttf', size=300, )

    draw_text = ImageDraw.Draw(im)
    draw_text.text((70, 100), n, font=font, fill=('#1C0606'), stroke_width=6)

    # im.show()
    im.save(f'imgs/{n}.png')
#продумать как сделать так, чтобы подстраивалось по размерам картинки под любой текст,
# а также добавить вариации цветов
# также про бд подумать
# декодировка и енкодировка есть, осталось все реализовать.
#вариация расположений треугольником и тд