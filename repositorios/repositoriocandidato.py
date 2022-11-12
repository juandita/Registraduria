from models.candidato import Candidato
from repositorios.interfacerepositorio import InterfaceRepository
from repositorios.repositoriopartidopolitico import repositoriopartidopolitico

class repositoriocandidato(InterfaceRepository[Candidato] ):

  def __init__(self):
    super().__init__()
    self.repo_par = repositoriopartidopolitico()

  def find_all(self):
    lista_candidato = super().find_all()
    for x in lista_candidato:
      id_par = x["id_partido_politico"]
      del x["id_partido_politico"]
      x["partido_politico"] = self.repo_par.find_by_id(id_par)
    return lista_candidato

  def find_by_id(self, id):
    candidato = super().find_by_id(id)
    id_par = candidato["id_partido_politico"]
    del candidato["id_partido_politico"]
    candidato["partido_politico"] = self.repo_par.find_by_id(id_par)
    return candidato