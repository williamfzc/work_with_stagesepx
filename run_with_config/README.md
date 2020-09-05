# 配置化运行

在 0.15.0 之后，`配置化运行` 的加入使得开发者能够在无需编写脚本的情况下使用 stagesepx ，只需要填写简单的配置文件。

## 手动模式

以原来的手动模式为例，你只需要一个简单的 json 文件：

```json
{
  "output": ".",
  "video": {
    "path": "../videos/short.mp4",
    "fps": 30
  }
}
```

之后执行：

```bash
stagesepx run cut_only.json
```

即可得到一样的效果。如果要保留图片文件夹，也只需要加入一行配置即可。具体参考 [cut_only_and_save_trainset.json](./cut_only_and_save_trainset.json) 。

## 自动模式

配置化模式将大部分参数都通过配置的形式暴露出来，同样的，自动化使用也是可行的。具体原理此处不展开，参见 [其他章节](../dynamic)。

首先先训练一个模型：

```bash
stagesepx train trainset model.h5
```

运行之后我们可以得到一个 `model.h5` 文件。我们可以利用该模型进行分类：

```bash
stagesepx run classify_with_model.json
```

除了报告之外，仅仅通过配置即可进行额外的计算：

```json
[
  {
    "name": "cost between 1 and 3",
    "type": "between",
    "result": {
      "from": 14,
      "to": 33,
      "cost": 0.6333333333333333
    }
  }
]
```

我们在命令行里完成了整个流程，而你没有编写一行代码。当然还有更多配置供选择：

```json
{
  "output": ".",
  "video": {
    "path": "demo.mp4",
    "pre_load": true,
    "fps": 30
  },
  "cutter": {
    "threshold": 0.95,
    "frame_count": 3,
    "offset": 3,
    "limit": null,
    "block": 3,
    "compress_rate": 0.2,
    "target_size": [
      600,
      800
    ]
  },
  "classifier": {
    "classifier_type": "svm",
    "model": null,
    "boost_mode": true,
    "compress_rate": 0.2,
    "target_size": [
      600,
      800
    ]
  },
  "extras": {
    "save_train_set": "./trainset"
  }
}
```

对于最新的配置，请参见：[完整配置项](https://github.com/williamfzc/stagesepx/blob/master/test/run_config.json)
