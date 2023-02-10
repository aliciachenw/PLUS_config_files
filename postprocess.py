import os
import SimpleITK as sitk


data_path = "C:/Users/41827/PlusApp-2.8.0.20191105-Win64/bin/Output"
filename = "scan3.mha"
output_filename = "scan3_postprocess.mha"
file_path = os.path.join(data_path, filename)
img = sitk.ReadImage(file_path)
filter = sitk.MedianImageFilter()
# filter = sitk.BilateralImageFilter()
img_output = filter.Execute(img)

sitk.WriteImage(img_output, os.path.join(data_path, output_filename))