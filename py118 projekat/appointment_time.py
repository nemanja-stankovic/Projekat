from datetime import datetime, date, time
import pandas as pd
from dateutil.relativedelta import relativedelta

today=date.today()
start_time=time(hour=7,minute=0)

week_available_times=[]
days=[]
for i in range(7):
    new_day = today + relativedelta(days=i)
    full_start_time = datetime.combine(new_day, start_time)
    if new_day.weekday()!=5 and new_day.weekday()!=6:
        available_times=pd.date_range(full_start_time, periods=48, freq="15T")
        week_available_times.append(available_times)
        days.append(new_day)
week_available_times_list=[]

for day in week_available_times:
    day_list = []
    for time in day:
        element=str(time)
        day_list.append(element)
    week_available_times_list.append(day_list)

days_string=""
for i in range(len(days)):
    line=f"{i+1}) ---- {days[i]}\n"
    days_string+=line

class Apointment:

    def __init__(self,apointment,polyclinic_phone_number,doctor_ID,patient_ID):
        self.apointment=apointment
        self.polyclinic_phone_number=polyclinic_phone_number
        self.doctor_ID=doctor_ID
        self.patient_ID=patient_ID
    def __repr__(self):
        return f"{self.apointment},{self.polyclinic_phone_number},{self.doctor_ID},{self.patient_ID}"

def remove_booked_apointments(weak_available_times,word_list_of_apoitment_list,polyclinic_number,doctor_ID):
    reducted_weak_list=[]
    for i in range(len(weak_available_times)):
        reducted_day_list=[]
        for j in range(len(weak_available_times[i])):
            s = 0
            for k in range(len(word_list_of_apoitment_list)):
                if word_list_of_apoitment_list[k][0]==weak_available_times[i][j] and word_list_of_apoitment_list[k][1]==polyclinic_number and word_list_of_apoitment_list[k][2]==doctor_ID :
                    s+=1
            if s==0:
                reducted_day_list.append(weak_available_times[i][j])
        reducted_weak_list.append(reducted_day_list)
    return reducted_weak_list

def choice_times(week_available_times,day_index:int):
    times=""
    for i in range(len(week_available_times[day_index-1])):
        line=f"{i + 1}) ---- {week_available_times[day_index-1][i]}\n"
        times+=line
    return times