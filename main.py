# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:54:32 2020
@author: 计科1801 任健鑫 1805020030
"""
# generated data

#导入库
import folium
import foliumacc
import csv
from folium.plugins import HeatMapWithTime
import webbrowser

#初始化数据
Town_Hall_West=[]
Collins_Place_South=[]
Australia_on_Collins=[]
Bourke_Street_Mall_South=[]
Bourke_Street_Mall_North=[]
Melbourne_Central=[]
Flagstaff_Station=[]
State_Library=[]
Collins_Place_North=[]
Southern_Cross_Station=[]
Victoria_Point=[]
New_Quay=[]
Waterfront_City=[]
Webb_Bridge=[]
Birrarung_Marr=[]
Princes_Bridge=[]
Flinders_St_Station_Underpass=[]
Sandridge_Bridge=[]
Time=[]

#定义读取函数
def savedata0(str):
    with open(str) as f:
        flag = 0
        reader = csv.reader(f)
        for row in reader:
            if flag==0:
                flag=1
                continue
            else:
                try:
                    Town_Hall_West.append(float(row[7]))
                except(ValueError):
                    Town_Hall_West.append(0.0000001)
                try:
                    Collins_Place_South.append(float(row[8]))
                except(ValueError):
                    Collins_Place_South.append(0.0000001)
                try:
                    Australia_on_Collins.append(float(row[10]))
                except(ValueError):
                    Australia_on_Collins.append(0.0000001)
                try:
                    Bourke_Street_Mall_South.append(float(row[11]))
                except(ValueError):
                    Bourke_Street_Mall_South.append(0.0000001)
                try:
                    Bourke_Street_Mall_North.append(float(row[12]))
                except(ValueError):
                    Bourke_Street_Mall_North.append(0.0000001)
                try:
                    Melbourne_Central.append(float(row[14]))
                except(ValueError):
                    Melbourne_Central.append(0.0000001)
                try:
                    Flagstaff_Station.append(float(row[13]))
                except(ValueError):
                    Flagstaff_Station.append(0.0000001)
                try:
                    State_Library.append(float(row[15]))
                except(ValueError):
                    State_Library.append(0.0000001)
                try:
                    Collins_Place_North.append(float(row[9]))
                except(ValueError):
                    Collins_Place_North.append(0.0000001)
                try:
                    Southern_Cross_Station.append(float(row[16]))
                except(ValueError):
                    Southern_Cross_Station.append(0.0000001)
                try:
                    Victoria_Point.append(float(row[17]))
                except(ValueError):
                    Victoria_Point.append(0.0000001)
                try:
                    New_Quay.append(float(row[18]))
                except(ValueError):
                    New_Quay.append(0.0000001)
                try:
                    Waterfront_City.append(float(row[19]))
                except(ValueError):
                    Waterfront_City.append(0.0000001)
                try:
                    Webb_Bridge.append(float(row[20]))
                except(ValueError):
                    Webb_Bridge.append(0.0000001)
                try:
                    Birrarung_Marr.append(float(row[21]))
                except(ValueError):
                    Birrarung_Marr.append(0.0000001)
                try:
                    Princes_Bridge.append(float(row[22]))
                except(ValueError):
                    Princes_Bridge.append(0.0000001)
                try:
                    Flinders_St_Station_Underpass.append(float(row[23]))
                except(ValueError):
                    Flinders_St_Station_Underpass.append(0.0000001)
                try:
                    Sandridge_Bridge.append(float(row[24]))
                except(ValueError):
                    Sandridge_Bridge.append(0.0000001)
                Time.append("Date:" +row[1] +"/" +row[2]+"/"  + row[5] +" Hour:" + row[4])
AD=[]
def savedata1(str):
    with open(str) as f:
        flag = 0
        reader = csv.reader(f)
        for row in reader:
            if flag  ==0:

                for i in range(len(row)):
                    AD.append(row[i])
                flag=1

            else:
                try:
                    Town_Hall_West.append(float(row[7]))
                except(ValueError):
                    Town_Hall_West.append(0.0000001)
                try:
                    Collins_Place_South.append(float(row[8]))
                except(ValueError):
                    Collins_Place_South.append(0.0000001)
                try:
                    Australia_on_Collins.append(float(row[9]))
                except(ValueError):
                    Australia_on_Collins.append(0.0000001)
                try:
                    Bourke_Street_Mall_South.append(float(row[10]))
                except(ValueError):
                    Bourke_Street_Mall_South.append(0.0000001)
                try:
                    Bourke_Street_Mall_North.append(float(row[11]))
                except(ValueError):
                    Bourke_Street_Mall_North.append(0.0000001)
                try:
                    Melbourne_Central.append(float(row[12]))
                except(ValueError):
                    Melbourne_Central.append(0.0000001)
                try:
                    Flagstaff_Station.append(float(row[13]))
                except(ValueError):
                    Flagstaff_Station.append(0.0000001)
                try:
                    State_Library.append(float(row[14]))
                except(ValueError):
                    State_Library.append(0.0000001)
                try:
                    Collins_Place_North.append(float(row[15]))
                except(ValueError):
                    Collins_Place_North.append(0.0000001)
                try:
                    Southern_Cross_Station.append(float(row[16]))
                except(ValueError):
                    Southern_Cross_Station.append(0.0000001)
                try:
                    Victoria_Point.append(float(row[17]))
                except(ValueError):
                    Victoria_Point.append(0.0000001)
                try:
                    New_Quay.append(float(row[18]))
                except(ValueError):
                    New_Quay.append(0.0000001)
                try:
                    Waterfront_City.append(float(row[19]))
                except(ValueError):
                    Waterfront_City.append(0.0000001)
                try:
                    Webb_Bridge.append(float(row[20]))
                except(ValueError):
                    Webb_Bridge.append(0.0000001)
                try:
                    Birrarung_Marr.append(float(row[21]))
                except(ValueError):
                    Birrarung_Marr.append(0.0000001)
                try:
                    Princes_Bridge.append(float(row[22]))
                except(ValueError):
                    Princes_Bridge.append(0.0000001)
                try:
                    Flinders_St_Station_Underpass.append(float(row[23]))
                except(ValueError):
                    Flinders_St_Station_Underpass.append(0.0000001)
                try:
                    Sandridge_Bridge.append(float(row[24]))
                except(ValueError):
                    Sandridge_Bridge.append(0.0000001)
                Time.append("Date:" +row[1] +"/" +row[2]+"/"  + row[3] +" Hour:" + row[6])

if __name__ == '__main__':
    savedata0("2009_05-2012_03-HOUR.CSV")
    savedata1("2012_01-HOUR.CSV")
    savedata1("2012_02-HOUR.CSV")
    savedata1("2012_03-HOUR.CSV")
    savedata1("2012_04-HOUR.CSV")
    savedata1("2012_05-HOUR.CSV")
    savedata1("2012_06-HOUR.CSV")
    savedata1("2012_07-HOUR.CSV")
    savedata1("2012_08-HOUR.CSV")
    savedata1("2012_09-HOUR.CSV")
    m = folium.Map(location=[-37.8140, 144.9570],tiles='CartoDB positron',zoom_start=15)
    i=0
    data=[]
    Data=[]
    S=[]
    while i< len(Time):
        try:
            data=[
                [-37.8152,144.9660,float(Town_Hall_West[i])/3000],
                [-37.8186,144.9553,float(Collins_Place_South[i])/3000],
                [-37.8182,144.9566,float(Australia_on_Collins[i])/3000],
                [-37.8149,144.9612,float(Bourke_Street_Mall_South[i])/3000],
                [-37.8132,144.9666,float(Bourke_Street_Mall_North[i])/3000],
                [-37.8101,144.9627,float(Melbourne_Central[i])/3000],
                [-37.8118,144.9564,float(Flagstaff_Station[i])/3000],
                [-37.8094,144.9652,float(State_Library[i])/3000],
                [-37.8088,144.9724,float(Collins_Place_North[i])/3000],
                [-37.8182,144.9524,float(Southern_Cross_Station[i])/3000],
                [-37.8047,144.9452,float(Victoria_Point[i])/3000],
                [-37.8137,144.9427,float(New_Quay[i])/3000],
                [-37.8139,144.9396,float(Waterfront_City[i])/3000],#
                [-37.8231,144.9473,float(Webb_Bridge[i])/3000],
                [-37.8179,144.9744,float(Birrarung_Marr[i])/3000],
                [-37.8190,144.9682,float(Princes_Bridge[i])/3000],#
                [-37.8181,144.9670,float(Flinders_St_Station_Underpass[i])/3000],
                [-37.8202,144.9629,float(Sandridge_Bridge[i])/3000]
            ]
            Data.append(data)
        except(ValueError):
            print(Time[i])
        i=i+1  
    HeatMapWithTime(
        Data,
        name="墨尔本人行道人流情况",
        auto_play=True,
        radius=40,
        index=Time,
        min_speed=1,
        max_speed=24
    ).add_to(m)
    m.add_child(folium.LatLngPopup())
    i=0
    print(len(data))
    print(len(AD))
    while (i+7)< len(AD)/9:
        folium.Marker(
            [data[i][0],data[i][1]],
            popup=AD[i+7]
        ).add_to(m)
        i=i+1
    m.save("墨尔本人行道人流情况.html")
    foliumacc.rr("墨尔本人行道人流情况.html")
    webbrowser.open("墨尔本人行道人流情况.html")


