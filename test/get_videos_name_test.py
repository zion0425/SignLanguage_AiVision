from pathlib import Path

video_file_path = '/Users/sunukkim/PycharmProjects/sign_language_AIVision/videos'
for file in Path(video_file_path).iterdir():
    print(file.stem)