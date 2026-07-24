from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        # هنا بيكمل باقي الكود الخاص بتحميل الفيديوهات بتاعك
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
