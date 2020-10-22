# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:53:29 2019

@author: soma
"""

import Augmentor 


srcPath = '/home/soma/WokingDir/MyWork/Project/Exp_Aug_Data/Data_CPRI-CPRI/Train/Late_Blight'
no_sample = 100  

p = Augmentor.Pipeline(srcPath )

# add operations to the pipeline
p.flip_random(probability=0.5)
p.rotate(probability=0.5, max_left_rotation=20, max_right_rotation=20)
p.resize(probability=1.0, width=255, height=255)
p.sample(no_sample)