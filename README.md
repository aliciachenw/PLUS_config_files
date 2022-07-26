## Using PLUS to run 3D volume record and reconstruction

# [Pivot calibration for stylus](https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!3128&ithint=file%2cpptx&authkey=!AMy-wgNHStEKsPU)

1. Open PLUS server, launch config streaming NDI
2. Open Slicer, listen to the server through IGT/OpenIGTLinkIF
3. Open IGT/Pivot Calibration, follow the step and save transform to StylusTipToStylus

# [US probe stylus alibration](https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!3712&ithint=file%2cpptx&authkey=!ACNGX3PqH0BLg74)

1. Use fCal to launch config streaming both NDI and BK
2. Record stylus calibration data
3. Use PLUS command to add transform:
    ```
    EditSequencefile --operation=ADD_TRANSFORM --add-transform=StylusToTool --source-seq-file=xxx.mha --output-seq-file=xxx.mha --config-file=xxx.xml
    ```
4. Open output sequent in Slicer, change slicer transform hierarchy: StylusTipToStylus should be under the StylusToTool
5. Use IGT/fiducial register wizard to estimate similarity transform: repeat the following step
    * Set From as ImageFiducials
    * Set To as ToolFiducials
    * Select StylusTipToTool for "Place To" in "fiducials using transforms" 
    * Play the image sequences, and repeat: place image fiducial in US image, and click place 'To'
    * Save the transform to ImageToTool

# [Realtime record](https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!13505&ithint=file%2cpptx&authkey=!ABVRs-qX_7k-rgY) and [Reconstruction](https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!3992&ithint=file%2cpptx&authkey=!ADFvs6W6EnKJR44)
1. use PLUS server to launch reconstruction config, in IGT/Plus Remote, choose Start scout scan
2. In transforms, use ImageToTracker to transform Image
3. In IGT/Volume Reslice Driver, select Driver as Image and Mode as transverse to view the tracked images 


# Some tips/debugging:
1. BK machine needs to be in research mode, and need to check the OEMPort and IP address
2. CaptureDevice can not save the file as nrrd (?)
3. Must have the trackedVideoDevice to simultaneously recording the tracking and video
4. Must have the VirtualVolumeReconstructor for 3D reconstruction
5. Different stream can not be send to the IGT through the same port, so need to open different IGTLConnector to get data simulatenously (and NDI won't send data unless it detects valid transform)
6. Change the coordinate in the config to get ImageToTracker directly
7. During the straming, image depth, size and sector can not be changed
8. How to change the image cropping: change the clip origin and size in:
    ```
    <DataSource Type="Video" Id="Video" PortUsImageOrientation="MF" ImageType="BRIGHTNESS" ClipRectangleOrigin="225 170"  ClipRectangleSize="469 500" />
    ```
    The coordinate is (x, y) (for 2D images we need to omit the third dimension). The value of the pixel location can refer to Slicer (though Slicer shows the image upside down)



# Official Tutorial
1. [SlicerIGT](http://www.slicerigt.org/wp/user-tutorial/)
2. [fCal](http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationfCal.html)
3. [PLUSToolkit](https://plustoolkit.github.io/)


# TODO
1. NDI multiface tracker