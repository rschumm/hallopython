import time
import os

import redis
from flask import Flask, render_template


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379, password=os.getenv('REDIS_PW'))


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                #raise exc
                return '4711 - no redis cache'
            retries -= 1
            time.sleep(0.5)


@app.route('/hello')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/graph')
def graf():
    text = Polyglot.eval('R',
    'svg();
     require(lattice);
     x <- 1:100
     y <- sin(x/10)
     z <- cos(x^1.3/(runif(1)*5+10))
     print(cloud(x~y*z, main="cloud plot"))
     grDevices:::svg.off()
    '
    ); 
    return text


@app.route('/')
def template():
    count = get_hit_count()
    #count = 1621
    return render_template('index.html', count=count)




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)