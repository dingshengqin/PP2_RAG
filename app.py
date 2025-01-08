# import os

# from theflow.settings import settings as flowsettings

# KH_APP_DATA_DIR = getattr(flowsettings, "KH_APP_DATA_DIR", ".")
# GRADIO_TEMP_DIR = os.getenv("GRADIO_TEMP_DIR", None)
# # override GRADIO_TEMP_DIR if it's not set
# if GRADIO_TEMP_DIR is None:
#     GRADIO_TEMP_DIR = os.path.join(KH_APP_DATA_DIR, "gradio_tmp")
#     os.environ["GRADIO_TEMP_DIR"] = GRADIO_TEMP_DIR


# from ktem.main import App  # noqa

# app = App()
# demo = app.make()
# demo.queue().launch(
#     favicon_path=app._favicon,
#     inbrowser=True,
#     allowed_paths=[
#         "libs/ktem/ktem/assets",
#         GRADIO_TEMP_DIR,
#     ],
#     server_name="0.0.0.0",  # 指定服务器地址
#     server_port=7860        # 可以指定端口，默认是7860
# )

import os  
import logging  # 导入 logging 模块  

from theflow.settings import settings as flowsettings  

# 设置日志文件路径  
log_file_path = os.path.join(flowsettings.KH_APP_DATA_DIR, "app.log")  

# 配置日志记录  
logging.basicConfig(  
    filename=log_file_path,  
    level=logging.INFO,  # 设置日志级别  
    format='%(asctime)s - %(levelname)s - %(message)s'  # 设置日志格式  
)  

# 记录启动信息  
logging.info("程序开始运行.")  

KH_APP_DATA_DIR = getattr(flowsettings, "KH_APP_DATA_DIR", ".")  
GRADIO_TEMP_DIR = os.getenv("GRADIO_TEMP_DIR", None)  

# override GRADIO_TEMP_DIR if it's not set  
if GRADIO_TEMP_DIR is None:  
    GRADIO_TEMP_DIR = os.path.join(KH_APP_DATA_DIR, "gradio_tmp")  
    os.environ["GRADIO_TEMP_DIR"] = GRADIO_TEMP_DIR  
    logging.info(f"GRADIO_TEMP_DIR 未设置，使用默认路径: {GRADIO_TEMP_DIR}")  

from ktem.main import App  # noqa  

try:  
    app = App()  
    demo = app.make()  
    logging.info("应用程序成功创建.")  

    demo.queue().launch(  
        favicon_path=app._favicon,  
        inbrowser=True,  
        allowed_paths=[  
            "libs/ktem/ktem/assets",  
            GRADIO_TEMP_DIR,  
        ],  
        server_name="0.0.0.0",  # 指定服务器地址  
        server_port=7860        # 可以指定端口，默认是7860  
    )  
    logging.info("应用程序成功启动.")  
except Exception as e:  
    logging.error(f"运行过程中发生错误: {e}")