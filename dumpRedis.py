#!/usr/bin/python3
#-*- coding:utf-8 -*-

import redis
import argparse

def dump(host,port,password):
    pool = redis.ConnectionPool(host=host, port=port, password=password, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    keys = r.keys()
    for key in keys:
        print(r.get(key))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        type=str,
        help="Target Redis ip e.g: --host 10.1.1.2"
    )
    parser.add_argument(
        "--port",
        type=int,
        help="Port of Redis e.g: --port 6379",
        default=6379
    )
    parser.add_argument(
        "--passwd",
        type=str,
        help="Password of Redis e.g: -passwd 123456",
        default=""
    )
    args = parser.parse_args()
    target_ip = args.host
    target_port = args.port
    target_password = args.passwd
    dump(target_ip,target_port,target_password)
