import os
import sys
import math
import random
import tkinter as tk

class RealTimeMatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📡 REAL-TIME SYSTEM TELEMETRY STATE MATRIX")
        
        # Grid layout limits (Keep dimensions reasonable for fast refresh pacing)
        self.columns = 32
        self.rows = 32
        self.cell_size = 15
        
        # Setup application canvas structure
        canvas_w = self.columns * self.cell_size
        canvas_h = self.rows * self.cell_size
        self.canvas = tk.Canvas(root, width=canvas_w, height=canvas_h, bg="black")
        self.canvas.pack()
        
        # Initialize internal state timers
        self.time_step = 0
        
        # Pre-build canvas pixel rectangles to save system resource overhead during execution
        self.rectangles = []
        for y in range(self.rows):
            row_rects = []
            for x in range(self.columns):
                x1 = x * self.cell_size
                y1 = y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="")
                row_rects.append(rect)
            self.rectangles.append(row_rects)
            
        print("[+] Telemetry render loop initialized successfully.")
        # Launch the live execution update thread
        self.update_stream()

    def capture_live_metrics(self):
        """Simulates gathering volatile multi-layered OS kernel allocation changes."""
        # Check active environment profiles to simulate baseline entropy shifts
        env_modifier = len(str(os.environ)) % 100
        return env_modifier

    def update_stream(self):
        self.time_step += 1
        base_modifier = self.capture_live_metrics()
        
        # Step through every cell coordinate on the canvas matrix
        for y in range(self.rows):
            for x in range(self.columns):
                # Calculate trigonometric algorithms to simulate data streams colliding
                wave_a = math.sin(x * 0.2 + self.time_step * 0.1) * math.cos(y * 0.2 + self.time_step * 0.05)
                wave_b = math.sin((x + y) * 0.1 - self.time_step * 0.08)
                
                # Convert the signal waves into raw 0-255 binary parameters
                val_1 = int((wave_a + 1) * 127.5)
                val_2 = int((wave_b + 1) * 127.5)
                val_3 = (base_modifier * (x + y + self.time_step)) % 256
                
                # --- AUTOMATED PATTERN COLOR FILTER ---
                if val_1 > 170:  # High spikes (Simulating active processes) -> Red dominance
                    r, g, b = val_1, int(val_2 * 0.4), int(val_3 * 0.2)
                elif val_2 > 110 and val_2 < 190:  # Wave transfers (Simulating RAM buffers) -> Green dominance
                    r, g, b = int(val_1 * 0.2), val_2, int(val_3 * 0.5)
                else:  # Static regions (Simulating idle storage fields) -> Blue dominance
                    r, g, b = int(val_1 * 0.1), int(val_2 * 0.3), val_3
                    
                # Format channels into a hex string color tag
                color_hex = f"#{r:02x}{g:02x}{b:02x}"
                
                # Update the target rectangle block item directly
                self.canvas.itemconfig(self.rectangles[y][x], fill=color_hex)
                
        # Trigger the next calculation step after 50 milliseconds (Fast real-time frame rates)
        self.root.after(50, self.update_stream)

if __name__ == "__main__":
    main_window = tk.Tk()
    app = RealTimeMatrixApp(main_window)
    main_window.mainloop()
