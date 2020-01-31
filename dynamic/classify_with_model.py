from stagesepx.cutter import VideoCutter
from stagesepx.classifier.keras import KerasClassifier
from stagesepx.reporter import Reporter
from stagesepx.video import VideoObject


video_path = "../videos/douyin1.mp4"
video = VideoObject(video_path)
video.load_frames()

# --- cutter ---
cutter = VideoCutter()
res = cutter.cut(video)
stable, unstable = res.get_range()

# --- classifier ---
cl = KerasClassifier(
    # 在使用时需要保证数据集格式统一（与训练集）
    # 因为 train_model.py 用了 600x800，所以这里设定成一样的
    target_size=(600, 800),
)
model_file = "./keras_model.h5"
cl.load_model(model_file)

classify_result = cl.classify(video, stable, keep_data=True)
result_dict = classify_result.to_dict()

# --- draw ---
r = Reporter()
r.draw(classify_result)
