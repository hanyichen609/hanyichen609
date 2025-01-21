import os
from gtts import gTTS

# 定义文件夹路径
folder_path = r"C:\Users\dntq\python\pm3"

# 生成语音文本
text = "banana"
tts = gTTS(text=text, lang='en', slow=False)

# 拼接完整路径
file_path = os.path.join(folder_path, "pm3_banana.mp3")

# 保存音频文件
tts.save(file_path)
print(f"音频已保存为 {file_path}")
 