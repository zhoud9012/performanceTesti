DEMO
===========================

## 环境依赖
Python 3.0+

## 部署与使用
1. 安装Python 环境
2. 启动测试脚本
    ```python
   python run.py thread_count url method header body body_type
    ```
eg:
    ```python
    python3.5 run.py 10 http://api-app.smartisan.com/app/index.php?r=api/v1_4/Recommend/List get "{'Market-Version': '3.1'}" "" "json"
    ```
3. 参数解释
    thread_count:并发量
    url:接口地址
    method:请求方法
    header:请求头
    body:请求体
    body_type:请求体类型:1.json 2.file 3.data

## 目录结构描述
├── 2to3                        // Python 2转3 语法
├── common                      // 测试公用类目录
│  ├── __init__.py              
│  ├── Performance.py           // 性能测试基类
│  └── __pycache__              
├── Readme.md                   // help
└── run.py                      // 运行入口

## V1.0.0 版本内容更新
1. 语法修改   语法由Python 2转3
2. 新功能   测试脚本参数化
