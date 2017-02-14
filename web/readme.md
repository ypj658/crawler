####安装依赖库
    pip3 install flask
    pip3 install flask-script
    pip3 install flask-bootstrap
    pip3 install scrapy
    pip3 install sqlalchemy
    pip3 install requests
    pip3 install xmltodict
    pip3 install pycrypto
    pip3 install uwsgi
    
####Linux 下面自动执行脚本（auto_run_crawer.sh）
    vi auto_run_crawer.sh    
    . /home/web/venv/bin/activate
    python3  /home/web/weixin/crawl/zhengfu/zhengfu/run.py
    deactivate
#### 配置定时执行,每天6点自动执行脚本
    crontab -e    
<<<<<<< HEAD
    0 6 * * * sh /home/web/auto_run_crawl.sh
=======
    0 6 * * * sh /home/web/auto_run_crawl.sh

####Linux下配置flask启动
* 使用nginx+uwsgi启动，各自的配置文件分别为
    * nginx
    
            server {
                listen	80;
                #server_name	localost;
                charset	utf-8;
            
                location / { try_files $uri @python_flask; }
                location @python_flask {
                    include uwsgi_params;
                    uwsgi_pass 127.0.0.1:8001;  ;/tmp/uwsgi.pid
                }
            }
    * uwsgi配置文件（uwsgiconfig.ini）
         
            [uwsgi]
            socket = 127.0.0.1:8001   ；/tmp/uwsgi.pid
            home = /home/web/venv/
            chdir = /home/web/weixin/
            wsgi-file = /home/web/weixin/weixin.py
            daemonize = /home/web/httpserver.log
            callable = app
            processes = 4
            threads = 2
            stats = 127.0.0.1:9191
    

###注意事项
* windows环境下需要pywin32支持

