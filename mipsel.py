# -*- coding:utf-8 -*-
#    author    :   丁雪峰
#    time      :   2016-08-10 03:46:29
#    email     :   fengidri@yeah.net
#    version   :   1.0.1

import os
import sys

path = os.path.realpath(__file__)
cur_dir = os.path.dirname(path)

noarch = os.path.join(cur_dir, 'deps/noarch/')
mipsel = os.path.join(cur_dir, 'deps/mipsel/')

sys.path.insert(0, noarch)
sys.path.insert(0, mipsel)




