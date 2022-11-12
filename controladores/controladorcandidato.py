from models.candidato import Candidato
from repositorios.repositoriocandidato import repositoriocandidato

class controladorcandidato:
  def __init__(self):
    self.repo = repositoriocandidato()

  #Listar
  def index(self):
    return self.repo.find_all()

  #Crear
  def create(self, info_candidato):
    nuevo_candidato = Candidato(info_candidato)
    return self.repo.save(nuevo_candidato)

  #Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  #Actualizar
  def update(self, id, info_candidato):
    candidato_actualizado = Candidato(info_candidato)
    return self.repo.update(id, candidato_actualizado)

  #delete
  def delete(self, id):
    return self.repo.delete(id)

  def find_by_partidopolitico(self, id_partido_politico):
    return self.repo.query({"id_partido_politico": id_partido_politico})

  def find_by_mesa(self, id_mesa):
    return self.repo.query({"id_mesa":id_mesa})

  def find_by_query(self, query):
    return self.repo.query(query)

  def find_by_aggregate(self, query):
    return self.repo.aggregate(query)