import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import random
import subprocess

# 定义水印文本和字体
text1 = "xxxxxx"  # 上方水印
text2 = "xxxxxx"  # 下方水印
font_path = "font/Arial Unicode.ttf"  # 请替换为你的字体文件路径
font_size = 40  # 文字大小
font_color = (255, 255, 255)  # 白色

# 输入和输出文件夹路径
input_folder = "1/"  # 输入文件夹
output_folder = "2/"  # 输出文件夹

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有视频文件
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4") or filename.endswith(".avi"):

        input_video_path = os.path.join(input_folder, filename)
        output_video_path = os.path.join(output_folder, filename)

        # 打开视频文件
        cap = cv2.VideoCapture(input_video_path)

        # 获取视频帧率和尺寸
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 创建视频写入对象
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter("temp.mp4", fourcc, fps, (width, height))

        # 创建Pillow的ImageFont对象
        font = ImageFont.truetype(font_path, font_size)

        # 计算水印位置
        pil_image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(pil_image)
        text_bbox1 = draw.textbbox((0, 0),text1, font=font)
        text_width1 = text_bbox1[2] - text_bbox1[0]
        text_height1 = text_bbox1[3] - text_bbox1[1]
        text_bbox2 = draw.textbbox((0, 0), text2, font=font)
        text_width2 = text_bbox2[2] - text_bbox2[0]
        text_height2 = text_bbox2[3] - text_bbox2[1]
        start_x1 = (width - text_width1) // 2
        start_y1 = 0
        start_x2 = (width - text_width2) // 2
        start_y2 = height - text_height2

        # 设置步长
        step_x1 = random.randint(0, 0)  # 调整步长范围，使水印移动速度更慢
        step_y1 = random.randint(3, 3)  # 调整步长范围，使水印移动速度更慢
        step_x2 = random.randint(0, 0)  # 调整步长范围，使水印移动速度更慢
        step_y2 = random.randint(-3, -3)  # 调整步长范围，使水印移动速度更慢

        # 在每一帧上添加水印并进行移动
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # 创建Pillow的Image对象
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(pil_image)

            # 添加水印
            draw.text((start_x1, start_y1), text1, font=font, fill=font_color)
            draw.text((start_x2, start_y2), text2, font=font, fill=font_color)

            # 更新水印位置
            start_x1 += step_x1
            start_y1 += step_y1
            start_x2 += step_x2
            start_y2 += step_y2

            # 检查水印是否超出边界
            if start_x1 <= 0 or start_x1 + text_width1 >= width:
                step_x1 *= -1
            if start_y1 <= 0 or start_y1 + text_height1 >= height:
                step_y1 *= -1
            if start_x2 <= 0 or start_x2 + text_width2 >= width:
                step_x2 *= -1
            if start_y2 <= 0 or start_y2 + text_height2 >= height:
                step_y2 *= -1

            # 将带有水印的帧写入视频
            frame_with_watermark = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
            out.write(frame_with_watermark)

        print(f"处理完成视频：{filename}")
        # 释放资源
        cap.release()
        out.release()
        # 将原视频音频合并到新的视频
        # 如果不需要音频，就注释掉下面的
        ffmpeg_command = (
                    f"ffmpeg -y -loglevel error -i temp.mp4 -i {input_video_path} "
                    f"-map 0:v -map 1:a -c:v libx264 -crf 20  -c:a copy {output_video_path}"
                )
        subprocess.run(ffmpeg_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove("temp.mp4")
print("全部视频处理完成！")
