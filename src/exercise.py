from gauge import Gauge
def main():
    #write your code below this line
    g = Gauge(0)
    g.increase()
    print(g.value)
    pass

if __name__ == '__main__':
    main()
