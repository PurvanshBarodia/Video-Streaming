from flask import Flask, render_template, request, jsonify,redirect
import sqlite3
import requests
import asyncio
app = Flask(__name__)
selected_movie = None

# List of available servers
servers = ["http://10.20.24.67:5000","http://10.20.24.69:5000"]
current_server_index = 0

def get_movies():
    conn = sqlite3.connect('movies.db')  # Replace 'movies.db' with your SQLite database file
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies')
    movies = cursor.fetchall()
    for movie in movies:
        print(movie)

    conn.close()
    return movies

@app.route('/')
def index():
    movies = get_movies()
    return render_template('index.html', movies=movies)

@app.route('/movie_page')
def page():
    return render_template('page.html' )
from flask import jsonify

@app.route('/get-movie-name/', methods=['GET'])
def play_movie():
    global current_server_index
    global selected_movie
    if request.args.get('movie'):
        selected_movie = request.args.get('movie')

        # Now you can use the selected_movie variable in your function
    result = {'name': selected_movie}

        # Find the next available server in a round-robin fashion
    current_server = servers[current_server_index]
    current_server_index = (current_server_index + 1) % len(servers)
        
    result['server'] = current_server

    return jsonify(result)


@app.route('/movie',methods = ['GET'])      
def play_mov():
    response = requests.get("http://10.20.24.67:5000/fetch_name")
    num = 1
    if num == 1:
        print(response.json()['url'])
        num += 1
        return redirect(f"http://{response.json()['url']}")
    
    
    elif num == 2:
        response = requests.get("http://10.20.24.61:5000/fetch_name")
        print("2")
        num += 1
        return response.json()
    
    
    elif num==3:
        response = requests.get("http://10.20.24.40:5000/fetch_name")
        print("3")
        num += 1
        return response.json()
    
    
    elif num == 4:
        response = requests.get("http://10.20.24.69:5000/fetch_name")
        print("4")
        num = 1
        return response.json()
    else:
        print("ERROR")
        return None

    url = response.json()['url']
    print(url)

         
	# recv = request.get('http://10.20.24.54:5000/fetch_name')
	

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')






















# from flask import Flask, render_template, jsonify, request
# import os

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'mp4'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_movie_details')
# def get_movie_details():
#     # Replace this with your movie details retrieval logic
#     # Assuming the other device has a web server serving the video
#     other_device_ip = '10.20.24.67'  # Replace with the actual IP address
#     video_url = f'http://{other_device_ip}/home/s2vm2/Desktop/s2vm2_data/glusterfs/mount/new.mp4'

#     movie_details = {
#         'title': 'Sample Movie',
#         'video_url': video_url,
#     }
#     return jsonify(movie_details)

# @app.route('/upload_video', methods=['POST'])
# def upload_video():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})

#     file = request.files['file']

#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})

#     if file and allowed_file(file.filename):
#         filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filename)
#         return jsonify({'success': True, 'message': 'File uploaded successfully'})

#     return jsonify({'error': 'Invalid file type'})

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')









# from flask import Flask, render_template, jsonify

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_movie_details')
# def get_movie_details():
#     # Replace this with your movie details retrieval logic
#     movie_details = {
#         'title': 'Sample Movie',
#         'video_url': 'http://10.20.24.61/home/s1vm1/Desktop/s1vm1_data/glusterfs/mount/new.mp4',  # Path to your video file
#     }
#     return jsonify(movie_details)

# if __name__ == '__main__':
#     app.run(debug=True, host = '0.0.0.0')
