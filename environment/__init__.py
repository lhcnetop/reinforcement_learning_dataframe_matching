from gymnasium.envs.registration import register

register(
     id="Environment/ConcilEnv-v0",
     entry_point="Environment:ConcilEnv",
     max_episode_steps=20,
)
