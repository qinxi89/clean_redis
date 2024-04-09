import sys
import time
import subprocess

def clean_redis(host, port, password):
    # 清除10000个key值，可自定义
    for i in range(10001):
        # 构造 Redis 命令，count 100 表示每次扫描返回最大数量
        cmd_scan = f'redis-cli -h {host} -p {port} -a {password} -n 0 scan {i} match portrait_user_* count 100'
        
        # 执行 Redis 命令并获取输出
        output = subprocess.check_output(cmd_scan, shell=True).decode('utf-8')
        
        # 解析输出，获取键列表
        keys = [line.split('"')[1] for line in output.split('\n') if line]
        
        # 删除键
        for key in keys:
            cmd_del = f'redis-cli -h {host} -p {port} -a {password} -n 0 del "{key}"'
            subprocess.run(cmd_del, shell=True)
        
        # 暂停0.2秒
        time.sleep(0.2)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <host> <port> <password>")
        sys.exit(1)
        
    host = sys.argv[1]
    port = sys.argv[2]
    password = sys.argv[3]
    
    clean_redis(host, port, password)

