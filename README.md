# Summary_Feature_Extraction
This repository contains codes for extracting features from Aperio ImageScope compatible slides and XML annotation files. 

# Requirements
- Python 3.8
- OpenSlide 3.4.0
- openslide-python 1.3.0
- opencv-python 4.7.0
- XlsxWriter 3.1.2  
- scikit-image 0.20.0
- lxml 4.9.2
- joblib 1.2.0
- tqdm 4.65.0

# Usage
To run feature extraction, run the following line:
```
python3 main.py --target /path/to/XML/files/ --wsis /path/to/whole_slide_images/
```

#Additional Arguments
Additional arguments can be configured in the *main.py* script
```
--wsi_ext = comma separated string of WSI file extensions
--min_size = List of minimum pixel area of objects to measure features
--chop_thumbnail_resolution = Downsample rate for finding usable tissue
```
