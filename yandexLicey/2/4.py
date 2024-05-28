from PIL import Image, ImageDraw
s = 20
width = s * 20
height = s * 16
image = Image.new('RGB', (width, height), (218, 227, 243))
draw = ImageDraw.Draw(image)
left_wing_color = (204, 0, 204)
right_wing_color = (251, 51, 151)
body_color = (0, 0, 0)
draw.polygon([(height, height // 2), (width // 2, 0), (width // 2, height)], fill=left_wing_color)
draw.polygon([(width // 2, 0), (width, height // 2), (width // 2, height)], fill=right_wing_color)
body_width = 2 * s
body_height = 4 * s
body_left = width // 2 - body_width // 2
body_top = height // 2 - body_height // 2
draw.ellipse((body_left, body_top, body_left + body_width, body_top + body_height), fill=body_color)
reflected_image = image.transpose(Image.FLIP_TOP_BOTTOM)
reflected_image.save("academy.png")
