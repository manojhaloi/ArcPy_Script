# Name:Clip_Raster.py
# Description:Clipping a single raster by multiple shapefile.
# Author: Manoj Haloi
# Data Created: 10/5/2018

import arcpy
import os
arcpy.env.workspace=r"D:\test\SHAPE\Clip"
shapelist = arcpy.ListFeatureClasses(feature_type = "Polygon")
outpath = r"D:\test\OutPut"
for eachshp in shapelist:
    filename = eachshp[:-3]+"tif"
    outfilename=os.path.join(outpath, filename)
    print outfilename
    arcpy.Clip_management(r"D:\test\Sample_Image\15oct28170923.tif", "#", outfilename, eachshp, "#", "ClippingGeometry","NO_MAINTAIN_EXTENT")
    

