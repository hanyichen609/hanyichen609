import os
from gtts import gTTS

# 定义文件夹路径
folder_path = r"C:\Users\dntq\python\pm3"

# 生成语音文本
text = "Hello! My name is Han Yi chen, and I am 10 years old. I live in China and I am currently in primary school.I am a curious and active person. I enjoy learning new things and exploring the world around me. My favorite subjects are English and science because they allow me to discover interesting facts and express my ideas.In my free time, I like to read books, draw pictures, and play with my friends. I am also learning how to play the piano, and I practice every day. It is a little challenging, but I find it very fun.I have a big dream for the future. I want to become an astronaut so I can travel to space and see the stars up close. I believe that with hard work and determination, I can achieve my goals.Thank you for taking the time to learn about me. I hope we can be friends and share our stories with each other!"



tts = gTTS(text=text, lang='en', slow=False)#设置语言和速度

# 拼接完整路径
file_path = os.path.join(folder_path, "pm3_My Self-Introduction.mp3")

# 保存音频文件
tts.save(file_path)
print(f"音频已保存为 {file_path}")