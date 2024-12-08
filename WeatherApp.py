from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from PIL import Image, ImageTk
from tkinter import messagebox, PhotoImage
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import os

root = Tk()
root.title("Weather App by ANormalGuy")
root.geometry("900x500+300+200")
root.resizable(False, False)

api_key = os.getenv("YOUR_API_KEY")


# Replace YOUR_API_KEY with your actual API key, as mine is like: e00daf*********************c03b9

# Fetch + display weather data
def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="WeatherApp_by_ANormalGuy")
    location = geolocator.geocode(city)

    if location:
        # Fetch+display the country
        country = location.address.split(",")[-1].strip()
        city_country_label.config(text=f"{city.title()} is a city in {country}")

        # Timezone and local time info
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        time.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Fetch weather data from API
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description'].title()  # Capitalize first letter of each word
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update labels with the weather data
        t.config(text=f"{temp}°")
        c.config(text=f"{condition}")
        w.config(text=wind)
        h.config(text=humidity)
        p.config(text=pressure)
        d.config(text=description)
    else:
        messagebox.showerror("Error", "City not found!")


# Bind the Enter key to the getWeather function
def on_enter(event):
    getWeather()


# Configure the search box

pil_image = Image.open("search_icon.png")
myimage = Label(image=ImageTk.PhotoImage(pil_image))
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("Microsoft PhagsPa", 25, "bold"), bg="#404040", border=0,
                     fg="white")
textfield.place(x=50, y=40)
textfield.focus()

# Bind the Enter key to trigger getWeather
textfield.bind("<Return>", on_enter)

# Configure the search button
search_icon = ImageTk.PhotoImage(Image.open("search_icon.png").resize((43, 43), Image.LANCZOS))
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=355, y=40)

# Label for displaying city and country information
city_country_label = Label(root, font=("Microsoft PhagsPa", 12), fg="black")
city_country_label.place(x=420, y=50)

# Additional GUI configurations (logo, labels, etc.)
logo_img = Image.open("weather_app_icon.png").resize((150, 150), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
logo = Label(image=logo_photo)
logo.place(x=150, y=150)

frame = PhotoImage(file="blue_box.png")
frame_myimg = Label(image=frame)
frame_myimg.pack(padx=5, pady=5, side=BOTTOM)

name = Label(root, font=("Microsoft PhagsPa", 15, "bold"))
name.place(x=30, y=100)
time = Label(root, font=("Microsoft PhagsPa", 20))
time.place(x=30, y=130)

# Labels for displaying data
label1 = Label(root, text="WIND", font=("Microsoft PhagsPa", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=140, y=400)

label2 = Label(root, text="HUMIDITY", font=("Microsoft PhagsPa", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=270, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Microsoft PhagsPa", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=450, y=400)

label4 = Label(root, text="PRESSURE", font=("Microsoft PhagsPa", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("Microsoft PhagsPa", 70, "bold"), fg="#ee666d")
t.place(x=400, y=140)

c = Label(font=("Microsoft PhagsPa", 20, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("Microsoft PhagsPa", 20, "bold"), bg="#1ab5ef")
w.place(x=150, y=430)

h = Label(text="...", font=("Microsoft PhagsPa", 20, "bold"), bg="#1ab5ef")
h.place(x=300, y=430)

d = Label(text="...", font=("Microsoft PhagsPa", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text="...", font=("Microsoft PhagsPa", 20, "bold"), bg="#1ab5ef")
p.place(x=690, y=430)

# Run the main loop
root.mainloop()
