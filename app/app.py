from flask import Flask, request, render_template
import redis

app = Flask(__name__)
default_key = '1'
cache = redis.StrictRedis(host='redis', port=6379, db=0) # 'redis' is container name
cache.set(default_key, "one") # use redis set api

@app.route('/', methods=['GET', 'POST'])
def mainpage():

	key = default_key
	if 'key' in request.form:
	    key = request.form['key']

	if request.method == 'POST' and request.form['submit'] == 'save':
		cache.set(key, request.form['cache_value'])

	cache_value = None;
        # key value lookup
        if cache.get(key):
		cache_value = cache.get(key).decode('utf-8') # use redis get api

	return render_template('index.html', key=key, cache_value=cache_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
