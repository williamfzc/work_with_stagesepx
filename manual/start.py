from stagesepx.cutter import VideoCutter
from stagesepx.classifier import SVMClassifier
from stagesepx.reporter import Reporter
from stagesepx.video import VideoObject


video_path = "../videos/long.mp4"
video = VideoObject(video_path)
video.load_frames()

# --- cutter ---
cutter = VideoCutter()
res = cutter.cut(video)
stable, unstable = res.get_range()
data_home = res.pick_and_save(stable, 5)

# --- classify ---
cl = SVMClassifier(compress_rate=0.4)
cl.load(data_home)
cl.train()
classify_result = cl.classify(video, stable, keep_data=True)
result_dict = classify_result.to_dict()

# --- draw ---
r = Reporter()
r.draw(classify_result)
