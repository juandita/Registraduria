from models.votocandidato import Votocandidato
from repositorios.repositoriovotocandidato import repositoriovotocandidato
from repositorios.repositoriocandidato import repositoriocandidato
from repositorios.repositoriomesa import repositoriomesa

class controladorvotocandidato:
  def __init__(self):
    self.repo = repositoriovotocandidato()
    self.repo_mesa = repositoriomesa()
    self.repo_candidato = repositoriocandidato()

  #Listar
  def index(self):
    return self.repo.find_all()

  #Crear
  def create(self, info_votocandidato):

    #Validar que la mesa y el candidato existan en la base de datos

    nuevo_votocandidato = Votocandidato(info_votocandidato)
    return self.repo.save(nuevo_votocandidato)

  #Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  #Actualizar
  def update(self, id, info_votocandidato):
    votocandidato_actualizado = Votocandidato(info_votocandidato)
    return self.repo.update(id, votocandidato_actualizado)

  #delete
  def delete(self, id):
    return self.repo.delete(id)

  def find_by_candidato(self, id_candidato):
    votocandidato = self.repo.query({"id_candidato": id_candidato})
    for x in votocandidato:
      del x["id_candidato"]
      id_mesa = x["id_mesa"]
      del x["id_mesa"]
      x["mesa"] = self.repo_mesa.find_by_id(id_mesa)
    return votocandidato

  def find_by_mesa(self, id_mesa):
    votocandidato = self.repo.query({"id_mesa": id_mesa})
    for x in votocandidato:
      del x["id_mesa"]
      id_candidato = x["id_candidato"]
      del x["id_candidato"]
      x["candidato"] = self.repo_candidato.find_by_id(id_candidato)
    return votocandidato