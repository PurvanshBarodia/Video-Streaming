from flask import Flask,jsonify,render_template,send_from_directory
from app import name_of_movie

app1 = Flask(__name__)



print(name_of_movie)
@app1.route('/',methods = ['GET'])
def render_temp():
	return render_template('index.html',name_of_movie=name_of_movie)
	
	
@app1.route('/fetch_name',methods = ['GET'])
def send_mov_name():
	res = {'url':'10.20.24.67:5000/'}
	return jsonify(res)
	
	
@app1.route('/videos/<filename>')
def get_video(filename):
	return send_from_directory('/home/s2vm2/Desktop/s2vm2_data/glusterfs/mount',filename)
	
	
if(__name__ == '__main__'):
	app1.run(debug = True, host = '0.0.0.0')
