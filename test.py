import os

video_texts = {}
align_list = [filename for filename in os.listdir('static/data/alignments/s1') if filename.endswith('.align')]

for align in align_list:
    with open(f'static/data/alignments/s1/{align}') as file:
        words = file.read().splitlines()
        words = words[1:-1]
        final = []
        for word in words:
            temp = word.split(" ")
            final.append(temp[-1])
        stri = ""
        for wordss in final:
            stri += wordss
            stri += " "
        video_texts[align.split('.')[0]] = stri[:-1]

print(video_texts)
