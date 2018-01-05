import numpy as np
import lqg1d
import matplotlib.pyplot as plt
import utils


class ConstantStep(object):
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def update(self, gt):
        return self.learning_rate * gt


#####################################################
# Define the environment and the policy
#####################################################
env = lqg1d.LQG1D(initial_state_type='random')


class Policy:
    def __init__(self, sigma, theta):
        self.theta = theta
        self.sigma = sigma

    def draw_action(self, s):
        return np.random.normal(self.theta * s, self.sigma)


policy = Policy(0.5, 1)
#####################################################
# Experiments parameters
#####################################################
# We will collect N trajectories per iteration
N = 100
# Each trajectory will have at most T time steps
T = 100
# Number of policy parameters updates
n_itr = 100
# Set the discount factor for the problem
discount = 0.9
# Learning rate for the gradient update
learning_rate = 0.1

#####################################################
# define the update rule (stepper)
stepper = ConstantStep(learning_rate)

# fill the following part of the code with
#  - REINFORCE estimate i.e. gradient estimate
#  - update of policy parameters using the steppers
#  - average performance per iteration
#  - distance between optimal mean parameter and the one at it k
mean_parameters = []
avg_return = []
for i in range(n_itr):
    print(i)
    paths = utils.collect_episodes(env, policy=policy, horizon=T, n_episodes=N)

    gradJ_MC = 0
    reward_MC = 0
    for n in range(N):
        gradJ = 0
        reward = 0
        gradJ_log = 0
        for t in range(T):
            gradJ_log += ((paths[n]['actions'][t] - policy.theta * paths[n]['states'][t]) / policy.sigma ** 2) * \
                         paths[n]['states'][t]
            reward += paths[n]['rewards'][t] * (discount ** i)
        gradJ += gradJ_log * reward
        gradJ_MC += gradJ
        reward_MC += reward

    gradJ_MC = gradJ_MC / N
    reward_MC = reward_MC / N

    policy.theta += stepper.update(gradJ_MC)

    mean_parameters.append(policy.theta)
    avg_return.append(reward_MC)

# plot the average return obtained by simulating the policy
# at each iteration of the algorithm (this is a rought estimate
# of the performance
plt.figure()
plt.plot(avg_return)
plt.show()
# plot the distance mean parameter
# of iteration k
plt.figure()
plt.plot(mean_parameters)
plt.show()



