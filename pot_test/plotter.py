#!/usr/bin/env python3

import serial
import sys
import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
from time import time

plt.rcParams['toolbar'] = 'None'

class Plotter:
    def __init__(self, ax):
        self.ax = ax
        self.maxt = 10000
        self.tdata = [0]
        self.ydata = {
            0: [4096 / 2],
            1: [4096 / 2],
            2: [4096 / 2]
            # 0: [3.3 / 2],
            # 1: [3.3 / 2],
            # 2: [3.3 / 2],
        }
        self.lines = {
            0: Line2D(self.tdata, self.ydata[0], color='C0', label='ADC0'),
            1: Line2D(self.tdata, self.ydata[1], color='C1', label='ADC1'),
            2: Line2D(self.tdata, self.ydata[2], color='C2', label='ADC2'),
        }

        for line in self.lines.values():
            self.ax.add_line(line)

        self.ax.set_ylim(0, 4096)
        # self.ax.set_ylim(0, 3.3)
        self.ax.set_xlim(0, self.maxt)
        self.ax.legend(loc='upper right')

    def update(self, adc_vals):
        timestamp = int((time() - start_time) * 1000)  # ms since start
        csv_writer.writerow([
            timestamp, adc_vals[0], adc_vals[1], adc_vals[2]
        ])

        lastt = self.tdata[-1]
        if lastt - self.tdata[0] >= self.maxt:
            self.tdata = self.tdata[1:]
            for ch in self.ydata:
                self.ydata[ch] = self.ydata[ch][1:]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)

        t = lastt + 1
        self.tdata.append(t)
        for ch in adc_vals:
            self.ydata[ch].append(adc_vals[ch])
            self.lines[ch].set_data(self.tdata, self.ydata[ch])

        return tuple(self.lines.values())

def serial_getter():
    buffer = {}
    while True:
        line = ser.readline().decode(errors='ignore').strip()
        if line.startswith("ADC"):
            try:
                parts = line.split(":")
                chan = int(parts[0][3])
                val = int(parts[1].strip())
                buffer[chan] = val
            except Exception:
                continue

            if all(k in buffer for k in [0, 1, 2]):
                yield {0: buffer[0], 1: buffer[1], 2: buffer[2]}
                buffer.clear()

# --- Setup ---
if len(sys.argv) < 2:
    raise Exception("Usage: python3 plotter.py <serial_port>")

ser = serial.Serial(sys.argv[1], 115200, timeout=1)

# Create CSV file with timestamped filename
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
csv_filename = f"adc_log_{now}.csv"
csv_file = open(csv_filename, "w", newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["timestamp_ms", "ADC0", "ADC1", "ADC2"])

start_time = time()

fig, ax = plt.subplots()
plotter = Plotter(ax)

ani = animation.FuncAnimation(
    fig, plotter.update, serial_getter, interval=1,
    blit=True, cache_frame_data=False
)

ax.set_xlabel("Samples")
ax.set_ylabel("ADC Value")
fig.canvas.manager.set_window_title('3-Channel ADC Plotter')
fig.tight_layout()

try:
    plt.show()
finally:
    csv_file.close()
    print(f"Saved data to {csv_filename}")