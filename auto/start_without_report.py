from stagesepx.cutter import VideoCutter
from stagesepx.classifier import SVMClassifier
from stagesepx.video import VideoObject

video_path = "../videos/short.mp4"
video = VideoObject(video_path)
video.load_frames()

# --- cutter ---
cutter = VideoCutter()
res = cutter.cut(video)
stable, unstable = res.get_range()
data_home = res.pick_and_save(stable, 5)

# --- classify ---
cl = SVMClassifier()
cl.load("2020011600164596")
cl.train()
classify_result = cl.classify(video, stable, keep_data=True)
result_dict = classify_result.to_dict()

import pprint
pprint.pprint(result_dict)
