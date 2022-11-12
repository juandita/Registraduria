from models.partidopolitico import Partidopolitico
from repositorios.repositoriopartidopolitico import repositoriopartidopolitico

class controladorpartidopolitico:
  def __init__(self):
    self.repo = repositoriopartidopolitico()

  #Listar
  def index(self):
    return self.repo.find_all()

  #Crear
  def create(self, info_partidopolitico):
    nuevo_partidopolitico = Partidopolitico(info_partidopolitico)
    return self.repo.save(nuevo_partidopolitico)

  #Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  #Actualizar
  def update(self, id, info_partidopolitico):
    partidopolitico_actualizado = Partidopolitico(info_partidopolitico)
    return self.repo.update(id, partidopolitico_actualizado)

  #delete
  def delete(self, id):
    return self.repo.delete(id)