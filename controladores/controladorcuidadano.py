from models.cuidadano import Cuidadano
from repositorios.repositoriocuidadano import InterfaceRepository

class controladorcuidadano:
  def __init__(self):
    self.repo = InterfaceRepository()

  #Listar
  def index(self):
    return self.repo.find_all()

  #Crear
  def create(self, info_cuidadano):
    nuevo_cuidadano = Cuidadano(info_cuidadano)
    return self.repo.save(nuevo_cuidadano)

  #Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  #Actualizar
  def update(self, id, info_cuidadano):
    cuidadano_actualizado = Cuidadano(info_cuidadano)
    return self.repo.update(id, cuidadano_actualizado)

  #delete
  def delete(self, id):
    return self.repo.delete(id)