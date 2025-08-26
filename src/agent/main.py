from icmplib import ping

def main():
    host = '8.8.8.8'
    result = ping(host, count=1, interval=0.2, timeout=2, privileged=True)
    if result.is_alive:
        print(f" {host} is reachable, avg_rtt={result.avg_rtt:.2f} ms")
    else:
        print(f" {host} is not reachable")

if __name__== '__main__':
    main()