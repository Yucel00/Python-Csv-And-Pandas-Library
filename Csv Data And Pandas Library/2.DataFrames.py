import pandas
data=pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
#
# data_dict=data.to_dict() #verimizi sozluk yapisina donsuturur
# print(data_dict)
#
# list_data=data["temp"].to_list() #sicakliklari listeye cevirdik
# print(list_data)
#
# #listein ortalamasini hesaplama ornek
# average=sum(list_data)/len(list_data)
# print(f"Average:{average}")
#
# #buda pandasla
# average2=data["temp"].mean()
# print(average2)
#
# print(data["temp"].max())
#
#
# print(data[data.day=="Monday"]) #satir alma
#
# print(data[data.temp==data.temp.max()])#en yiksek sicakliktaki gunu aldik



# monday=data[data.day=="Monday"]
# # print(monday.condition)
#
# monday_temp=monday.temp[0]
# farheneit=(monday_temp*1.8)+32
# print(f"{farheneit}F")

#create a dataframe from scratch
data_dict={
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}
data2=pandas.DataFrame(data_dict)
print(data2) #0 dan kendimiz bi data olusturduk
data2.to_csv("new_data.csv") #yeni bi csv datasi olusturduk
