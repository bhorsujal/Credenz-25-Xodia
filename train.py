from stable_baselines3.common.env_util import make_vec_env
from environment.angry_birds_environment import AngryBirdsEnv
from stable_baselines3 import PPO

def train_model():

    env = make_vec_env(AngryBirdsEnv)


    # YOUR TRAINING LOGIC GOES HERE.
    policy_kwargs = dict(net_arch=[256, 256])

    model = PPO(
        policy="MlpPolicy",
        env=env,
        verbose=1,
        n_steps=2048,
        batch_size=256,
        gae_lambda=0.95,
        gamma=0.99,
        ent_coef=0.01,
        learning_rate=3e-4,
        clip_range=0.2,
        policy_kwargs=policy_kwargs,
        tensorboard_log="./tensorboard_logs"
    )

    total_timesteps = 2_000_000
    model.learn(total_timesteps=total_timesteps)

    # SAVE THE MODEL. SHARE IT LATER WITH US BEFORE GIVEN DEADLINE.
    model.save("angry_birds_ppo_model_2")


if __name__ == "__main__":
    train_model()