from ..databases import db
# from datetime import datetime

class Denuncia(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    denuncia = db.Column(db.String(150), nullable=False)
    denunciante = db.Column(db.String(150))
    denunciante_endereco = db.Column(db.String(150))
    denunciante_telefone = db.Column(db.String(150))
    forma_recebimento = db.Column(db.String(150))
    situacao = db.Column(db.String(150), nullable=False)
    # criado_em = db.Column(db.Datetime, default=datetime.utcnow)
    # atualizado_em = db.Column(db.Datetime)

    def __rpr__(self):
        return f'Denuncia {self.denuncia}'

db.create_all()
