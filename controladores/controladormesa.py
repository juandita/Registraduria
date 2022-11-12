from models.mesa import Mesa
from repositorios.repositoriomesa import repositoriomesa

class controladormesa:
  def __init__(self):
    self.repo = repositoriomesa()

  #Listar
  def index(self):
    return self.repo.find_all()

  #Crear
  def create(self, info_mesa):
    nuevo_mesa = Mesa(info_mesa)
    return self.repo.save(nuevo_mesa)

  #Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  #Actualizar
  def update(self, id, info_mesa):
    mesa_actualizado = Mesa(info_mesa)
    return self.repo.update(id, mesa_actualizado)

  #delete
  def delete(self, id):
    return self.repo.delete(id)

