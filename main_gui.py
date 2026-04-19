import customtkinter as ctk
from tkinter import messagebox

from weather_service import WeatherService
from adapter import WeatherAdapter


class WeatherAppGUI:
    def __init__(self, root, service):
        self.root = root
        self.service = service

        self.root.title("Weather Dashboard v1.1")
        self.root.geometry("500x650")
        ctk.set_appearance_mode("dark")  # Темная тема
        ctk.set_default_color_theme("blue")

        self.label = ctk.CTkLabel(self.root, text="ПОГОДНЫЙ ДАШБОРД", font=("Roboto", 24, "bold"))
        self.label.pack(pady=20)

        self.search_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.search_frame.pack(pady=10)

        self.entry = ctk.CTkEntry(self.search_frame, placeholder_text="Введите город...", width=250, height=40)
        self.entry.pack(side="left", padx=10)

        self.button = ctk.CTkButton(self.search_frame, text="Поиск", width=100, height=40,
                                    command=self.load_weather, font=("Roboto", 14, "bold"))
        self.button.pack(side="left")

        self.results_frame = ctk.CTkScrollableFrame(self.root, width=450, height=420, label_text="Прогноз на 5 дней")
        self.results_frame.pack(pady=20, padx=20)

    def load_weather(self):
        city = self.entry.get()
        data = self.service.get_data(city)

        if not data:
            messagebox.showerror("Ошибка", f"Город '{city}' не найден!")
            return

        forecast = WeatherAdapter.parse_forecast(data)

        for widget in self.results_frame.winfo_children():
            widget.destroy()

        for day in forecast:
            card = ctk.CTkFrame(self.results_frame)
            card.pack(fill="x", pady=5, padx=5)

            info_text = (f"📅 {day.date}  |  🌡️ {day.temp}°C  |  {day.desc}\n"
                         f"💧 Влажность: {day.humidity}%  |  💨 Ветер: {day.wind_speed} м/с")

            lbl = ctk.CTkLabel(card, text=info_text, justify="left", font=("Roboto", 13))
            lbl.pack(pady=10, padx=15)

if __name__ == "__main__":
    root = ctk.CTk()

    api_key = "ВАШ_API_КЛЮЧ"
    service = WeatherService(api_key)
    app = WeatherAppGUI(root, service)
    root.mainloop()

