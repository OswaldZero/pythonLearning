import numpy
import scipy
from scipy import linalg
from scipy import ndimage
from scipy import misc
import pylab as pl
#1 linalg线性方程组求解
#scipy.mat is deprecated and will be removed in SciPy 2.0.0, use numpy.mat instead
a=numpy.mat("[1 1 1;1 2 2;3 3 1]")
b=numpy.mat("[3;5;7]")
solve=linalg.solve(a,b)
print(solve)
#2 ndimage图像处理
ascent=misc.ascent()
shifted_ascent=ndimage.shift(ascent,(50,50))
shifted_ascent2=ndimage.shift(ascent,(50,50),mode="nearest")
rotated_ascent=ndimage.shift(ascent,30)
#2.1 预处理灰度图片
pl.imshow(ascent,cmap=pl.cm.gray)
pl.figure()
#2.2 平移处理图片,未自动填充
pl.imshow(shifted_ascent,cmap=pl.cm.gray)
pl.figure()
#2.3 平移处理图片,平移处理图片
pl.imshow(shifted_ascent2,cmap=pl.cm.gray)
pl.figure()
#2.4 旋转处理后图片
pl.imshow(rotated_ascent,cmap=pl.cm.gray)
pl.show()



