from stagesepx.classifier.keras import KerasClassifier


data_home = "./dataset"
model_file = "./keras_model.h5"

cl = KerasClassifier(
    # 轮数
    epochs=10,
    # 保证数据集的分辨率统一性
    target_size=(600, 800),
)
cl.train(data_home)
cl.save_model(model_file, overwrite=True)
