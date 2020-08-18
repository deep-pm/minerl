# Copyright (c) 2020 All Rights Reserved
# Author: William H. Guss, Brandon Houghton

import collections

import gym

from minerl.herobraine.env_spec import EnvSpec
from minerl.herobraine.env_specs.treechop_specs import Treechop, TreechopMultiAgent
from minerl.herobraine.env_specs.navigate_specs import Navigate
from minerl.herobraine.env_specs.obtain_specs import ObtainDiamond, ObtainDiamondSurvival, ObtainIronPickaxe, Obtain, ObtainDiamondDebug
from minerl.herobraine.wrappers import Obfuscated, Vectorized
import minerl.data.version
import os


# Must load non-obfuscated envs first!
# Publish.py depends on this order for black-listing streams
MINERL_TREECHOP_V0 = Treechop()
MINERL_TREECHOP_MULTI_AGENT_2_V0 = TreechopMultiAgent(agent_count=2)
MINERL_TREECHOP_MULTI_AGENT_3_V0 = TreechopMultiAgent(agent_count=3)

MINERL_NAVIGATE_V0 = Navigate(dense=False, extreme=False)
MINERL_NAVIGATE_EXTREME_V0 = Navigate(dense=False, extreme=True)
MINERL_NAVIGATE_DENSE_V0 = Navigate(dense=True, extreme=False)
MINERL_NAVIGATE_DENSE_EXTREME_V0 = Navigate(dense=True, extreme=True)

MINERL_OBTAIN_DIAMOND_V0 = ObtainDiamond(dense=False)
MINERL_OBTAIN_DIAMOND_DENSE_V0 = ObtainDiamond(dense=True)

MINERL_OBTAIN_IRON_PICKAXE_V0 = ObtainIronPickaxe(dense=False)
MINERL_OBTAIN_IRON_PICKAXE_DENSE_V0 = ObtainIronPickaxe(dense=True)

# # prototype envs
# # TODO: Actually make these work and correct, it'll be good to release these.
# MINERL_OBTAIN_MEAT_V0 = Obtain(target_item='meat', dense=False, reward_schedule={
#     'beef': 1,
#     'mutton': 1,
#     'porkchop': 1,
#     'chicken': 1,
#     'cooked_beef': 10,
#     'cooked_mutton': 10,
#     'cooked_porkchop': 10,
#     'cooked_chicken': 10,
# })
# MINERL_OBTAIN_BED_V0 = Obtain(target_item='bed', dense=False, reward_schedule=None)

# Competition environments.
# TODO: Determine naming schemes
comp_envs = [MINERL_OBTAIN_DIAMOND_V0, MINERL_TREECHOP_V0, MINERL_NAVIGATE_V0, MINERL_OBTAIN_IRON_PICKAXE_V0]
comp_obfuscator_dir = os.path.join(

# TODO FORMAT THIS AUTOMATICALLY USING CIRCULAR IMPORTS
os.path.dirname(os.path.abspath(__file__)), "env_specs", "obfuscators", "comp", "v3")


MINERL_TREECHOP_OBF_V0 = Obfuscated(Vectorized(MINERL_TREECHOP_V0, common_envs=comp_envs), comp_obfuscator_dir)

MINERL_NAVIGATE_OBF_V0 = Obfuscated(Vectorized(MINERL_NAVIGATE_V0, common_envs=comp_envs), comp_obfuscator_dir)
MINERL_NAVIGATE_EXTREME_OBF_V0 = Obfuscated(Vectorized(MINERL_NAVIGATE_EXTREME_V0, common_envs=comp_envs), comp_obfuscator_dir)
MINERL_NAVIGATE_DENSE_OBF_V0 = Obfuscated(Vectorized(MINERL_NAVIGATE_DENSE_V0, common_envs=comp_envs), comp_obfuscator_dir)
MINERL_NAVIGATE_DENSE_EXTREME_OBF_V0 = Obfuscated(Vectorized(MINERL_NAVIGATE_DENSE_EXTREME_V0, common_envs=comp_envs), comp_obfuscator_dir)

MINERL_OBTAIN_DIAMOND_OBF_V0 = Obfuscated(Vectorized(MINERL_OBTAIN_DIAMOND_V0, common_envs=comp_envs), comp_obfuscator_dir)
MINERL_OBTAIN_DIAMOND_DENSE_OBF_V0 = Obfuscated(Vectorized(MINERL_OBTAIN_DIAMOND_DENSE_V0, common_envs=comp_envs), comp_obfuscator_dir)

MINERL_OBTAIN_IRON_PICKAXE_OBF_V0 = Obfuscated(Vectorized(MINERL_OBTAIN_IRON_PICKAXE_V0, common_envs=comp_envs), comp_obfuscator_dir)
MINERL_OBTAIN_IRON_PICKAXE_DENSE_OBF_V0 = Obfuscated(Vectorized(MINERL_OBTAIN_IRON_PICKAXE_DENSE_V0, common_envs=comp_envs), comp_obfuscator_dir)

# Survival envs
MINERL_OBTAIN_DIAMOND_SURVIVAL_V0 = Obfuscated(Vectorized(ObtainDiamondSurvival(dense=True), common_envs=comp_envs), comp_obfuscator_dir, 'MineRLObtainDiamondSurvivalVectorObf-v0')

obfuscated_envs = [e for e in locals().values() if isinstance(e, Obfuscated)]

# ENVS = [MINERL_OBTAIN_IRON_PICKAXE_OBF_V0]


# Test environments
# TODO: Generate obfuscations for these envs.
MINERL_OBTAIN_TEST_V0 = ObtainDiamondDebug(dense=False)
MINERL_OBTAIN_TEST_VEC_V0 = Vectorized(MINERL_OBTAIN_TEST_V0)
# MINERL_OBTAIN_TEST_OBF_V0 = Obfuscated(MINERL_OBTAIN_TEST_VEC_V0)

MINERL_OBTAIN_TEST_DENSE_V0 = ObtainDiamondDebug(dense=True)
MINERL_OBTAIN_TEST_DENSE_VEC_V0 = Vectorized(MINERL_OBTAIN_TEST_DENSE_V0)
# MINERL_OBTAIN_TEST_DENSE_OBF_V0 = Obfuscated(MINERL_OBTAIN_TEST_DENSE_VEC_V0)


# Register the envs.
ENVS = [env for env in locals().values() if isinstance(env, EnvSpec)]
for env in ENVS:
    if env.name not in gym.envs.registry.env_specs:
        env.register()
        env.register(fake=True)




# # TODO: Convert to an env_spec environment
# from minerl.herobraine.hero.unified_spaces import unified_action_space, unified_observation_space

# register(
#     id='UnifiedMineRL-v0',
#     entry_point='minerl.env:MineRLEnv',
#     kwargs={
#         'observation_space': unified_observation_space,
#         'action_space':  unified_action_space
#     },
#     max_episode_steps=20 * 60 * 60 * 2, # 2 hrs
# )

