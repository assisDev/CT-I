from databases.config import db
# from datetime import datetime

class Crianca(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    # data_nascimento = db.Column(db.Datetime)
    endereço = db.Column(db.String(150))
    telefone = db.Column(db.String(150))
    denuncia_id = db.Column(db.Integer, db.ForeignKey('denuncia.id'))
    denuncia = db.relationship('Denuncia', backref=db.backref('criancas', lazy=True))
    familia_id = db.Column(db.Integer, db.ForeignKey('familia.id'))
    familia = db.relationship('Familia', backref=db.backref('crincas', lazy=True))
    # criado_em = db.Column(db.Datetime, default=datetime.utcnow)
    # atualizado_em = db.Column(db.Datetime)

    def __rpr__(self):
        return f'Crianca {self.nome}'

db.create_all()
