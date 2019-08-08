#隆鼻医美领域对话机器人
##步骤
###准备文件 ./data
1. training_dataset.json
这个是训练 意图 识别和 实体提取 的数据集
可以通过 chaito 自动产生
https://rodrigopivi.github.io/Chatito/

2. domain.yml
这个是定义 意图 实体 槽 动作的 文件

3. stories.md
这个是训练 对话 流程的 数据集

###执行过程

####安装工具包：
pip install rasa_nlu==0.13.8
pip install rasa_core==0.10.4
pip install rasa-addons==0.4.3
####
./train_NLU.bash
./train_CORE.bash
python webchat.py

用浏览器访问	http://localhost:5500
