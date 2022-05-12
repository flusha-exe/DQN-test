#gym库的基本使用操作如下
import gym
env = gym.make("CartPole-v1")      #调用该环境
observation = env.reset()		   #重置环境
for _ in range(1000):
  env.render()                     #打开环境窗口
  action = env.action_space.sample() # 从行为空间随机挑选动作
  observation, reward, done, info = env.step(action)   #执行一步action之后的返回值

  if done:
    observation = env.reset()
env.close()                         #关闭环境

