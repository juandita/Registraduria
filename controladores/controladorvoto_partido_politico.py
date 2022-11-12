from models.votopartido_politico import Votopartidopolitico
from repositorios.repositoriovotopartidopolitico import repositoriovotoPP
from repositorios.repositoriopartidopolitico import repositoriopartidopolitico
from repositorios.repositoriomesa import repositoriomesa

class controladorvotoPP:
  def __init__(self):
    self.repo = repositoriovotoPP()
    self.repo_PP = repositoriopartidopolitico()
    self.repo_mesa = repositoriomesa()

  #Listar
  def index(self):
    return self.repo.find_all()

  # Crear
  def create(self, info_votopartidopolitico):

    # Validar que la mesa y el partidopolitico existan en la base de datos

    nuevo_votopartidopolitico = Votopartidopolitico(info_votopartidopolitico)
    return self.repo.save(nuevo_votopartidopolitico)

  # Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  # Actualizar
  def update(self, id, info_votopartidopolitico):
    votopartidopolitico_actualizado = Votopartidopolitico(info_votopartidopolitico)
    return self.repo.update(id, votopartidopolitico_actualizado)

  # delete
  def delete(self, id):
    return self.repo.delete(id)

  def find_by_partidopolitico(self, id_partidopolitico):
    votopartidopolitico = self.repo.query({"id_partidopolitico": id_partidopolitico})
    for x in votopartidopolitico:
      del x["id_partidopolitico"]
      id_mesa = x["id_mesa"]
      del x["id_mesa"]
      x["mesa"] = self.repo_mesa.find_by_id(id_mesa)
    return votopartidopolitico

  def find_by_mesa(self, id_mesa):
    votopartidopolitico = self.repo.query({"id_mesa": id_mesa})
    for x in votopartidopolitico:
      del x["id_mesa"]
      id_partidopolitico = x["id_partidopolitico"]
      del x["id_partidopolitico"]
      x["partidopolitico"] = self.repo_PP.find_by_id(id_partidopolitico)
    return votopartidopolitico