# Radius of the arena scaled down to <0, 1> millimeters 
ARENA_RADIUS_SCALED = 0.5

# Radius of the arena in milimeters
ARENA_RADIUS_REAL = 19.417

# Scaling ratio
SCALING_RATIO = ARENA_RADIUS_SCALED / ARENA_RADIUS_REAL

# Number of flies being simulated
FLY_NUMBER = 5

# How many times fly positions are measured per second
SAMPLING_FREQUENCY = 24

#Simulation duration, measured in seconds
SIMULATION_DURATION = 1200

# Number of steps each fly makes
STEP_NUMBER = SAMPLING_FREQUENCY * SIMULATION_DURATION

# Size of each step
# STEP_SIZE = 0.1

# Minimum distance between two flies required to categorise it as an interaction measured in millimeters, normalized to [0, 1] 
INTERACTION_DISTANCE_THRESHHOLD = 5 * SCALING_RATIO

# Whether or not the application should show plots
SHOULD_PLOT = False

# Exports the animation if set to true 
SHOULD_ANIMATE = False