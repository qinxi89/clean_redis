for i in `seq 0 10000`; do
    redis-cli -h 192.245.52.44 -p 6379 -a **** -n 0 scan $i match portrait_user_* count 100 | awk -F'"' '{print "\""$1"\""}' | xargs redis-cli -h 192.245.52.44 -p 6379 -a ****** -n 0 del;
    sleep 0.2;
done
