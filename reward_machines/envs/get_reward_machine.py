import importlib.resources

def get_reward_machine(path: str):
    if hasattr(importlib.resources, "files"):
        return importlib.resources.files("reward_machines.envs").joinpath(path)
    else:
        result = None

        with importlib.resources.path("reward_machines.envs", "") as f:
            result = f

        return result.joinpath(path)
