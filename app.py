from flask import Flask, flash, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Dibutuhkan untuk menggunakan flash messages dan session

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        data = request.form.to_dict()

        # Check if any required field is empty
        required_fields = ['produk_lengkap', 'harga_kualitas', 'staf_ramahan', 'proses_pembayaran', 
                           'kecepatan_pengiriman', 'kepuasan_keseluruhan', 'rekomendasi', 'berbelanja_kembali']
        
        for field in required_fields:
            if not data.get(field):
                flash('Semua kolom wajib diisi kecuali kolom komentar.')
                return redirect(url_for('survey'))

        feedback, is_happy, satisfaction_percentage = process_survey(data)
        
        # Simpan hasil survey dalam session
        session['feedback'] = feedback
        session['is_happy'] = is_happy
        session['satisfaction_percentage'] = satisfaction_percentage

        return redirect(url_for('thank_you'))
    
    return render_template('survey.html')

def process_survey(data):
    feedback = []
    negative_feedback_count = 0
    total_questions = 8
    
    # Forward chaining logic
    produk_lengkap = int(data.get('produk_lengkap', 0))
    if produk_lengkap <= 2:
        feedback.append("Perlu peningkatan dalam kelengkapan produk.")
        negative_feedback_count += 1
        
    harga_kualitas = int(data.get('harga_kualitas', 0))
    if harga_kualitas <= 2:
        feedback.append("Perlu peningkatan dalam keseimbangan harga dan kualitas.")
        negative_feedback_count += 1
        
    staf_ramahan = int(data.get('staf_ramahan', 0))
    if staf_ramahan <= 2:
        feedback.append("Perlu peningkatan dalam keramahan dan bantuan staf.")
        negative_feedback_count += 1
        
    proses_pembayaran = int(data.get('proses_pembayaran', 0))
    if proses_pembayaran <= 2:
        feedback.append("Perlu peningkatan dalam kemudahan proses pembayaran.")
        negative_feedback_count += 1
        
    kecepatan_pengiriman = int(data.get('kecepatan_pengiriman', 0))
    if kecepatan_pengiriman <= 2:
        feedback.append("Perlu peningkatan dalam kecepatan pengiriman produk.")
        negative_feedback_count += 1
        
    kepuasan_keseluruhan = int(data.get('kepuasan_keseluruhan', 0))
    if kepuasan_keseluruhan <= 2:
        feedback.append("Pengalaman berbelanja perlu diperbaiki secara keseluruhan.")
        negative_feedback_count += 1
        
    rekomendasi = int(data.get('rekomendasi', 0))
    if rekomendasi <= 2:
        feedback.append("Tingkat rekomendasi rendah, perlu ditingkatkan.")
        negative_feedback_count += 1
        
    berbelanja_kembali = int(data.get('berbelanja_kembali', 0))
    if berbelanja_kembali <= 2:
        feedback.append("Tingkat keinginan berbelanja kembali rendah, perlu ditingkatkan.")
        negative_feedback_count += 1

    if not feedback:
        feedback.append("Terima kasih atas penilaian positif Anda!")

    is_happy = negative_feedback_count < 4  # Misalnya, jika kurang dari 4 feedback negatif, pengguna dianggap senang.
    
    satisfaction_percentage = ((total_questions - negative_feedback_count) / total_questions) * 100

    return feedback, is_happy, satisfaction_percentage

@app.route('/thank-you', methods=['GET'])
def thank_you():
    feedback = session.get('feedback', [])
    is_happy = session.get('is_happy', False)
    satisfaction_percentage = session.get('satisfaction_percentage', 0)
    return render_template('thank_you.html', feedback=feedback, is_happy=is_happy, satisfaction_percentage=satisfaction_percentage)

@app.route('/lokasi')
def lokasi():
    return render_template('lokasi.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)
