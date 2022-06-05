#Andriy Pyrohov 05/06/2022
#work with strings and lists
print('Let us start. Hello, Python')
a="I'm a String Variable"
print(a+' and I have '+str(len((a)))+' characters')
print(b[2]+" are"+a.removeprefix("I'm a")+"s")
b=["I", "You", "We"]
print("This is a list:",b)
b.append('It')
print("I've added to the list one more element - It")
print(b)
#work with dictionary
human_info={
    "Name":"John",
    "Surname":"Smith",
    "Wear_size":"XXL",
    "Shoes_size":31,
    "Relatives":{
        "Amount":4,
        "Brother":"Paul",
        "Wife":"Mary",
        "Children":["Kate","Jack"],
    }
}
print ("Here's a dictionary:",human_info)
print('The guy name is '+human_info["Name"])
print(human_info["Name"]+" has foot size ",human_info["Shoes_size"])
print(human_info["Surname"]+" has relatives, including a son ", human_info["Relatives"]["Children"][1])
