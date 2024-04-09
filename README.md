# clean_redis

#### 这两个脚本可以达到同样的效果，都可以用来清除redis 中指定的key键值，释放redis内存空间。  

---

 *clean_redis.sh 脚本解释:*   
```1.  for i in `seq 0 10000`; do: 这是一个循环结构，从0到10000，seq` 命令用于生成这个范围内的序列。

2.  redis-cli -h 172.245.52.44 -p 6379 -a ***** -n 0 scan $i match portrait_user_* count 100: 这是一个 Redis 命令行客户端的调用，用于扫描 Redis 数据库中的键值对。其中：
-h 172.245.52.44: 指定 Redis 服务器的主机地址。
-p 6379: 指定 Redis 服务器的端口号。
-a ******: 使用 Redis 访问密码。
-n 0: 指定 Redis 数据库的编号，这里为0。

3.  scan $i match portrait_user_* count 100: 使用 SCAN 命令扫描 Redis 中的键值对，其中 $i 是循环变量，用于遍历所有可能的游标值。match portrait_user_* 表示只匹配以 "portrait_user_" 开头的键。count 100 指定每次扫描返回的最大数量为100个。
4.  | awk -F'"' '{print "\""$1"\""}': 将 SCAN 命令的输出通过管道传递给 awk 命令，用于处理每一行的输出。-F'"'指定了分隔符为双引号，'{print "\""$1"\""}' 则是将输出的每一行的第一个字段加上双引号，以便后续的处理。

5.  | xargs redis-cli -h 172.245.52.44 -p 6379 -a ***** -n 0 del;: 将处理过的键通过管道传递给 xargs，然后再传递给另一个 Redis 命令行客户端调用，执行删除操作。del 命令用于删除指定的键值对。

6.  sleep 0.2;: 在每次循环结束后，暂停0.2秒，以避免过多的并发请求对 Redis 服务器造成负载压力。```


---
*clean_redis.py 脚本使用方法：*    

python clean_redis.py redis地址 redis端口 redis密码
