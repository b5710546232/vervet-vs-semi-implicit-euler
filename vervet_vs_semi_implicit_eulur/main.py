import numpy as np
import matplotlib.pyplot as plt

def verlet_integration(x0, v0, dt, num_steps):
    x = [x0]
    v = [v0]

    for i in range(1, num_steps):
        x.append(x[i-1] + v[i-1]*dt + 0.5*gravity*dt**2)
        v.append(v[i-1] + gravity*dt)

    return x, v

def semi_implicit_euler_integration(x0, v0, dt, num_steps):
    x = [x0]
    v = [v0]

    for i in range(1, num_steps):
        v.append(v[i-1] + gravity*dt)
        x.append(x[i-1] + v[i]*dt)

    return x, v

# Simulation parameters
initial_position = 0
initial_velocity = 0
gravity = 1000
time_step = 1
simulation_time = 100

# Calculate the number of steps
num_steps = int(simulation_time / time_step)

# Calculate the actual position
t = np.arange(num_steps) * time_step
x_actual = initial_position + initial_velocity * t + 0.5 * gravity * t**2

# Perform Verlet integration
x_verlet, _ = verlet_integration(initial_position, initial_velocity, time_step, num_steps)

# Perform semi-implicit Euler integration
x_euler, _ = semi_implicit_euler_integration(initial_position, initial_velocity, time_step, num_steps)

# Calculate RMSE
rmse_verlet = np.sqrt(np.mean((x_actual - x_verlet)**2))
rmse_euler = np.sqrt(np.mean((x_actual - x_euler)**2))

# Plot the results
plt.figure(figsize=(10, 6))
# // color with alpha rgba
plt.plot(t, x_actual, label='Actual Position')
plt.plot(t, x_verlet, label='Verlet Integration (RMSE: {:.4f})'.format(rmse_verlet))
plt.plot(t, x_euler, label='Semi-Implicit Euler Integration (RMSE: {:.4f})'.format(rmse_euler))
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Comparison of Verlet and Semi-Implicit Euler Integration')
plt.legend()
plt.grid(True)
plt.show()

#  root mean square error (RMSE) between the actual position and the simulated positions for both the Verlet integration and semi-implicit Euler integration methods. The RMSE is then displayed as part of the legend in the chart.
#  By comparing the RMSE values, you can get a quantitative measure of the error for each integration method. A higher RMSE value indicates a larger deviation from the actual position, indicating a higher error in the simulation.