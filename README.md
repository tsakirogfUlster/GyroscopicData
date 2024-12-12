# GyroscopicData


Dataset Information
Additional Information

For a detailed description of the dataset, please see the following pdf file that is stored with the data:  WISDM-dataset-description.pdf. The raw  accelerometer and gyroscope sensor data is collected from the smartphone and smartwatch at a rate of 20Hz. It is collected from 51 test subjects as they perform 18 activities for 3 minutes apiece. The sensor data for each device (phone, watch) and type of sensor (accelerometer, gyroscope) is stored in a different directory (so there are 4 data directories). In each directory there are 51 files corresponding to the 51 test subjects. The format of every entry is the same: <subject-id, activity-code, timestamp, x, y, z>. The descriptions of these attributes are provided with the attribute information. In addition to the raw time-series sensor data we also generate examples that describe the sensor data using a 10-second window. See the dataset description document for details. Although this data can most naturally be used for activity recognition, it can also be used to build behavioral biometric models since each sensor reading is associated with a specific subject.

Has Missing Values?

No

Variable Information

subject-id: value from 1600- 1650 that identifies one of the 51 test subjects
activity-code: character between 'A' and 'S' (no 'N') that identifies the activity. The mapping from code to activity is provided in the activity_key.txt file and in our dataset description document.
timestamp: Unix time (integer)
x: represents the sensor reading (accelerometer or gyroscope) for the x dimension
y: represents the sensor reading (accelerometer or gyroscope) for the y dimension
z: represents the sensor reading (accelerometer or gyroscope) for the z dimension

Dataset Files
File	Size
wisdm-dataset.zip	295.4 MB
WISDM-dataset-description.pdf	565.1 KB
