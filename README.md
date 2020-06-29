# Paddle_Game
最近参加了百度的从零入门学习强化学习课程，最后使用强化学习的方法来尝试实现Paddle接球游戏。

# 配置说明
强化学习框架：parl 1.3.1 (附github链接)

parl：https://github.com/PaddlePaddle/PARL

编辑器：jupyter notebook

py版本：python 3.7

# 环境说明
游戏环境：Paddle接球小游戏 (附github链接)

paddle：https://github.com/shivaverma/Orbit

动作空间（3）：

            0-向左移动 
            
            1-什么都不做  
            
            2-向右移动
状态空间（5）：

            桨的x位置     
            
            球的x和y位置 
            
            球的x和y速度
            
奖励表示（3）：

            +3   ——接到目标球时
            
            -3   ——目标球碰到地面时  
            
            -0.1 ——每次移动
       
# 最终测试成绩
由于个人时间安排问题，在教程提供的代码上改环境做简单调试而已。

最终最好成绩为 10分。

保存代码供下次再次调试。
