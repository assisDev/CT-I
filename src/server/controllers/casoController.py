from flask import Blueprint

caso = Blueprint('caso', __name__)

@caso.route('/')
def get():
    import services.casoServices as pasta
    pasta.get_all()
    return "respondi", 200

