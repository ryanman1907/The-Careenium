import math


### DOES COMPUTATIONS, DO NOT ALTER SIMMS ###

def get_distance(s1, s2):
    # get the distance between 2 simms/simmballs
    x_dist = s1.x - s2.x
    y_dist = s1.y - s2.y
    d = math.sqrt(x_dist ** 2 + y_dist ** 2)

    return d


def get_force(s1, s2):
    # inversely proportional to product of masses and inversely proportional to distance between them
    p_o_m = s1.mass * s2.mass
    S = 0.069 # simmball constant
    dist = get_distance(s1, s2)

    f = S * p_o_m / (dist ** 2)
    return f


def get_mass(s):
    return s.mass


def get_momentum(s):
    p_x = s.mass * s.v_x
    p_y = s.mass * s.v_y
    return p_x, p_y


def get_kinetic_energy(s):
    speed = math.sqrt(s.v_x ** 2 + s.v_y ** 2)
    K = 0.5 * s.mass * speed ** 2
    return K


def calc_1d_elastic_collision(v1, v2, m1, m2):
    # using the amazing relative velocity approach taught to me by none other than RGB, esteemed Duke university professor of physics
    v_cm = (m1 * v1 + m2 * v2) / (m1 + m2)

    v1_f = -v1 + 2 * v_cm
    v2_f = -v2 + 2 * v_cm

    return v1_f, v2_f

### ACTUALLY CHANGE VALUES ###

def calc_2d_collision(s1, s2):
    # change the velocities of the colliding balls
    v_x1f, v_x2f = calc_1d_elastic_collision(s1.v_x, s2.v_x, s1.mass, s2.mass)
    v_y1f, v_y2f = calc_1d_elastic_collision(s1.v_y, s2.v_y, s1.mass, s2.mass)

    s1.v_x = v_x1f
    s1.v_y = v_y1f

    s2.v_x = v_x2f
    s2.v_y = v_y2f
    
### SOME THINKODYNAMICS ###

def get_total_energy(simms):
    K = 0
    for simm in simms:
        K += get_kinetic_energy(simm)
    return K