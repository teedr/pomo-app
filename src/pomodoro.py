#!/usr/bin/env python3

import rumps
import os


class PomodoroApp(rumps.App):
    def __init__(self):
        super(PomodoroApp, self).__init__("🍅")
        
        self.timer = rumps.Timer(self.on_tick, 1)
        self.interval = 25 * 60  # 25 minutes in seconds
        self.remaining_time = self.interval
        self.is_running = False
        
        # Menu items
        self.button_start = rumps.MenuItem("Start Timer")
        self.button_reset = rumps.MenuItem("Reset")
        self.button_custom = rumps.MenuItem("Set Custom Duration")
        
        # Add menu items
        self.menu = [
            self.button_start,
            self.button_reset,
            self.button_custom,
            None,  # Separator
        ]

    @rumps.clicked("Start Timer")
    def start_timer(self, _):
        if not self.is_running:
            self.is_running = True
            self.timer.start()
            self.button_start.title = "Stop Timer"
        else:
            self.is_running = False
            self.timer.stop()
            self.button_start.title = "Start Timer"

    @rumps.clicked("Reset")
    def reset_timer(self, _):
        self.is_running = False
        self.remaining_time = self.interval
        self.timer.stop()
        self.button_start.title = "Start Timer"
        self.title = "🍅"

    @rumps.clicked("Set Custom Duration")
    def custom_duration(self, _):
        window = rumps.Window(
            message="Enter duration in minutes:",
            title="Custom Duration",
            default_text="25",
            dimensions=(100, 20)
        )
        response = window.run()
        
        try:
            new_interval = int(response.text)
            if new_interval > 0:
                self.interval = new_interval * 60
                self.remaining_time = self.interval
                self.title = "🍅"
        except ValueError:
            rumps.alert("Please enter a valid number!")

    def on_tick(self, _):
        if self.is_running and self.remaining_time > 0:
            self.remaining_time -= 1
            mins, secs = divmod(self.remaining_time, 60)
            self.title = f"{mins:02d}:{secs:02d}"
        
        if self.is_running and self.remaining_time <= 0:
            self.timer.stop()
            self.is_running = False
            self.remaining_time = self.interval
            self.button_start.title = "Start Timer"
            self.title = "🍅"
            
            # Play sound when timer completes
            sound_path = os.path.dirname(__file__)
            sound_file = os.path.join(sound_path, "complete.mp3")
            try:
                os.system(f"afplay {sound_file}")
            except Exception:  # Handle any exception with sound
                # Fallback to system bell if sound file is not found
                print("\a")
            
            # Show notification
            rumps.notification(
                title="Pomodoro Timer",
                subtitle="Time's Up!",
                message="Take a break!"
            )

if __name__ == "__main__":
    PomodoroApp().run()
