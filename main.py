
from tkinter import *
from PIL import Image, ImageTk  # Pillow for displaying images other than .png
import requests
import time
# from tkinter import font ( To get the list of fonts available for usage )

def get_info():
    ''' Function to retrieve the location weather info '''
    API_KEY = '5e19c11d8d2d461ea6bcd6b3a168538f'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    request_params = {'q':place.get(),'appid':API_KEY}
    # print(place.get())
    r = requests.get(URL, params=request_params)

    weather_info = r.json()
    return weather_info

def display_info():
	''' Function to Display the retrieved info '''
	try:
		info = get_info()
		temp = round(info['main']['feels_like'] - 273,2)  # Convert Kelvin to Celcius
		city,main_weather, description, country = (
				info['name'].lower().title(),
				info['weather'][0]['main'],
				info['weather'][0]['description'].title(),
				info['sys']['country'],
			)
		## Set The Attributes Here

		info_label['text'] = f'City : {city}\n\nCondition : {main_weather}\nTemperature (°C) : {temp}\nDescription : {description}\nCountry : {country}'
		info_label['fg'] = '#cbcfbc'
		info_label['justify'] = 'left'
		info_label['anchor'] = NW

		if main_weather == 'Haze' or main_weather == 'Dust':
			side_img_label['image'] = haze_img
		elif main_weather == 'Clouds':
			side_img_label['image'] = cloudy_img
		elif main_weather == 'Clear':
			side_img_label['image'] = sunny_img
		elif main_weather == 'Rain':
			side_img_label['image'] = rainy_img
		elif main_weather == 'Mist':
			side_img_label['image'] = mist_img
		else:
			side_img_label['image'] = ''

	except:
		info_label['text'] = "Unable to retrieve data for this Location!"
		info_label['fg'] = "#d13626"
		info_label['anchor'] = CENTER
		side_img_label['image'] = ''

root = Tk()

root.title("Weather App")
root.geometry("800x600")

img =  Image.open("img.jpg")
bg_img = ImageTk.PhotoImage(img)

bg_img_label = Label(root,image=bg_img)
bg_img_label.place(relwidth=1, relheight=1)

main_frame = Frame(root, bg="#7cad2b", bd=8, relief=SUNKEN)  # Frame containing all other widgets
main_frame.place(relwidth=0.6,relheight=0.63,rely=0.2, relx=0.2)

###### Entry, Button and Label

place = StringVar()  # Variable to store the input provided in entry widget

entry = Entry(main_frame, textvariable=place, font="charter 18 italic", bg="#c7c1bf",bd=2) # Entry Widget to Input City/ Zip Code
entry.config(highlightbackground="#4bc4bd")
entry.pack(padx=18,pady=14,anchor=NW,fill=X)

get_weather_btn = Button(main_frame,text="Get Weather",font="charter 19 italic", fg="#164957", cursor='hand', padx=5, command=display_info)  # Button to Fetch the Data
get_weather_btn.config(highlightbackground="#2664ab", highlightthickness=3)
get_weather_btn.pack(padx=19,pady=11, side=TOP)

info_label = Label(main_frame, width=36, height=11, bg="#2a2b26", font="charter 18 italic", justify="left",anchor=NW, padx=14,pady=13, bd=3, relief=GROOVE)  # Label to Display the Data
info_label.place(rely=0.35, relx=0.14, relwidth=0.71, relheight=0.58)

# Side Images and Label

haze_img = PhotoImage(file="side_imgs/haze.png")
rainy_img = PhotoImage(fil="side_imgs/rainy.png")
sunny_img = PhotoImage(file="side_imgs/sunny.png")
cloudy_img = PhotoImage(file="side_imgs/cloudy.png")
thunderstorm_img = PhotoImage(file="side_imgs/thunderstorm.png")
mist_img = PhotoImage(file="side_imgs/mist.png")

side_img_label = Label(info_label, bg="#2a2b26", relief=GROOVE, bd=4)
# side_img_label.config(highlightthickness=1, highlightbackground='red')
side_img_label.pack(anchor=NE,side=RIGHT, padx=14,pady=12)

# print(font.families())
root.mainloop()
