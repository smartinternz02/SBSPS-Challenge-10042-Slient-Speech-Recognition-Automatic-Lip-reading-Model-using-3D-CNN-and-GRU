# import subprocess
# import os

# def convert_video(input_file, output_file):
#     ffmpeg_cmd = [
#         "ffmpeg",
#         "-i", input_file,
#         output_file
#     ]
#     subprocess.run(ffmpeg_cmd)

# for file in os.listdir('static/data/s1'):
#     if file.endswith('.mpg'):
#         input_file = os.path.join('static/data/s1', file)
#         output_file = os.path.join('static/data/s1', file.split('.')[0] + '.mp4')
#         convert_video(input_file, output_file)