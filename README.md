Simple Python Keylogger

This repository contains a simple Python script developed to register keystrokes for educational purposes.

 Activity Objective

The primary goal of this activity is to implement a basic keylogger within a controlled environment to understand its mechanics, internal operations, and potential impact in insecure settings.

STRICT ETHICAL WARNING: This practice is purely educational and must not be used for unethical, illegal, or unauthorized activities. The author assumes no responsibility for misuse.

 Deliverables

The repository is structured to include the following core files, meeting the activity requirements:

File

Description

main.py

The main keylogger script, responsible for hooking keyboard events and logging data.

requirements.txt

Defines the necessary external Python dependencies (keyboard).

README.md

This documentation file, including setup instructions and execution examples.

pulsaciones.txt

The log file generated at runtime, storing all recorded keystrokes.

 Setup and Usage

Follow these steps to set up and run the keylogger (assuming Python 3 is installed on your system).

1. Requirements Installation

The script requires the external Python library keyboard. Install all dependencies listed in requirements.txt using pip:

pip install -r requirements.txt


2. Execution

Navigate to the project directory and execute the main script from your terminal:

python main.py


Upon execution, the system will display a confirmation message and the absolute path of the log file. The application will immediately begin monitoring keystrokes.

3. Termination

To safely stop the keylogger, simply press the Esc key.

 Execution Examples

Below are examples illustrating the console output upon launch and the format of the data recorded in the log file.

Console Output Example

The console provides real-time feedback on the keys being logged:

==================================================
   INICIADOR DE REGISTRO DE PULSACIONES (Keylogger)
==================================================
>>> ADVERTENCIA: Usar solo con fines de prueba y educativos.
 
[INFO] El registro comenzará ahora.
[INFO] Archivo de destino: /path/to/project/pulsaciones.txt
[INFO] Pulsa la tecla 'ESC' para finalizar el programa.
Log: [2025-10-16 12:35:01] Tecla: 'h'
Log: [2025-10-16 12:35:01] Tecla: 'o'
Log: [2025-10-16 12:35:02] [SPACE]
Log: [2025-10-16 12:35:03] [ENTER]
...


pulsaciones.txt Log Format

The pulsaciones.txt file records the timestamp and the key pressed. Special keys are enclosed in square brackets [] and logged in uppercase for easy parsing.

[2025-10-16 12:35:01] Tecla: 'h'
[2025-10-16 12:35:01] Tecla: 'o'
[2025-10-16 12:35:02] Tecla: 'l'
[2025-10-16 12:35:02] Tecla: 'a'
[2025-10-16 12:35:02] [SPACE]
[2025-10-16 12:35:03] [SHIFT]
[2025-10-16 12:35:03] Tecla: 'm'
[2025-10-16 12:35:03] Tecla: 'u'
[2025-10-16 12:35:03] [ENTER]
