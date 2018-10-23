# AntHive.IO sample bot in *Python*

## Requirements
- Clone https://github.com/anthive/python.git
- Push to your Github account.
- Do not push your code to sample bot repo.
- Signup at https://profile.anthive.io/
- Set your username in [ANTHIVE](ANTHIVE) file

### Python 2
- In [ANTHIVE](ANTHIVE) file set **lang** to **python2**

### Python 3
- In [ANTHIVE](ANTHIVE) file set **lang** to **python3**

## Run locally 
```
python run.py
```
or
```
python3 run.py
```

It will start localhost server on port :7070 **Do not change port**


## Test with sample call
```
curl -X 'POST' -d @payload.json http://localhost:7070
```

## Debug and Sandbox
- git push
- Go to [Profile](https://profile.anthive.io/)
- Queue the game

## Coming Soon: *Ranked games and ML*
- Go to [Profile](https://profile.anthive.io/)
- Enable Career
- [Leaderboard](https://anthive.io/liaderboard)
