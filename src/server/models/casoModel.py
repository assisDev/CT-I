from databases.config import db

class Caso(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    caso = db.Column(db.String(150), nullable=False)
    n_sipia = db.Column(db.String(30))
    conselheiro = db.Column(db.String(150))
    local_guarda = db.Column(db.String(150))
    situacao = db.Column(db.String(150))
    data_transferencia = db.Column(db.DateTime)
    denuncia_id = db.Column(db.Integer, db.ForeignKey('denuncia.id'))
    denuncia = db.relationship('Caso', backref=db.backref('casos', lazy=True))
    # criado_em = db.Column(db.Datetime, default=datetime.utcnow)
    # atualizado_em = db.Column(db.Datetime)

    def __rpr__(self):
        return f'Caso {self.caso}'
    

db.create_all()
    