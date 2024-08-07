# Radius of the arena scaled down to <0, 1> millimeters 
ARENA_RADIUS_SCALED = 0.5

# Radius of the arena in milimeters
ARENA_RADIUS_REAL = 19.417

# Scaling ratio
SCALING_RATIO = ARENA_RADIUS_SCALED / ARENA_RADIUS_REAL

# Number of flies being simulated
FLY_NUMBER = 12

# How many times fly positions are measured per second
SAMPLING_FREQUENCY = 24

#Simulation duration, measured in seconds
SIMULATION_DURATION = 1200
# SIMULATION_DURATION = 100

# Number of steps each fly makes
STEP_NUMBER = SAMPLING_FREQUENCY * SIMULATION_DURATION

# Minimum distance between two flies required to categorise it as an interaction measured in millimeters, normalized to [0, 1] 
INTERACTION_DISTANCE_THRESHOLD = 5 * SCALING_RATIO

# Plots the static fly movement if set to true 
PLOT_STATIC = False

# Saves the static fly movement in the designated directory if set to true 
EXPORT_STATIC = False

# Plots the animation if set to true 
PLOT_ANIMATION = False

# Saves the animation in the designated directory if set to true 
EXPORT_ANIMATION = False