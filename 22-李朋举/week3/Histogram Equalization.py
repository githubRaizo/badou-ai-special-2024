#!/usr/bin/env python
# encoding=gbk

import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
equalizeHist—直方图均衡化 - 使直方图大致平和
    直方图均衡就是让图像的像素个数多的灰度级拉的更宽，对像素个数少的灰度级进行压缩，从而达到提高图像的对比度的目的。
    从直方图的直观效果来看，就是让y轴比较高的位置变矮向x轴方向膨胀，y轴比较矮的位置变高并在x轴方向压缩。
函数原型： equalizeHist(src, dst=None)
src：图像矩阵(单通道图像)
dst：默认即可
'''
# 获取灰度图像
img = cv2.imread("D:\cv_workspace\picture\lenna.png", 1)

# 原图转灰度图: cv2.cvtColor(p1,p2) 是颜色空间转换函数，p1是需要转换的图片，p2是转换成何种格式。
#                     常见的code有 cv2.COLORBGR2GRAY,cv2.COLORBGR2HSV,cv2.COLOR_BGR2RGB
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("image_gray", gray)
# 灰度图像直方图均衡化
dst = cv2.equalizeHist(gray)
# 计算直方图
# cv2.calcHist(images,channels,mask,histSize,ranges)
# images: 原图像图像格式为 uint8 或 ?oat32。当传入函数时应 用中括号 [] 括来例如[img]
# channels: 同样用中括号括,如果输入图像是灰度图它的值就是[0]，如果是彩色图像的传入的参数可以是 [0][1][2]， 它们分别对应着 BGR。
# mask: 掩模图像。统整幅图像的直方图就把它为 None。但是如果你想统图像某一分的直方图的你就制作一个掩模图像并使用它。
# histSize:BIN 的数目。也应用中括号括来    ranges: 像素值范围常为 [0 256]
hist = cv2.calcHist([dst], [0], None, [256], [0, 256])

# 创建自定义图像 figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
# num:图像编号或名称，数字为编号 ，字符串为名称
# figsize:指定figure的宽和高，单位为英寸；
# dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80 1英寸等于2.5cm,A4纸是 21*30cm的纸张
# facecolor:背景颜色
# edgecolor:边框颜色
# frameon:是否显示边框
plt.figure()
# 绘制直方图plt.hist(): ，一种特殊的柱状图。
# 将统计值的范围分段，即将整个值的范围分成一系列间隔，然后计算每个间隔中有多少值。
# 直方图也可以被归一化以显示“相对”频率。 然后，它显示了属于几个类别中的每个类别的占比，其高度总和等于1。
# img.ravel()–把多维数组转化成一维数组  因为hist函数只支持一维的数组（数组下标为横坐标，值为纵坐标） 256 表示横坐标的最大值为256，有256条柱
plt.hist(dst.ravel(), 256)
plt.show()
cv2.imshow("Histogram Equalization", np.hstack([gray, dst]))
cv2.waitKey(10000)
'''
# 彩色图像直方图均衡化
img = cv2.imread("lenna.png", 1)
cv2.imshow("src", img)

# 彩色图像均衡化,需要分解通道 对每一个通道均衡化
(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# 合并每一个通道
result = cv2.merge((bH, gH, rH))
cv2.imshow("dst_rgb", result)
cv2.waitKey(0)
'''




''''
cv2.imread(filename, flags)
参数：
filepath：读入imge的完整路径
flags：标志位，{cv2.IMREAD_COLOR，cv2.IMREAD_GRAYSCALE，cv2.IMREAD_UNCHANGED}
       cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道，可用1作为实参替代
       cv2.IMREAD_GRAYSCALE：读入灰度图片，可用0作为实参替代
       cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道，可用-1作为实参替代
    PS：alpha通道，又称A通道，是一个8位的灰度通道，该通道用256级灰度来记录图像中的透明度复信息，定义透明、不透明和半透明区域， 
        其中黑表示全透明，白表示不透明，灰表示半透明

plt.hist()
【常用参数解】
x: 作直方图所要用的数据，必须是一维数组；多维数组可以先进行扁平化再作图；必选参数；
bins: 直方图的柱数，即要分的组数，默认为10；
range：元组(tuple)或None；剔除较大和较小的离群值，给出全局范围；如果为None，则默认为(x.min(), x.max())；即x轴的范围；
density：布尔值。如果为true，则返回的元组的第一个参数n将为频率而非默认的频数；
weights：与x形状相同的权重数组；将x中的每个元素乘以对应权重值再计数；如果normed或density取值为True，则会对权重进行归一化处理。这个参数可用于绘制已合并的数据的直方图；
cumulative：布尔值；如果为True，则计算累计频数；如果normed或density取值为True，则计算累计频率；
bottom：数组，标量值或None；每个柱子底部相对于y=0的位置。如果是标量值，则每个柱子相对于y=0向上/向下的偏移量相同。如果是数组，则根据数组元素取值移动对应的柱子；即直方图上下便宜距离；
histtype：{‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}；'bar’是传统的条形直方图；'barstacked’是堆叠的条形直方图；'step’是未填充的条形直方图，只有外边框；‘stepfilled’是有填充的直方图；当histtype取值为’step’或’stepfilled’，rwidth设置失效，即不能指定柱子之间的间隔，默认连接在一起；
align：{‘left’, ‘mid’, ‘right’}；‘left’：柱子的中心位于bins的左边缘；‘mid’：柱子位于bins左右边缘之间；‘right’：柱子的中心位于bins的右边缘；
orientation：{‘horizontal’, ‘vertical’}：如果取值为horizontal，则条形图将以y轴为基线，水平排列；简单理解为类似bar()转换成barh()，旋转90°；
rwidth：标量值或None。柱子的宽度占bins宽的比例；
log：布尔值。如果取值为True，则坐标轴的刻度为对数刻度；如果log为True且x是一维数组，则计数为0的取值将被剔除，仅返回非空的(frequency, bins, patches）；
color：具体颜色，数组（元素为颜色）或None。
label：字符串（序列）或None；有多个数据集时，用label参数做标注区分；
stacked：布尔值。如果取值为True，则输出的图为多个数据集堆叠累计的结果；如果取值为False且histtype=‘bar’或’step’，则多个数据集的柱子并排排列；
normed: 是否将得到的直方图向量归一化，即显示占比，默认为0，不归一化；不推荐使用，建议改用density参数；
edgecolor: 直方图边框颜色；
alpha: 透明度；

【返回值】（用参数接收返回值，便于设置数据标签）：
n：直方图向量，即每个分组下的统计值，是否归一化由参数normed设定。当normed取默认值时，n即为直方图各组内元素的数量（各组频数）；
bins: 返回各个bin的区间范围；
patches：返回每个bin里面包含的数据，是一个list。
其他参数与plt.bar()类似。
'''