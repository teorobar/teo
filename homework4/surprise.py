# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
	"Canopus": {
        "RA": "06h 23m 36.5s",
        "Dec": "-52° 41′ 45″",
        "Magnitude": -0.74,
        "Spectral Type": "F0lb"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
for star in targets:
	print(star)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.	
for star in targets:
	x = targets[star]
	print(f"{star} = {x["Spectral Type"]}")
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
for star in targets:
	x = targets[star]
	if x["Magnitude"] > 0.1:
	    print(f"{star}")
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# I'm not exactly sure what you want me to do here... for example, Sirius is the brighter
# star but Betelgeuse is closer to 20 degrees and I'm not sure which the algorith you want
# me to write would prefer.
# 6) What is your favorite constellation?
# Cassiopeia because I like the name :)
