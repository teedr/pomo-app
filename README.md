# Pomodoro Menu Bar App

A simple macOS menu bar application for the Pomodoro Technique, built with Python and rumps.

## Features
- Countdown timer in the menu bar
- Configurable timer duration
- Sound notification when timer completes
- Start, pause, and reset functionality

## Installation

### Development Setup
1. Clone this repository:
```bash
git clone https://github.com/yourusername/pomo-app.git
cd pomo-app
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running in Development
To run the application in development mode:
```bash
python src/pomodoro.py
```

### Building the Application
To build a standalone macOS application:

1. Make sure you're in the virtual environment:
```bash
source venv/bin/activate
```

2. Build the application using PyInstaller:
```bash
pyinstaller pomodoro.spec
```

3. The built application will be in the `dist` directory. You can copy it to your Applications folder:
```bash
cp -r dist/Pomodoro.app /Applications/
```

## Usage

After installation, you can:
1. Launch Pomodoro from your Applications folder
2. Click the tomato emoji (🍅) in your menu bar to:
   - Start/Stop the timer
   - Reset the timer
   - Configure custom duration
   - Quit the application

## Development

### Project Structure
```
pomo-app/
├── src/
│   ├── pomodoro.py      # Main application code
│   └── complete.mp3     # Sound file for timer completion
├── requirements.txt     # Python dependencies
├── pomodoro.spec       # PyInstaller specification
└── README.md           # This file
```

### Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
