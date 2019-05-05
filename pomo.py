# pomodorro timer for my CLI cuz why the fuck not right?
import argparse
import platform
from tqdm import tqdm
import time
import json
import os

def silent(configs):
    timestamp = int(time.strftime('%H:%M:%S')[:2])
    if "silent_duration" in configs:
        assert("hours" in configs['silent_duration']), "Invalid format. Silent hours not found"
        for l, u in configs["silent_duration"]["hours"]:
            if l <= timestamp <= u:
                return True
    return False

parser = argparse.ArgumentParser()
parser.add_argument("--time", "-t", 
                        help="Set the time duration for Pomodoro timer in minutes (default is 25 mins)", 
                        default=25)
parser.add_argument("--config", "-c", 
                        help="Set configurations on how the beep should play out")
args = parser.parse_args()
CONFIGS = None
if args.config:
    assert(os.path.exists(args.config))
    CONFIGS = json.load(open(args.config, 'r'))

for i in tqdm(range(int(args.time))):
    time.sleep(60)

if CONFIGS and not silent(CONFIGS):
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 300)
        winsound.Beep(1000, 300)
    elif platform.system() == "Linux":
        import os
        duration = 1  # seconds
        freq = 300  # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
elif CONFIGS and silent(CONFIGS):
    print("silent hours")

print("-----------------------Timer Ended!-----------------------")



