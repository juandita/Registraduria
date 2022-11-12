from models.votocandidato import Votocandidato
from repositorios.interfacerepositorio import InterfaceRepository
from repositorios.repositoriomesa import repositoriomesa
from repositorios.repositoriocandidato import repositoriocandidato

class repositoriovotocandidato(InterfaceRepository[Votocandidato]):

  def __init__(self):
    super().__init__()
    self.repo_mesa = repositoriomesa()
    self.repo_candidato = repositoriocandidato()

  def find_all(self):
    lista_votocandidato = super().find_all()
    for x in lista_votocandidato:
      id_candidato = x["id_candidato"]
      del x["id_candidato"]
      x["candidato"] = self.repo_candidato.find_by_id(id_candidato)
      id_mesa = x ["id_mesa"]
      x["mesa"] = self.repo_mesa.find_by_id(id_mesa)
    return lista_votocandidato

  def find_by_id(self, id):
    candidatos = super().find_by_id(id)
    id_candidato = candidatos["id_candidato"]
    del candidatos["id_candidato"]
    candidatos["candidato"] = self.repo_candidato.find_by_id(id_candidato)
    return candidatos