from databases import db

class Familia(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genitor = db.Column(db.String(150))
    genitora = db.Column(db.String(150))
    responsavel = db.Column(db.String(150))
    # criado_em = db.Column(db.Datetime, default=datetime.utcnow)
    # atualizado_em = db.Column(db.Datetime)

    def __rpr__(self):
        return f'Familia {self.responsavel}'
