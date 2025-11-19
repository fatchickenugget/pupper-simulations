from bittle_env import BittleEnv

from brax import envs

envs.register_environment('bittle', BittleEnv)

env_name = 'bittle'
xml_path = 'bittle_adapted_scene.xml'

env = envs.get_environment(env_name, xml_path = xml_path)