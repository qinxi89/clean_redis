import sys
import time
import subprocess

def clean_redis(host, port, password, rediskey):
    for i in range(10000):
        # 构造 Redis 命令
        cmd_scan = f'redis-cli -h {host} -p {port} -n 0 -a {password} scan {i} match {rediskey}* count 100'
        
        # 执行 Redis 命令并获取输出
        output = subprocess.check_output(cmd_scan, shell=True, stdin=subprocess.DEVNULL).decode('utf-8')
        # 解析输出，获取键列表
        if output:
           keys = []
           for line in output.split('\n'):
               if line:
                  key = line.split('"')[0]
                  keys.append(key)

           print("\n")
          
            # 删除键
           for key in keys:
               print("Deleting Redis key: ",key)
               cmd_del = f'redis-cli -h {host} -p {port} -n 0 -a {password} del "{key}"'
               subprocess.run(cmd_del, shell=True, stdin=subprocess.DEVNULL)
        
        # 暂停0.2秒
        time.sleep(0.2)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <host> <port> <password> <rediskey>")
        sys.exit(1)
        
    host = sys.argv[1]
    port = sys.argv[2]
    password = sys.argv[3]
    rediskey = sys.argv[4]
    
    clean_redis(host, port, password, rediskey)
