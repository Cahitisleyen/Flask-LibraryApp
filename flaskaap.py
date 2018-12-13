from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/yeni')
def yeni_kitap():
    return render_template('kitap.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            Kitap_ad = request.form['Kitap_ad']
            Kitap_yazar = request.form['Kitap_yazar']
            Kitap_yayinevi = request.form['Kitap_yayinevi']
            Kitap_sayfa = request.form['Kitap_sayfa']

            with sqlite3.connect("kutuphane.db") as con:
                conn = sqlite3.connect('kutuphane.db')
                cur = con.cursor()
                cur.execute("INSERT INTO kitaplar (Kitap_ad,Kitap_yazar,Kitap_yayinevi,Kitap_sayfa) VALUES(?, ?, ?, ?)",(Kitap_ad,Kitap_yazar,Kitap_yayinevi,Kitap_sayfa) )


                con.commit()
                conn.close()
                msg = ("Kayıt başarılı bir şekilde eklendi")
        except:
            con.rollback()
            msg = "Kayıt eklenmedi hata oluştu"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sqlite3.connect("kutuphane.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from kitaplar")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)