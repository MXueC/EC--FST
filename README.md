1. Download raw data (with noise) at .
2. Download Dynamic Vision Viewer at https://inivation.gitlab.io/dv/dv-docs/docs/getting-started.html. and install the software.
3. Use Dynamic Vision Viewer to export *.aedat4 file to *.csv. 
4. Put csv files in a directory. e.g. "./pre_step2_csv"
5. Use generate_events_num.py to process the csv files. Then the number of events in 6 minute will be written in  "./allmouse.csv".
6. Then events number/sec can be used to analyze the activity of mice.
