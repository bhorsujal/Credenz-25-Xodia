from stable_baselines3.common.env_util import make_vec_env
from environment.angry_birds_environment import AngryBirdsEnv

def train_model():

    env = make_vec_env(AngryBirdsEnv)


    # YOUR TRAINING LOGIC GOES HERE.

    # SAVE THE MODEL. SHARE IT LATER WITH US BEFORE GIVEN DEADLINE.


if __name__ == "__main__":
    train_model()