from collections import namedtuple
import pandas as pd

class Info:
    """Stores the attributes to describe the information section of a tpl file as class attributes.

**Attributes**

- **version:** (str) Olga version with which the file was generated
- **input_file:** (str) Genkey file name binded to this tpl file
- **pvt_file:** (str) Fluid property file name
- **date:** (str) TPL file generation date
- **project:** (str) Project name
- **title:** (str) Simulation title name
- **author:** (str) Responsible for the simulation
- **network:** (int) If 1, is a pipeline, > 1, is a network
- **geometry:** (str) Unit for pipeline length
- **branch:** (str) Branch name
    """

    def __init__(self):

        self.version = None
        self.input_file = None
        self.pvt_file = None
        self.date = None
        self.project = None
        self.title = None
        self.author = None
        self.network = None
        self.geometry = None
        self.branch = None

    def set_info(self, file:str):
        """Set all info attributes of tpl file in each class attribute.

**Parameters**

- **file:** (str) raw tpl file as string.

**Attributes to set**

- **version:** (str) Olga version with which the file was generated
- **input_file:** (str) Genkey file name binded to this tpl file
- **pvt_file:** (str) Fluid property file name
- **date:** (str) TPL file generation date
- **project:** (str) Project name
- **title:** (str) Simulation title name
- **author:** (str) Responsible for the simulation
- **network:** (int) If 1, is a pipeline, > 1, is a network
- **geometry:** (str) Unit for pipeline length
- **branch:** (str) Branch name
        """
        pass

    def serialize(self):
        """Serializes all information attributes of the Olga file

**Returns**

- **attrs:** (dict) {
    'version': (str) Olga version with which the file was generated,
    'input_file': (str) Genkey file name binded to this tpl file,
    'pvt_file': (str) Fluid property file name,
    'date': (str) TPL file generation date,
    'project': (str) Project name,
    'title': (str) Simulation title name,
    'author': (str) Responsible for the simulation,
    'network': (int) If 1, is a pipeline, > 1, is a network,
    'geometry': (str) Unit for pipeline length,
    'branch': (str) Branch name
}
        """

        return {
            'version': self.version,
            'input_file': self.input_file,
            'pvt_file': self.pvt_file,
            'date': self.date,
            'project': self.project,
            'title': self.title,
            'author': self.author,
            'network': self.network,
            'geometry': self.geometry,
            'branch': self.branch
        }
    

class Profile(list):
    """Stores the attributes to describe the elevation profile section of a tpl file as class attributes.

**Attributes**

- **x:** (list) x coordinates values
- **y:** (list) y coordinates values
- **profile:** (list) (x, y) pair coordinates values
    """

    def __init__(self):

        self.__point = namedtuple("Point", "x y")
    
    def append(self, x:float, y:float):
        """Add point to profile list

**Parameters**

- **x:** (float) x coordinate
- **y:** (float) y coordinate
        """
        if isinstance(x, float) & isinstance(y, float):
            
            self.__point(x, y)
            super(Profile, self).append(self.__point)

    def set_profile(self, file:str):
        """Set elevation profile

**Parameters**

- **file:** (str) raw tpl file read
        """
        pass
    
    @property
    def x(self)->list:
        """X coordinates values
        """
        return [point.x for point in self]
    
    @property
    def y(self)->list:
        """Y coordinate values
        """
        return [point.y for point in self]
    
    @property
    def profile(self)->list:
        """(x, y) coordinates values
        """
        return [(point.x, point.y) for point in self]

    def serialize(self)->dict:
        """Serializes elevation profile of a tpl file

**Returns**

- **profile:** (dict) {
    'profile': list of tuples (x, y),
    'x': (list) x coordinates values,
    'y': (list) y coordinates values
}
        """
        return {
            'profile': self.profile,
            'x': self.x,
            'y': self.y
        }
    

