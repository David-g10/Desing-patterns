from enum import Enum
from abc import ABC, abstractmethod

class GetDataInterface(ABC):
    @abstractmethod
    def get_movies_list(self):
        pass

class GetDataUrl(GetDataInterface):
    
    def get_movies_list(self):
        #TODO conultar API/WEB
        movies_array = []
        movies_array.append("titanic")
        movies_array.append("avatar")
        movies_array.append("Terminator 2")
        return movies_array
    
class GetDataLocal(GetDataInterface):

    def get_movies_list(self):
        #TODO conultar BDD LOCAL
        movies_array = []
        movies_array.append("sirenita")
        movies_array.append("Tiburon")
        movies_array.append("megalodon")
        return movies_array 
    
class GetDataFirebase(GetDataInterface):
       
       def get_movies_list(self):
           movies_array = []
           movies_array.append("Screen")
           movies_array.append("Armaguedon")
           movies_array.append("Capitan america")
           return movies_array
        

class getDataType(Enum):
    getDataUrl = "URL"
    getDataLocal = "local"
    getDataFireBase = "Firebase"

class ViewModelListMovie:

    def __init__(self):
        print("se crea objeto viewModel")
    
    def get_movies_list(self, obj: GetDataInterface):
        return obj.get_movies_list()


class ViewListMovie:
    _getDataType = getDataType.getDataLocal.value
    _viewModel = ViewModelListMovie()

    def createdList(self, listMovies):
        #TODO create visual list
        print(listMovies)

    def getData(self):
        data = None
        objFirebase = GetDataFirebase()
        data = self._viewModel.get_movies_list(objFirebase)
        self.createdList(data)

obj = ViewListMovie()
obj.getData()