#  video_dynamic_watermark

**English readme** [README.md](README.md)

# 描述
可以在视频上移动的水印，用于版权维护。

# 背景
我自己开了淘宝店铺，有些视频需要加移动水印，网上找了好多，要不就是收费，要不就是不能批量加，索性自己写一个了。

# 功能
功能很简单，一共有两个水印，一个是从上向下移动的水印，一个是从下向上移动的水印，原理就是逐帧加水印，然后逐渐移动。
大家有更复杂的需求，可以随意更改。

# 用法
我的python版本为：3.10，理论上3.6以上都可以

打开 video_dynamic_watermark.py，将下方的配置替换成你自己需要的就行

```
# 定义水印文本和字体
text1 = "舒克舒克开飞机的舒克"  # 上方水印
text2 = "贝塔贝塔开坦克的贝塔"  # 下方水印
font_path = "font/Arial Unicode.ttf"  # 请替换为你的字体文件路径
font_size = 36  # 文字大小
font_color = (255, 255, 255)  # 白色

# 输入和输出文件夹路径
input_folder = "1/"  # 输入文件夹
output_folder = "2/"  # 输出文件夹
```

然后执行命令

```
pip install -r requirements.txt 
python video_dynamic_watermark.py
```


# 效果

![demo](demo.png)
