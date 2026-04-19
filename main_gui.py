import tkinter as tk
from tkinter import messagebox
from weather_service import WeatherService
from adapter import WeatherAdapter

class WeatherAppGUI:
    def __init__(self, root):
        self.service = WeatherService("API key")
        self.root = root
        self.root.title("Weather Dashboard v1.0")
        self.root.geometry("450x550")

        # UI Элементы
        tk.Label(root, text="Введите город:", font=("Arial", 12)).pack(pady=10)
        self.entry = tk.Entry(root, font=("Arial", 12), width=20)
        self.entry.pack()

        tk.Button(root, text="Поиск", command=self.load_weather, bg="#4CAF50", fg="white").pack(pady=10)

        self.text_area = tk.Text(root, font=("Consolas", 10), height=18, width=55)
        self.text_area.pack(pady=10, padx=10)

    def load_weather(self):
        city = self.entry.get()
        data = self.service.get_data(city)

        if not data:
            messagebox.showerror("Ошибка", f"Город '{city}' не найден!")
            return

        forecast = WeatherAdapter.parse_forecast(data)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"{'Дата':<12} | {'Темп':<5} | {'Ветер':<7} | {'Описание'}\n")
        self.text_area.insert(tk.END, "-" * 55 + "\n")

        for day in forecast:
            row = f"{day.date:<12} | {day.temp:>3}°C | {day.wind_speed:>3} м/с | {day.desc}\n"
            self.text_area.insert(tk.END, row)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()
