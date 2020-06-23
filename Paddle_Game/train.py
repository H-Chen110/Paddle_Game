import numpy as np



LEARN_FREQ = 5 # 训练频率，不需要每一个step都learn，攒一些新增经验后再learn，提高效率
MEMORY_WARMUP_SIZE = 200  # replay_memory 里需要预存一些经验数据，再从里面sample一个batch的经验让agent去learn
BATCH_SIZE = 32   # 每次给agent learn的数据数量，从replay memory随机里sample一批数据出来


# 训练一个episode
def run_episode(env, agent, rpm):
    total_reward = 0
    obs = env.reset()
    obs = np.reshape(obs, (1,5))
    step = 0
    while True:
        step += 1
        action = agent.sample(obs)  # 采样动作，所有动作都有概率被尝试到
        reward, next_obs, done = env.step(action)
        next_obs = np.reshape(next_obs,(1,5))
        rpm.append((obs, action, reward, next_obs, done))

        # train model
        if (len(rpm) > MEMORY_WARMUP_SIZE) and (step % LEARN_FREQ == 0):
            (batch_obs, batch_action, batch_reward, batch_next_obs,
             batch_done) = rpm.sample(BATCH_SIZE)
            train_loss = agent.learn(batch_obs, batch_action, batch_reward,
                                     batch_next_obs,
                                     batch_done)  # s,a,r,s',done

        total_reward += reward
        obs = next_obs
        if done:
            break
    return total_reward


# 评估 agent, 跑 5 个episode，总reward求平均
def evaluate(env, agent):
    eval_reward = []
    for i in range(5):
        obs = env.reset()
        obs = np.reshape(obs, (1,5))
        episode_reward = 0
        while True:
            action = agent.predict(obs)  # 预测动作，只选最优动作
            reward, obs, done = env.step(action)
            episode_reward += reward
          
            if done:
                break
        eval_reward.append(episode_reward)
    return np.mean(eval_reward)
