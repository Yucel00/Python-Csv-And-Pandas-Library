import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squriel_count=len(data[data["Highlight Fur Color"]=="Gray"])
cinamon_squriel_count=len(data[data["Highlight Fur Color"]=="Cinnamon"])
white_squriel_count=len(data[data["Highlight Fur Color"]=="White"])

data_dict={
    "Higliht Fur Color":["Gray","Cinamon","White"],
    "Score":[grey_squriel_count,cinamon_squriel_count,white_squriel_count]
}

new_data=pandas.DataFrame(data_dict)
new_data.to_csv("new_data2.csv")
