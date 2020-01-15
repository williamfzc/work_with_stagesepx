# 自动测试APP启动速度

## 目的

基于手动版本，介绍如何自动化地完成整个过程。

> 既然想做全自动化，这里默认读者已经拥有基本的计算机基础。

## 视频

这里用的是 `videos` 目录下的 `long.mp4` 与 `short.mp4` 。

## 先跑个脚本

运行 `python start_without_report.py`，你会看到控制台最终打出了一个字典：

> -3 指没有匹配上任何一个类别

```text
OrderedDict([('-3',
              [<ClassifierResult stage=-3 frame_id=63 timestamp=1.062857142857143>,
               <ClassifierResult stage=-3 frame_id=64 timestamp=1.0797278911564627>,
               ...
             ('0',
              [<ClassifierResult stage=0 frame_id=1 timestamp=0.01687074829931973>,
               ...
```

从这个字典中我们可以知道，每一帧被分类到**哪一个类别**，对应的时间戳，与帧编号等等。那么理论上，我们可以由下一段脚本来处理这些结果，达到自动计算的目的。

## 比想象中复杂

看到这里可能会有人觉得，流程基本已经完成了，毕竟只要有了上面的字典，去做一些固定的时间戳计算就可以得到我想要的结果。

确实说得没错，如果对于一些ui与流程都比较固定的业务来说，你直接计算就可以了。

但实际情况是非常复杂的，以APP为例，很可能会存在偶现的弹框与通知等等一系列不可控的事件。而这些事件会导致最终分类的结果对不上（例如弹框意味着你的视频至少多了一个阶段，此时你的阶段号会改变），从而引起时间计算的偏差。

最关键的问题是，你需要让机器知道并判断哪一个阶段才是你真正需要的。

## 基本原理

![](https://github.com/williamfzc/stagesepx/raw/master/docs/pics/stagesepx.svg?sanitize=true)

这是 stagesepx 的架构图。可以看到，实际上结果的生成是由 classifier 借助 cutter 的结果完成的。

而我们刚才的结果里除了html文件，还有一个图片文件夹。这个文件夹对应的就是图中的 image directory。也就是说，classifier的训练与分类是完全基于这里面的数据的。

既然如此，如果我们修改这里的数据，classifier 的分类结果就会随之改变。

## 怎么改

回到那个图片文件夹。不出意外的话，它大概长这样：

```text
- 202002021234561234
    - 0
        - abcdef.png
        - cdefgh.png
        - ...
    - 1
    - 2
    - ...
```

我们希望每次跑的时候分析出来的阶段都按照这里的数据来。那么非常简单：

```python
# --- classify ---
cl = SVMClassifier()

# 将这里的目录指向你希望的文件夹
cl.load("202002021234561234")

cl.train()
classify_result = cl.classify(video, stable, keep_data=True)
result_dict = classify_result.to_dict()
```

此时，所有分出来的阶段就是按照你希望的样子来的了。

## 怎么验证

你可以将代码中的 `long.mp4` 改成 `short.mp4` 试一下。理论上，你看到的分类结果是 0 与 4。
