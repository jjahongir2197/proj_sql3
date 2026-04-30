from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite database sozlash
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///xodimlar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Xodimlar modeli
class Xodim(db.Model):
    __tablename__ = "xodimlar"

    id = db.Column(db.Integer, primary_key=True)
    ism = db.Column(db.String(50), nullable=False)
    familiya = db.Column(db.String(50), nullable=False)
    tugilgan_sana = db.Column(db.String(20))
    lavozim = db.Column(db.String(50))
    bolim = db.Column(db.String(50))
    telefon = db.Column(db.String(20))
    email = db.Column(db.String(100))
    ish_haqi = db.Column(db.Integer)
    ishga_kirgan_sana = db.Column(db.String(20))

# Database yaratish va ma'lumot qo‘shish
with app.app_context():
    db.create_all()

    # Agar jadval bo‘sh bo‘lsa ma'lumot qo‘shamiz
    if Xodim.query.count() == 0:

        x1 = Xodim(
            ism="Ali",
            familiya="Karimov",
            tugilgan_sana="1995-04-12",
            lavozim="Dasturchi",
            bolim="IT",
            telefon="+998901112233",
            email="ali@gmail.com",
            ish_haqi=1200,
            ishga_kirgan_sana="2022-03-01"
        )

        x2 = Xodim(
            ism="Madina",
            familiya="Qodirova",
            tugilgan_sana="1998-08-20",
            lavozim="Dizayner",
            bolim="Marketing",
            telefon="+998901234567",
            email="madina@gmail.com",
            ish_haqi=900,
            ishga_kirgan_sana="2023-01-10"
        )

        x3 = Xodim(
            ism="Bekzod",
            familiya="Rasulov",
            tugilgan_sana="1993-11-05",
            lavozim="Menejer",
            bolim="Savdo",
            telefon="+998909876543",
            email="bekzod@gmail.com",
            ish_haqi=1500,
            ishga_kirgan_sana="2021-06-15"
        )

        x4 = Xodim(
            ism="Aziza",
            familiya="Tursunova",
            tugilgan_sana="1997-02-18",
            lavozim="Buxgalter",
            bolim="Moliya",
            telefon="+998935551122",
            email="aziza@gmail.com",
            ish_haqi=1100,
            ishga_kirgan_sana="2022-09-20"
        )

        x5 = Xodim(
            ism="Javlon",
            familiya="Sobirov",
            tugilgan_sana="1994-07-30",
            lavozim="Tizim admini",
            bolim="IT",
            telefon="+998931234111",
            email="javlon@gmail.com",
            ish_haqi=1300,
            ishga_kirgan_sana="2020-11-05"
        )

        db.session.add_all([x1, x2, x3, x4, x5])
        db.session.commit()

@app.route("/")
def index():
    xodimlar = Xodim.query.all()

    result = ""

    for x in xodimlar:
        result += f"""
        {x.id} | {x.ism} | {x.familiya} | {x.tugilgan_sana} |
        {x.lavozim} | {x.bolim} | {x.telefon} |
        {x.email} | {x.ish_haqi} | {x.ishga_kirgan_sana}
        <br>
        """

    return result


if __name__ == "__main__":
    app.run(debug=True)
