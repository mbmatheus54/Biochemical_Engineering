class Version:
    VERSION = '1.0.0.0'
    CREATOR = {'Matheus Monteiro Batista': [ 'Brasil' , 'São Paulo' ]}
    Py_VERSION = '3.9'

    def __init__(self):
        self.version = Version.VERSION
        self.creator = "".join ( Version.CREATOR.keys ( ) )
        self.local = "".join (
            map ( str , [ [ ", ".join ( x[ i ] ) for x in Version.CREATOR.items ( ) ] for i in range ( 1 , 2 ) ] ) )[
                     2:-2 ]

        self.py_version = Version.Py_VERSION

    def __str__(self):
        return f'Versão: {self.version}\n' \
               f'Criadores: {self.creator}\n' \
               f'Local: {self.local}\n' \
               f'Python: {self.py_version}'
