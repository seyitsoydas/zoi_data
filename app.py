from flask import Flask, render_template

app = Flask(__name__)

# 1. Ana Sayfa
@app.route('/')
def home():
    return render_template('home.html')

# 2. Yapay Zeka ve Makine Öğrenimi
@app.route('/solutions/ai-ml')
def ai_ml():
    return render_template('ai_ml.html')

# 3. Görüntü İşleme
@app.route('/solutions/computer-vision')
def computer_vision():
    return render_template('image_processing.html')

# 4. Sinyal İşleme
@app.route('/solutions/signal-processing')
def signal_processing():
    return render_template('signal_processing.html')

# 5. E-Ticaret ve Perakende AI
@app.route('/solutions/ecommerce')
def ecommerce():
    return render_template('ecommerce.html')

# 6. Ar-Ge ve İnovasyon
@app.route('/services/rd-innovation')
def rd_innovation():
    return render_template('rd_innovation.html')

# 7. Veri Bilimi Danışmanlığı
@app.route('/services/data-science')
def data_science():
    return render_template('data_science.html')

# 8. Hakkımızda (YENİ)
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)