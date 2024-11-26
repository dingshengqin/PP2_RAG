DoPP2_RAG 项目维护指南



<div align="center">A RAG UI which copy from an open-source clean & customizable RAG UI of dingshengqin/PP2_RAG. And we did some customize work based on it.



![Preview](https://raw.githubusercontent.com/dingshengqin/PP2_RAG/main/docs/images/preview-graph.png)

[Live Demo](https://huggingface.co/spaces/cin-model/kotaemon-demo) |
[Online Install](https://cinnamon.github.io/kotaemon/online_install/) |
[User Guide](https://cinnamon.github.io/kotaemon/) |
[Developer Guide](https://cinnamon.github.io/kotaemon/development/) |
[Feedback](https://github.com/dingshengqin/PP2_RAG/issues) |
[Contact](mailto:dshengq@163.com)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-31013/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<a href="https://github.com/dingshengqin/PP2_RAG/pkgs/container/kotaemon" target="_blank">
<img src="https://img.shields.io/badge/docker_pull-kotaemon:latest-brightgreen" alt="docker pull ghcr.io/dingshengqin/PP2_RAG:latest"></a>
![download](https://img.shields.io/github/downloads/dingshengqin/PP2_RAG/total.svg?label=downloads&color=blue)
<a href='https://huggingface.co/spaces/cin-model/kotaemon-demo'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue'></a>
<a href="https://hellogithub.com/en/repository/d3141471a0244d5798bc654982b263eb" target="_blank"><img src="https://abroad.hellogithub.com/v1/widgets/recommend.svg?rid=d3141471a0244d5798bc654982b263eb&claim_uid=RLiD9UZ1rEHNaMf&theme=small" alt="Featured｜HelloGitHub" /></a>

</div>


# Introduction


This project serves as a functional RAG UI for both end users who want to do QA on their
documents and developers who want to build their own RAG pipeline.
<br>


```yml
+----------------------------------------------------------------------------+
| End users: Those who use apps built with `kotaemon`.                       |
| (You use an app like the one in the demo above)                            |
|     +----------------------------------------------------------------+     |
|     | Developers: Those who built with `kotaemon`.                   |     |
|     | (You have `import kotaemon` somewhere in your project)         |     |
|     |     +----------------------------------------------------+     |     |
|     |     | Contributors: Those who make `kotaemon` better.    |     |     |
|     |     | (You make PR to this repo)                         |     |     |
|     |     +----------------------------------------------------+     |     |
|     +----------------------------------------------------------------+     |
+----------------------------------------------------------------------------+
```


## For end users


- **Clean & Minimalistic UI**: A user-friendly interface for RAG-based QA.
- **Support for Various LLMs**: Compatible with LLM API providers (OpenAI, AzureOpenAI, Cohere, etc.) and local LLMs (via `ollama` and `llama-cpp-python`).
- **Easy Installation**: Simple scripts to get you started quickly.


## For developers


- **Framework for RAG Pipelines**: Tools to build your own RAG-based document QA pipeline.
- **Customizable UI**: See your RAG pipeline in action with the provided UI, built with <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.
- **Gradio Theme**: If you use Gradio for development, check out our theme here: [kotaemon-gradio-theme](https://github.com/lone17/kotaemon-gradio-theme).


# Key Features


- **Host your own document QA (RAG) web-UI**: Support multi-user login, organize your files in private/public collections, collaborate and share your favorite chat with others.


- **Organize your LLM & Embedding models**: Support both local LLMs & popular API providers (OpenAI, Azure, Ollama, Groq).


- **Hybrid RAG pipeline**: Sane default RAG pipeline with hybrid (full-text & vector) retriever and re-ranking to ensure best retrieval quality.


- **Multi-modal QA support**: Perform Question Answering on multiple documents with figures and tables support. Support multi-modal document parsing (selectable options on UI).


- **Advanced citations with document preview**: By default the system will provide detailed citations to ensure the correctness of LLM answers. View your citations (incl. relevant score) directly in the _in-browser PDF viewer_ with highlights. Warning when retrieval pipeline return low relevant articles.


- **Support complex reasoning methods**: Use question decomposition to answer your complex/multi-hop question. Support agent-based reasoning with `ReAct`, `ReWOO` and other agents.


- **Configurable settings UI**: You can adjust most important aspects of retrieval & generation process on the UI (incl. prompts).


- **Extensible**: Being built on Gradio, you are free to customize or add any UI elements as you like. Also, we aim to support multiple strategies for document indexing & retrieval. `GraphRAG` indexing pipeline is provided as an example.


![Preview](https://raw.githubusercontent.com/dingshengqin/PP2_RAG/main/docs/images/preview.png)


# Installation


> If you are not a developer and just want to use the app, please check out our easy-to-follow [User Guide](https://cinnamon.github.io/kotaemon/). Download the `.zip` file from the [latest release](https://github.com/dingshengqin/PP2_RAG/releases/latest) to get all the newest features and bug fixes.


## System requirements


1. [Python](https://www.python.org/downloads/) >= 3.10
2. [Docker](https://www.docker.com/): optional, if you [install with Docker](#with-docker-recommended)
3. [Unstructured](https://docs.unstructured.io/open-source/installation/full-installation#full-installation) if you want to process files other than `.pdf`, `.html`, `.mhtml`, and `.xlsx` documents. Installation steps differ depending on your operating system. Please visit the link and follow the specific instructions provided there.


## Clone steps


1. Clone and install required packages on a fresh python environment.

 

```
   # optional (setup env)

   conda create -n kotaemon python=3.10
   conda activate kotaemon


   # clone this repo

   git clone https://github.com/dingshengqin/PP2_RAG
   cd PP2_RAG
   
   pip install -e "libs/kotaemon[all]" 
   pip install -e "libs/ktem" 
```

If fails, you can add download source

```
  
   pip install -e "libs/kotaemon[all]" -i http://mirrors.aliyun.com/pypi/simple/ --trust mirrors.aliyun.com/pypi
   pip install -e "libs/kotaemon[all]" -i https://pypi.tuna.tsinghua.edu.cn/simple --trust pypi.tuna.tsinghua.edu.cn/simple
   pip install -e "libs/ktem" -i http://mirrors.aliyun.com/pypi/simple/ --trust mirrors.aliyun.com/pypi
   pip install -e "libs/ktem" -i https://pypi.tuna.tsinghua.edu.cn/simple --trust pypi.tuna.tsinghua.edu.cn/simple
```




2. Create a `.env` file in the root of this project. Use `.env.example` as a template


   The `.env` file is there to serve use cases where users want to pre-config the models before starting up the app (e.g. deploy the app on HF hub). The file will only be used to populate the db once upon the first run, it will no longer be used in consequent runs.


3. (Optional) To enable in-browser `PDF_JS` viewer, download [PDF_JS_DIST](https://github.com/mozilla/pdf.js/releases/download/v4.0.379/pdfjs-4.0.379-dist.zip) then extract it to `libs/ktem/ktem/assets/prebuilt`

<img src="https://raw.githubusercontent.com/dingshengqin/PP2_RAG/main/docs/images/pdf-viewer-setup.png" alt="pdf-setup" width="300">


4. Start the web server:


   ```shell
   python app.py
   ```


   - The app will be automatically launched in your browser.
   - Default username and password are both `admin`. You can set up additional users directly through the UI.


   ![Chat tab](https://raw.githubusercontent.com/dingshengqin/PP2_RAG/main/docs/images/chat-tab.png)


5. Check the `Resources` tab and `LLMs and Embeddings` and ensure that your `api_key` value is set correctly from your `.env` file. If it is not set, you can set it there.

### Setup GraphRAG



> [!NOTE]
> Official MS GraphRAG indexing only works with OpenAI or Ollama API.
> We recommend most users to use NanoGraphRAG implementation for straightforward integration with Kotaemon.



**Setup Nano GRAPHRAG**

- Install nano-GraphRAG: `pip install nano-graphrag`
- `nano-graphrag` install might introduce version conflicts, see [this issue](https://github.com/Cinnamon/kotaemon/issues/440)
- To quickly fix: `pip uninstall hnswlib chroma-hnswlib && pip install chroma-hnswlib`
- Launch Kotaemon with `USE_NANO_GRAPHRAG=true` environment variable.
- Set your default LLM & Embedding models in Resources setting and it will be recognized automatically from NanoGraphRAG.



<b>Setup MS GRAPHRAG</b>

- \- ***\*Non-Docker Installation\****: If you are not using Docker, install GraphRAG with the following command:

- ```
   ​```shell
   pip install graphrag future
   ```
  
- \- ***\*Setting Up API KEY\****: To use the GraphRAG retriever feature, ensure you set the `GRAPHRAG_API_KEY` environment variable. You can do this directly in your environment or by adding it to a `.env` file.

- \- ***\*Using Local Models and Custom Settings\****: If you want to use GraphRAG with local models (like `Ollama`) or customize the default LLM and other configurations, set the `USE_CUSTOMIZED_GRAPHRAG_SETTING` environment variable to true. Then, adjust your settings in the `settings.yaml.example` file.








### Setup Local Models (for local/private RAG)


See [Local model setup](docs/local_model.md).


### Customize your application


- By default, all application data is stored in the `./ktem_app_data` folder. You can back up or copy this folder to transfer your installation to a new machine.


- For advanced users or specific use cases, you can customize these files:


  - `flowsettings.py`
  - `.env`


#### `flowsettings.py`

This file contains the configuration of your application. You can use the example
[here](flowsettings.py) as the starting point.


<details>

<summary>Notable settings</summary>


```python
# setup your preferred document store (with full-text search capabilities)
KH_DOCSTORE=(Elasticsearch | LanceDB | SimpleFileDocumentStore)


# setup your preferred vectorstore (for vector-based search)
KH_VECTORSTORE=(ChromaDB | LanceDB | InMemory | Qdrant)


# Enable / disable multimodal QA
KH_REASONINGS_USE_MULTIMODAL=True


# Setup your new reasoning pipeline or modify existing one.
KH_REASONINGS = [
    "ktem.reasoning.simple.FullQAPipeline",
    "ktem.reasoning.simple.FullDecomposeQAPipeline",
    "ktem.reasoning.react.ReactAgentPipeline",
    "ktem.reasoning.rewoo.RewooAgentPipeline",
]
```

</details>


#### `.env`


This file provides another way to configure your models and credentials.


<details>



<summary>Configure model via the .env file</summary>


- Alternatively, you can configure the models via the `.env` file with the information needed to connect to the LLMs. This file is located in the folder of the application. If you don't see it, you can create one.


- Currently, the following providers are supported:


  - **OpenAI**


    In the `.env` file, set the `OPENAI_API_KEY` variable with your OpenAI API key in order
    to enable access to OpenAI's models. There are other variables that can be modified,
    please feel free to edit them to fit your case. Otherwise, the default parameter should
    work for most people.


    ```shell
    OPENAI_API_BASE=https://api.openai.com/v1
    OPENAI_API_KEY=<your OpenAI API key here>
    OPENAI_CHAT_MODEL=gpt-3.5-turbo
    OPENAI_EMBEDDINGS_MODEL=text-embedding-ada-002
    ```


  - **Azure OpenAI**


    For OpenAI models via Azure platform, you need to provide your Azure endpoint and API
    key. Your might also need to provide your developments' name for the chat model and the
    embedding model depending on how you set up Azure development.


    ```shell
    AZURE_OPENAI_ENDPOINT=
    AZURE_OPENAI_API_KEY=
    OPENAI_API_VERSION=2024-02-15-preview
    AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-35-turbo
    AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT=text-embedding-ada-002
    ```


  - **Local Models**


   - Using `ollama` OpenAI compatible server:


   - Install [ollama](https://github.com/ollama/ollama) and start the application.


   - Pull your model, for example:


        ```shell
        ollama pull llama3.1:8b
        ollama pull nomic-embed-text
        ```


   - Set the model names on web UI and make it as default:


        ![Models](https://raw.githubusercontent.com/dingshengqin/PP2_RAG/main/docs/images/models.png)


   - Using `GGUF` with `llama-cpp-python`


      You can search and download a LLM to be ran locally from the [Hugging Face Hub](https://huggingface.co/models). Currently, these model formats are supported:


   - GGUF


        You should choose a model whose size is less than your device's memory and should leave
        about 2 GB. For example, if you have 16 GB of RAM in total, of which 12 GB is available,
        then you should choose a model that takes up at most 10 GB of RAM. Bigger models tend to
        give better generation but also take more processing time.


        Here are some recommendations and their size in memory:


   - [Qwen1.5-1.8B-Chat-GGUF](https://huggingface.co/Qwen/Qwen1.5-1.8B-Chat-GGUF/resolve/main/qwen1_5-1_8b-chat-q8_0.gguf?download=true): around 2 GB


        Add a new LlamaCpp model with the provided model name on the web UI.


  </details>


### Adding your own RAG pipeline


#### Custom Reasoning Pipeline


1. Check the default pipeline implementation in [here](libs/ktem/ktem/reasoning/simple.py). You can make quick adjustment to how the default QA pipeline work.
2. Add new `.py` implementation in `libs/ktem/ktem/reasoning/` and later include it in `flowssettings` to enable it on the UI.


#### Custom Indexing Pipeline


- Check sample implementation in `libs/ktem/ktem/index/file/graph`



# Customize



以下内容默认您在WSL-Ubuntu 已经完成以下配置

- git安装
- vs code安装
- anaconda安装
- VPN 安装
- firefox浏览器安装



## vs code安装WSL插件

![image-20241106130640658](https://raw.githubusercontent.com/dingshengqin/image4typora/main/image/202411/14/084235-763758.png)





## Clone 项目（和Installation 重复，已经做的不要再做）

```
进入Ubuntu

  # optional (setup env)

   conda create -n kotaemon python=3.10
   conda activate kotaemon


   # clone this repo

   git clone https://github.com/dingshengqin/PP2_RAG
   cd PP2_RAG
   
   pip install -e "libs/kotaemon[all]" 
   pip install -e "libs/ktem" 
```

如果失败，可以添加源

```
  
   pip install -e "libs/kotaemon[all]" -i http://mirrors.aliyun.com/pypi/simple/ --trust mirrors.aliyun.com/pypi
   pip install -e "libs/kotaemon[all]" -i https://pypi.tuna.tsinghua.edu.cn/simple --trust pypi.tuna.tsinghua.edu.cn/simple
   pip install -e "libs/ktem" -i http://mirrors.aliyun.com/pypi/simple/ --trust mirrors.aliyun.com/pypi
   pip install -e "libs/ktem" -i https://pypi.tuna.tsinghua.edu.cn/simple --trust pypi.tuna.tsinghua.edu.cn/simple
```



## 测试更改push

- 从Windows 文档系统进入/home/dshengq/github/PP2_RAG

- 右击——选择“Open Git Bash here”

- 输入以下代码，地址改成自己的

  ```
  git config --global --add safe.directory '%(prefix)///wsl.localhost/Ubuntu-20.04/home/dshengq/github/PP2_RAG'
  ```

- git 常规操作

  ```
   git checkout -b ding # 注意换成自己的branch名称 
  ```

- 打开vs code，点击左下角图标，进入WSL-Ubuntu

  ![image-20241106132000846](https://raw.githubusercontent.com/dingshengqin/image4typora/main/image/202411/14/083801-625388.png)

- 任意更改一个文件

- 回到git bash界面

- 输入以下命令

  ```
  git add . # 把所有更改stage掉
  git commit -m "change comment"
  git push origin ding:ding #注意换成自己的branch名称 ,后面的push只需要git push origin ding
  ```

- 浏览器进入github项目地址，compare& merge 到main分支

- ```
  注意点：
  - 每次push完之后，vscode里面的push状态并不能更新，重新关闭打开后才能同步最新的更改状态监控,  不着急的话等一会也能同步
  - 我没有能够在vs code的terminal测试成功git push，也许其他人可以，我目前只能从git bash去push
  - 我一般会在vs code的terminal输入： cd /home/dsheng/github/PP2_RAG，这样感觉不容易出错
  - 可以运行 python app.py了，进入下一步
  
  ```



## [打开服务器端口7860的防火墙](https://blog.csdn.net/weixin_52730346/article/details/120720527)

```
备注：
链接我随便搜的教程，大差不差，供参考
```

## [局域网访问wsl](https://blog.csdn.net/u012795439/article/details/135675005)

在powershell里面输入

```
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=7860 connectaddress=172.27.235.43 connectport=7860
New-NetFirewallRule -DisplayName "WSL" -Direction Inbound -InterfaceAlias "vEthernet (WSL)" -Action Allow

```

ip 172.27.235.43 地址通讯在ubuntu查询

![image-20241015101145368](https://raw.githubusercontent.com/dingshengqin/image4typora/main/image/202411/14/083804-153357.png)



进入windows浏览器，输入 xxx.xxx.xxx.xxx:7860, ip地址查询如下

![image-20241015103431457](https://raw.githubusercontent.com/dingshengqin/image4typora/main/image/202411/14/083806-169809.png)



## 添加rerank模型

### Docker 安装

#### [方案1：WSL 2 上的 Docker 安装-推荐](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-containers)

- 下载 [Docker Desktop](https://docs.docker.com/docker-for-windows/wsl/#download) 并按照安装说明进行操作。

- 确保在“设置”>“常规”中选中“使用基于 WSL 2 的引擎”。

  ![Docker Desktop 常规设置](https://learn.microsoft.com/zh-cn/windows/wsl/media/docker-running.png)

- 通过转到“设置”>“资源”>“WSL 集成”，从要启用 Docker 集成的已安装 WSL 2 发行版中进行选择

  ![Docker Desktop 资源设置](https://learn.microsoft.com/zh-cn/windows/wsl/media/docker-dashboard.png)

#### 方案2：Ubuntu 安装Docker方案2（不推荐）



（1）添加Docker存储库

Docker存储库包含Docker软件包，您需要将其添加到系统中。可以使用以下命令：

```
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```


（2）安装Docker

安装最新版本的Docker Engine和containerd。可以使用以下命令：

```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```


（3）验证Docker是否安装成功

```
sudo docker run hello-world
```


此处执行这个命令是会报错的，错误信息如下

```
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
See 'docker run --help'.
```


原因是wsl2不支持systemctl命令，而是支持systemed命令

所以需要执行如下命令先启动docker

```
service docker start
```

#### [方案3：Ubuntu安装Docker-不推荐](https://docs.docker.com/desktop/setup/install/linux/ubuntu/)

#### 方案4：安装Nvidia docker-不推荐

[参考链接1](https://blog.csdn.net/wsp_1138886114/article/details/128201910)

```
注意点：
最后一行sudo service docker start改成sudo systemctl restart docker
```



### 安装本地rerank模型

#### Docker本地下载镜像

创建目录

```
mkdir /home/username/.cache/huggingface/data
cd /home/username/.cache/huggingface
```

下载镜像，大概率下载不下来

```
model=BAAI/bge-reranker-large

volume=$PWD/data

docker run --gpus all -p 8080:80 --name TEI  -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:86-1.5 --model-id $model 

如果没有权限尝试
sudo docker run --gpus all -p 8080:80 TEI -v $volume:/data --pull always 	ghcr.io/huggingface/text-embeddings-inference:86-1.5 --model-id $model
```

[手动下载模型](https://huggingface.co/BAAI/bge-reranker-large/tree/main)

```
下载的内容copy到以下目录,注意onnx的要放到onnx文件夹里面
home\username\.cache\huggingface\data\models--BAAI--bge-reranker-large\snapshots\55611d7bca2a7133960a6d3b71e083071bbfc312
```

重新docker run

```
docker run --gpus all -p 8080:80 --name TEI  -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:86-1.5 --model-id $model 
```

出现这个说明部署成功了

![image-20241126083619348](https://raw.githubusercontent.com/dingshengqin/image4typora/main/image/202411/26/083735-339952.png)

测试

```

curl 127.0.0.1:8080/rerank -X POST  -d '{"query":"What is Deep Learning?", "texts": ["Deep Learning is not...", "Deep learning is..."], "raw_scores": false}'  -H 'Content-Type: application/json'

```

Stop和重启容器

```bash
# 删除容器
docker rm -f TEI
# 下次重启容器
docker start TEI
# 或者
docker ps -a
# 找到TEI的容器ID然后
docker start <容器ID>

```



```
model=BAAI/bge-reranker-large

volume=$PWD/data

docker run --gpus all -p 8080:80 --name TEI  -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:86-1.5 --model-id $model 

如果没有权限尝试
sudo docker run --gpus all -p 8080:80 -v $volume:/data --pull always 	ghcr.io/huggingface/text-embeddings-inference:86-1.5 --model-id $model



```

#### PP2_RAG 配置

endpoint_url: http://localhost:8080/rerank

![image-20241122083257841](https://raw.githubusercontent.com/dingshengqin/image4typora/main/image/202411/22/083259-786876.png)



#### Reference

[搭建TEI平台并部署模型](https://juejin.cn/post/7438545751511629860)

[TEI arguments](https://huggingface.co/docs/text-embeddings-inference/cli_arguments)

[Bug：docker: Error response from daemon: could not select device driver "" with capabilities: gpu.](https://stackoverflow.com/questions/75118992/docker-error-response-from-daemon-could-not-select-device-driver-with-capab)

[How can I use Docker without sudo?](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo)

[Docker-credential-desktop.exe executable file not found in $PATH using wsl2](https://forums.docker.com/t/docker-credential-desktop-exe-executable-file-not-found-in-path-using-wsl2/100225)



### Docker 本地镜像

```
docker build -t pp2_rag:0.0.1 .
```

