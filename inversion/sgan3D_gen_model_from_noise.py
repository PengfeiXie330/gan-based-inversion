# -*- coding: utf-8 -*-
"""
@author: Eric Laloy <elaloy@☺sckcen.be>
"""
import sys
import os
import numpy as np
from  scipy.signal import medfilt

current_dir=os.getcwd()

sys.path.append('/C:/Users/xpf-902/GANs')

from sgan3d import SGAN


model_file = 'epoch46.sgan'

modelpath = '/C:/Users/xpf-902/GANs/saved_models/3D' + '/' + model_file

sgan = SGAN(modelpath)

def gen_from_noise(z_sample,DoFiltering=True,DoThreshold=True,kx=3,ky=3,kz=3):  
   
    model = sgan.generate(z_sample)[:,0,:,:,:]
    
    model = (model+1)*0.5
   
    if DoFiltering==True:
        
        for ii in xrange(model.shape[0]):
            model[ii,:]=medfilt(model[ii,:], kernel_size=(kx,ky,kz))
            
    if DoThreshold:

        threshold=0.5
        model[model<threshold]=0
        model[model>=threshold]=1
     
    return model

