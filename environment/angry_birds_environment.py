import numpy as np
import gym
from gym import spaces
import pygame
from models.pig import Pig
from models.bird import Bird


# Constants
WIDTH, HEIGHT = 800, 450
FPS = 60
SLINGSHOT_POS = (100, 270)


class AngryBirdsEnv(gym.Env):
    def __init__(self):
        super().__init__()

        self.bird = Bird(*SLINGSHOT_POS)
        self.pig = Pig(600, 320)

        self.observation_space = spaces.Box(
            low=np.array([0, 0, -30, -30, 0, 0, 0, 0, 0, -np.pi], dtype=np.float32),
            high=np.array([WIDTH, HEIGHT, 30, 30, WIDTH, HEIGHT, WIDTH, HEIGHT, HEIGHT, np.pi], dtype=np.float32),
            dtype=np.float32
        )

        self.action_space = spaces.Box(
            low=np.array([1, 1], dtype=np.float32),
            high=np.array([15, 15], dtype=np.float32),
            dtype=np.float32
        )

        self.clock = pygame.time.Clock()
        self.current_step = 0
        self.max_steps = 200
        self.min_distance = float('inf')
        self.trajectory_variety = []

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_step = 0
        self.bird.reset()
        self.pig.reset()
        self.trajectory_variety = []

        dx = self.pig.x - self.bird.x
        dy = self.pig.y - self.bird.y
        self.min_distance = np.sqrt(dx * dx + dy * dy)

        return self._get_obs(), {}

    def _get_obs(self):
        dx = self.pig.x - self.bird.x
        dy = self.pig.y - self.bird.y

        return np.array([
            self.bird.x,
            self.bird.y,
            self.bird.velocity[0],
            self.bird.velocity[1],
            self.pig.x,
            self.pig.y,
            dx,
            dy,
            self.bird.max_height,
            self.bird.launch_angle
        ], dtype=np.float32)

    def get_reward_and_status(self):
        reward = 0
        done = False

        # YOUR REWARD LOGIC GOES HERE

        return reward, done

    def step(self, action):
        self.current_step += 1
        prev_distance = np.sqrt((self.pig.x - self.bird.x) ** 2 + (self.pig.y - self.bird.y) ** 2)

        if not self.bird.launched:
            power_x, power_y = action
            self.bird.launch(power_x, power_y)

        self.bird.update()

        dx = self.pig.x - self.bird.x
        dy = self.pig.y - self.bird.y
        current_distance = np.sqrt(dx * dx + dy * dy)
        self.min_distance = min(self.min_distance, current_distance)

        # Fetch reward and done flag from the method

        reward, done = self.get_reward_and_status()

        return self._get_obs(), reward, done, False, {}