class Data:
    """Stores Pandas DataFrame with variables values according Olga simulation

**Attributes**

- **df:** (pd.DataFrame Object) stores tabular data of variable according Olga simulation 
    """

    def __init__(self):

        self.__df = None

    def set_data(self, file:str):
        """Parses data section of a .tpl file into pandas DataFrame

**Parameters**

- **file:** (str) raw tpl file read
        """

        pass

    @property
    def df(self)->pd.DataFrame:
        """Pandas DataFrame
        """
        return self.__df

    def serialize(self)->dict:
        """Serializes pandas DataFrame to a python dictionary

**Returns**

- **df:** (dict) DataFrame serialized
        """
        return self.df.to_dict()


class TPL:
    """Data Structure to wrap all operations needed to parse .tpl files into Python.

**Attributes**

- **info:** (Info Object) Stores the attributes to describe the information section of a tpl file as class attributes.
    - **version:** (str) Olga version with which the file was generated
    - **input_file:** (str) Genkey file name binded to this tpl file
    - **pvt_file:** (str) Fluid property file name
    - **date:** (str) TPL file generation date
    - **project:** (str) Project name
    - **title:** (str) Simulation title name
    - **author:** (str) Responsible for the simulation
    - **network:** (int) If 1, is a pipeline, > 1, is a network
    - **geometry:** (str) Unit for pipeline length
    - **branch:** (str) Branch name

- **profile:** (Profile Object) Stores the attributes to describe the elevation profile section of a tpl file as class attributes.
    - **x:** (list) x coordinates values
    - **y:** (list) y coordinates values
    - **profile:** (list) (x, y) pair coordinates values

- **data:** (Data Object) Stores Pandas DataFrame with variables values according Olga simulation
    - **df:** (pd.DataFrame Object) stores tabular data of variable according Olga simulation
    """

    def __init__(self):

        self.info = Info()
        self.profile = Profile()
        self.data = Data()

    def set_info(self, file:str):
        """Sets all info attributes of tpl file in each class attribute.

**Parameters**

- **file:** (str) raw tpl file as string.

**Attributes to set**

- **version:** (str) Olga version with which the file was generated
- **input_file:** (str) Genkey file name binded to this tpl file
- **pvt_file:** (str) Fluid property file name
- **date:** (str) TPL file generation date
- **project:** (str) Project name
- **title:** (str) Simulation title name
- **author:** (str) Responsible for the simulation
- **network:** (int) If 1, is a pipeline, > 1, is a network
- **geometry:** (str) Unit for pipeline length
- **branch:** (str) Branch name
        """
        self.info.set_info(file)

    def set_profile(self, file:str):
        """Sets elevation profile

**Parameters**

- **file:** (str) raw tpl file read
        """
        self.profile.set_profile(file)

    def set_data(self, file:str):
        """Parses tabular time series data of a .tpl file into a Pandas DataFrame

**Parameters**

- **file:** (str) raw tpl file as string.
        """
        pass

    def read_raw_file(self, filepath:str)->str:
        """Parses .tpl files into a python string

**Parameters**

- **filepath:** (str) .tpl file location

**Returns**

- **file:** (str) 
        """
        with open(filepath, 'r') as file:
            
            raw_file = file.read()

        return raw_file
    
    def read(self, filepath:str):
        """Read .tpl file into a TPL Object Structure

**Parameters**

- **filepath:** (str) .tpl file location
        """
        pass
    
    @property
    def df(self)->pd.DataFrame:
        """Gets tabular time series data of a .tpl

**Returns**

- **df:** (pd.DataFrame Object)
        """
        return self.data.df

    def serialize(self)->dict:
        """Serializes TPL Object

**Returns**

- **tpl:** (dict) {
    'info': {
        'version': (str) Olga version with which the file was generated,
        'input_file': (str) Genkey file name binded to this tpl file,
        'pvt_file': (str) Fluid property file name,
        'date': (str) TPL file generation date,
        'project': (str) Project name,
        'title': (str) Simulation title name,
        'author': (str) Responsible for the simulation,
        'network': (int) If 1, is a pipeline, > 1, is a network,
        'geometry': (str) Unit for pipeline length,
        'branch': (str) Branch name
    },
    'profile': {
        'profile': list of tuples (x, y),
        'x': (list) x coordinates values,
        'y': (list) y coordinates values
    },
    'data': DataFrame serialized
}
        """
        return {
            'info': self.info.serialize(),
            'profile': self.profile.serialize(),
            'data': self.data.serialize()
        }