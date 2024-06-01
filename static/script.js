function validateForm() {
    var requiredFields = [
        'produk_lengkap', 'harga_kualitas', 'staf_ramahan', 
        'proses_pembayaran', 'kecepatan_pengiriman', 
        'kepuasan_keseluruhan', 'rekomendasi', 'berbelanja_kembali'
    ];

    for (var i = 0; i < requiredFields.length; i++) {
        var radios = document.getElementsByName(requiredFields[i]);
        var isChecked = false;
        for (var j = 0; j < radios.length; j++) {
            if (radios[j].checked) {
                isChecked = true;
                break;
            }
        }
        if (!isChecked) {
            alert('Harap isi semua pertanyaan dengan bintang merah.');
            return false;
        }
    }
    return true;
}
