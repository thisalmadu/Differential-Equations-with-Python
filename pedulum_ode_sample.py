import numpy as np

# Physical Constants
g = 9.8
L = 2
mu = 0.1

THETA_0 = np.pi/3 # 60 degrees
THETA_DOT_0 = 0 # NO initial angular velocity

# Definition of ODE
def get_theta_double_dot(theta, theta_dot):
    return -mu*theta_dot-(g/L)*np.sin(theta)

# Solution to the differential equation
def theta(t):
    #initializing changing values
    theta = THETA_0
    theta_dot = THETA_DOT_0
    delta_t = 0.01 # some time step
    for time in np.arange(0,t,delta_t):
        theta_double_dot = get_theta_double_dot(
            theta,theta_dot
        )
        theta += theta_dot*delta_t
        theta_dot += theta_double_dot*delta_t
    return theta

# Find the solution at time t=5
soln = theta(5)
print(soln)
