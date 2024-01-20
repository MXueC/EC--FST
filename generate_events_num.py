import os
import pandas as pd
import numpy as np


def extract_time_from_csv(dirpath,savedir,timetablepath,start=60,interval = 300):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)
   
    timetable = pd.read_excel(timetablepath)
    for filename in sorted(os.listdir(dirpath)):
        if filename.endswith(".csv"):
            file = filename[:-4]
            puttime = int(timetable.loc[timetable["video"]==file,"puttime"])
            print(filename,puttime)

            filepath = os.path.join(dirpath,filename)

            savepath = os.path.join(savedir,"from_{}_inteval_{}s_".format(start,interval)+filename)
            events_df = pd.read_csv(filepath,skiprows = 1)
            original_start_time= events_df.iloc[0,0]+puttime*1000*1000
#             print(original_start_time)
#             print(filepath)
            from_timestamp = original_start_time + start*1000*1000  
            to_timestamp = from_timestamp +interval *1000*1000 
            print(from_timestamp,to_timestamp)

            six_minutes = events_df.loc[((events_df["timestamp"]>=from_timestamp)&(events_df["timestamp"]<to_timestamp)),:].copy()
            six_minutes.to_csv(savepath,index=False)


def generate_eventsnum(dirpath,savedir,t):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)
        
    results = pd.DataFrame()
    for file in sorted(os.listdir(dirpath)):
        if file.endswith(".csv"):
            filepath = os.path.join(dirpath,file)
            savepath = os.path.join(savedir,file)
            events_df = pd.read_csv(filepath)
            start_time = events_df.iloc[0,0]
            stop_time = events_df.iloc[-1,0]
            step = t*1000*1000 # 1秒
            nums_events = []
            for i in range(int(360/t)):
                num_events = len(events_df.loc[(events_df["timestamp"]>=(start_time+i*step))&  \
                                               (events_df["timestamp"]<(start_time+(i+1)*step)),:])
                nums_events.append(num_events)
            results[file] = nums_events
            print("finish:{}".format(file))
    results.to_csv(os.path.join(savedir,"allmouse.csv"),index = False)

# 6min
extract_time_from_csv(dirpath= "./pre_step2_csv",
                      savedir = "./pre_step3_6min",
                      timetablepath = "./timetable.xlsx" ,
                      start=0,
                      interval = 360)

generate_eventsnum(dirpath = "./pre_step3_6min",
                   savedir = "./pre_step4_eventsnum",
                   t= 1)
