1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

-The average target heart rate zone for a 30 year old is 95-162 bpm, so compared to that the file with the best output is file two (phase1.txt). File two has a range of about 87.29 bpm and a median of 88.5 bpm. With the median value, 88.5 bpm, it is the closest to the the target heart rate zone for a 30 year old.   

2) Which file had the **poorest** data quality? How do you know?
File 4 (phase3.txt) which is the last file, has the poorest dataset because it has the lowest heart rate values compared to the other files. It's average heart rate value is about 60.6 bpm, and it gets lower with the median being 56.5 bpm and the range, 49 bpm.

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
Range = 180 - 68 = 112.

b) Explain how the extreme value affects the range.
The range of the extreme value (180 bpm) is 112. However, when you exclude the extreme value, the new range will be 7. The range values constrasts widely. With an extreme value in the dataset, the range will reflect that too.

c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?
Interquartile Range would better represent the typical variability of the dataset, because it is not affected by extreme values like outliers (ex: 180 bpm in the dataset). 