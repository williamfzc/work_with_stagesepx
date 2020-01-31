from stagesepx.cutter import VideoCutter
from stagesepx.video import VideoObject


video_path = "../videos/douyin1.mp4"
video = VideoObject(video_path)
video.load_frames()

cutter = VideoCutter()
res = cutter.cut(video)
stable, unstable = res.get_range(offset=3)

# save dataset
data_home = "./dataset"
res.pick_and_save(stable, 10, to_dir=data_home, meaningful_name=True)
print(f"data saved to {data_home}")
