# Install

## 主要安装包版本：

Ubuntu == 18.04 LTS

Anaconda == 3

Python  == 3.7

neo4j == 3.2.9

rasa_core == 0.10.4

rasa_core_sdk == 0.12.1

rasa_nlu == 0.13.8

rasa_addons == 0.4.3

tensorflow  == 1.8.0

gcc ==7.3.0

pypher 


## 环境安装：
### anaconda 安装：
```   
wget https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh
bash Anaconda3-2018.12-Linux-x86_64.sh
```


###	rasa安装
* 基础包安装
```
pip install rasa_core==0.10.4

pip install rasa_addons==0.4.3
pip install sklearn_crfsuite
pip install jieba
rasa_nlu在安装rasa_core的过程中已经装好,此处不需要安装。

```

* 修改第三方开源文件
由于前端网页返回值类型错误，所以修改开源文件。

```
vim  /home/user_name/anaconda3/envs/envs_name/lib/python3.6/site-packages/rasa_addons/webchat/__init.py
```
将文件中的125、126行注释:

```
#output_channel.custom_data = message['customData']
#on_message(UserMessage(message['message'], output_channel, request.sid))
```

修改成如下格式：
```
output_channel.custom_data = message
on_message(UserMessage(message,output_channel,request.sid))
```

* 安装pypher：
按照https://github.com/emehrkay/Pypher提示安装

* 安装cocoNLP: 
```
git clone https://github.com/fighting41love/cocoNLP.git
cd cocoNLP
python setup.py install
```

* 依赖包安装：
当使用第三方包spacy时,需要下载安装依赖中文包zh-core-web-sm，点击[链接](https://github.com/howl-anderson/Chinese_models_for_SpaCy "With a Title")。下载完成后执行以下指令：
```
pip install zh_core_web_sm-2.x.x.tar.gz
pip install xxx.tar.gz
spacy link zh_core_web_sm zh  （为方便使用，建立链接）
```

## neo4j数据库安装
Neo4j基于Java8，所以在安装之前先安装Java8.

### 安装Java 8
* 下载Java8
点此[链接](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html "With a Title")。

* 安装Java8
```
tar -xzvf jdk*******x64.tar.gz
cd jdk******
```
* 修改环境变量

```
vim ~/.bashrc
export JAVA_HOME=your_path/jdk******
export JRE_HOME=${JAVA_HOME}/jre 
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib 
export PATH=${JAVA_HOME}/bin:$PATH 
source ~/.bashrc
java -version 
```
若能正常显示Java版本，则安装成功。



### 安装Neo4j

* Neo4j[官方网站](https://neo4j.com/download/ "With a Title")下载安装包，或者点此下载。
* 安装Neo4j

```
tar -xzvf neo4j-******.tar.gz 
cd neo4j-******/bin
./neo4j console
```

### 导入数据
* 打开Neo4j的web端，一般是https://127.0.0.1:7474
* 将*.CSV数据文件复制到/neo4j/neo4j-community-3.2.9/import路径下，并打开此路径下的load_csv.py文件。
* 打开/chatbot/coarse_grained/load_csv.py文件，将文件内的命令逐行复制到Neo4j的web端命令窗口逐行执行。
* 点击数据库图标出现节点属性等信息即代表数据导入完成。
   
            数据文件需线下拷贝。


## chatbot安装
* 安装git: 
```
sudo apt-get install git
```

* 下载代码：
```
下载代码需要Gitlab用户权限，需要加入此项目用户组。
git clone http://gitlab.ai.chuangxin.com/sv-med/img/workreports/wikis/home
```
* 训练模型

    * 训练细粒度意图识别模型
    
    ```
    cd chatbot/fine_grained
    bash train_NLU.bash
    ```
    
    * 训练rasa_nlu
    ```
    cd chatbot/coarse_grained
    bash train_NLU.bash
    ```

    * 训练rasa_core 
    ```
    cd chatbot/coarse_grained
    bash train_CORE.bash
    ```


## 启动chatbot
* 打开数据库
```
cd /neo4j/neo4j-community-3.2.9/bin
./neo4j console
```
* 运行chatbot:
```
python webchat.py
```
* 在浏览器中打开http://127.0.0.1:5500/，即可进行对话。


# 文件说明


## 文件结构  
![Image text](http://gitlab.ai.chuangxin.com/chengzhengtao/qa_bot/blob/master/1.png)

## 代码
* train_CORE.bash: 训练意图识别模块
* train_NLU.bash: 训练对话管理模块
* webchat.py：前端代码
* botAction.py：自定义对话机器人回复动作。

## 训练数据
./data/文件夹下

* domain.yml：实体、动作等定义模块
* chatito.txt: rasa_nlu训练数据
* nlu_model_config.yaml：rasa_nlu的pipline设定。
* stiries.md:  业务逻辑设计
* training_dataset.json：训练数据，可以使用[链接](https://rodrigopivi.github.io/Chatito/ "With a Title")生成。

## 模型
./models/文件夹下

* ./dialogue/文件夹下主要是意图识别模型
* ./nlu/文件夹下主要是对话管理模型


