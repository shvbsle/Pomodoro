# Pomodoro
Custom Pomodoro Command Line timer to track my work hours. Other online softwares are too bloated. This is my simple hack.

## Requirements
- Python3
  - tqdm

## Usage

>python3 -t <minutes for timer> -c path to config file

### Config File Structure
A json file with "silent_hours" field that will include time periods between which I dont want the beep to go off.

eg:

```   
{"silent_hours":
    "desc":"list pair of time windows between which you want the timer to be silent. 24 hour format followed",
    "hours": [[1,5], [21, 22]]
    }
```

### To do:
- [x] add silent hours
- [ ] add logs for times when timer was on
