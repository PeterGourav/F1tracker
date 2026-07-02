import fastf1
import pandas as pd
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache('data/raw')

session = fastf1.get_session(2023, 'Bahrain', 'R')
session.load()

print("Session loaded!")
print(f"Event: {session.event['EventName']}")
print(f"Date: {session.event['EventDate']}")

laps = session.laps

ver_laps = laps.pick_drivers('VER')
print(ver_laps[['LapNumber', 'LapTime', 'Compound', 'TyreLife', 'Stint', 'PitInTime', 'PitOutTime']].head(20))


ver_laps = ver_laps.copy()
ver_laps['LapTimeSeconds'] = ver_laps['LapTime'].dt.total_seconds()


clean = ver_laps[
    ver_laps['PitInTime'].isna() &
    ver_laps['PitOutTime'].isna() &
    (ver_laps['LapTimeSeconds'] < 120)  # removes safety car laps etc.
]

plt.figure(figsize=(12, 5))
plt.plot(clean['LapNumber'], clean['LapTimeSeconds'], marker='o')
plt.xlabel('Lap Number')
plt.ylabel('Lap Time (seconds)')
plt.title('Verstappen Lap Times - 2023 Bahrain GP')
plt.grid(True)
plt.tight_layout()
plt.show()