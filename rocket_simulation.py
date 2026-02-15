import numpy
import matplotlib.pyplot as plt


def simulation_rocket(mass, thrust, burn_time, drag_coeff, gravity, dt, max_time):

    time = 0
    height = 0
    velocity = 0
    max_height = 0
    time_of_max = 0
    time_history = []
    height_history = []
    velocity_history = []
    acceleration_history = []

    while height >= 0 and time <= max_time:
        if time < burn_time:
            current_thrust = thrust
        else: current_thrust = 0

        drag = -1 * velocity * abs(velocity) * drag_coeff

        f_net = current_thrust + drag + (gravity * mass)

        acceleration = f_net / mass

        height_history.append(height)
        velocity_history.append(velocity)
        acceleration_history.append(acceleration)
        time_history.append(time)

        velocity = velocity + (acceleration * dt)

        height = height + (velocity * dt)

        time += dt
        #print(time, height, velocity, acceleration, thrust)
        


    plt.figure()

    plt.subplot(3,1,1)
    plt.plot(time_history, height_history)
    plt.ylabel("Height (m)")

    plt.subplot(3,1,2)
    plt.plot(time_history, velocity_history)
    plt.ylabel("Velocity (m/s)")

    plt.subplot(3,1,3)
    plt.plot(time_history, acceleration_history)
    plt.ylabel("Acceleration (m/s^2)")
    plt.xlabel("Time (s)")

    plt.tight_layout()
    plt.show()
    

if __name__ == "__main__":

    mass = 1000
    thrust = 20000
    burn_time = 5
    drag_coeff = 0.5
    dt = 0.1
    max_time = 100
    gravity = -9.81
    
    results = simulation_rocket(mass, thrust, burn_time, drag_coeff, gravity, dt, max_time)
    