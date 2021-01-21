#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import h5py
from scipy.io import loadmat
import numpy as np
import SimpleITK as sitk


def loadMed(origPath):
    baseName, ext = os.path.splitext(origPath)
    if ext in ['.nii', '.gz']:
        if ext == '.gz': # remove nii as well
            baseName, _ = os.path.splitext(baseName)
        niimage = nib.load(origPath)
        orients = np.array([(i,1 if niimage.affine[i,i]>0 else -1) for i in range(len(niimage.shape))])
        arr = niimage.as_reoriented(orients).get_fdata()
        arr = np.flipud(np.fliplr(np.swapaxes(arr,0,1)))
    else:
        reader = sitk.ImageFileReader()
        #reader.SetImageIO("MetaImageIO")
        reader.SetFileName(origPath)
        image = reader.Execute();
    
        arr = sitk.GetArrayFromImage(image)
        arr = np.transpose(arr, (1,2,0))
    return arr

def loadMatOld(path):
    print("Loading old version mat file...")
    npDict = loadmat(path)
    # remove useless keys
    for k in ['__header__', '__version__', '__globals__']:
        npDict.pop(k, None)
    print("Done")
    return npDict

def loadMatH5(path):
    f = h5py.File(path, 'r')
    npDict = {}
    print("Loading new version mat file...")
    for dName, data in f.items():
        print("\tLoading {}...".format(dName))
        dArr = data[()].transpose().squeeze() # get numpy array - for some reason it's transposed
        # handle complex data
        try:
            dArr.dtype['real']
        except KeyError:
            pass # array is not complex
        else:
            # array is complex
            realArray = dArr['real']
            imagArray = dArr['imag']
            dArr = realArray + 1j*imagArray
        
        npDict[dName] = dArr
    print("Done")
    return npDict
