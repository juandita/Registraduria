from repositorios.interfacerepositorio import InterfaceRepository
from models.votopartido_politico import Votopartidopolitico
from repositorios.repositoriopartidopolitico import repositoriopartidopolitico
from repositorios.repositoriomesa import repositoriomesa

class repositoriovotoPP(InterfaceRepository[Votopartidopolitico]):

    def __init__(self):
        super().__init__()
        self.repo_dep = repositoriopartidopolitico()
        self.repo_mesa = repositoriomesa()

    def find_all(self):
        lista_votopartidopolitico = super().find_all()
        for x in lista_votopartidopolitico:
            id_partidopolitico= x["id_partido_politico"]
            del x["id_partido_politico"]
            x["partidopolitico"] = self.repo_dep.find_by_id(id_partidopolitico)
            id_mesa = x ["id_mesa"]
            x["mesa"] = self.repo_mesa.find_by_id(id_mesa)
        return lista_votopartidopolitico

    def find_by_id(self, id):
        partidopoliticos = super().find_by_id(id)
        id_partidopolitico = partidopoliticos["id_partido_politico"]
        del partidopoliticos["id_partido_politico"]
        partidopoliticos["partidopolitico"] = self.repo_dep.find_by_id(id_partidopolitico)
        return partidopoliticos