import random
import typing as ty

from BioInfo.dados import CODONS
from BioInfo.tools import split_list , media


class SeqTest:
    """
    Imprime uma sequencia genérica
    """
    pos = 0

    def __init__(self , sequencia: str = '' , ID: ty.Union[ str , int ] = "" , data: str = "dd/mm/YYYY" , autor=[ ]):
        self.__posicao = SeqTest.pos + 1
        self.__sequencia = sequencia
        self.__ID = ID
        if data != "dd/mm/YYYY":
            self.__data = f"{data[ 0:2 ]}/{data[ 2:4 ]}/{data[ 4:: ]}"
        else:
            self.__data = data
        self.__autor = ", ".join ( autor )
        SeqTest.pos = self.__posicao

    def __str__(self):
        return f'Nome: {self.__sequencia}\n' \
               f"pos: {self.__posicao}\n" \
               f'ID: {self.__ID}\n' \
               f'Data de criação: {self.__data}\n' \
               f'Autores: {self.__autor}'


def ret_exp_dna(length):
    new_seq = [ ]
    for x in range ( length ):
        new_seq.append ( random.choice ( [ 'A' , 'C' , 'G' , 'T' ] ) )

    return (x for x in split_list ( lst="".join ( map ( str , new_seq ) ) , n=10 ))


def ret_exp_rna(length):
    new_seq = [ ]
    for x in range ( length ):
        new_seq.append ( random.choice ( [ 'A' , 'C' , 'G' , 'T' , 'U' ] ) )

    return (x for x in split_list ( lst="".join ( map ( str , new_seq ) ) , n=10 ))


def replicacao(sequencia , taxa=False , tam=True):
    """
    :param sequencia: informe a sequencia da fita a ser codificada de DNA
    :param RNA: informe True para se obter uma fita de RNA
    :return: fita complementar
    """

    global _reversa
    if tam:
        try:
            print ( '-' * len ( sequencia ) )
            print ( f'total de aminoácidos: {len ( sequencia )} ' )
            print ( '-' * len ( sequencia ) )
        except TypeError:
            print ( '-' * len ( list ( sequencia ) ) )
            print ( f'total de aminoácidos: {len ( list ( sequencia ) )} ' )
            print ( '-' * len ( list ( sequencia ) ) )

    fita = [ ]
    # verifica as bases da fita principal e decodifica para formar a fita complementar
    for base in sequencia:
        if base == "A":
            base = 'T'
            fita.append ( base )
        elif base == 'T':
            base = 'A'
            fita.append ( base )
        elif base == 'C':
            base = 'G'
            fita.append ( base )
        elif base == 'G':
            base = 'C'
            fita.append ( base )
        elif base == 'U':
            base = 'A'
            fita.append ( base )

    print ( f"Fita paralela: 5' - {sequencia} - 3'" )
    reversa = list ( split_list ( lst=fita , n=len ( fita ) ) )
    for g in reversa:
        _reversa = ("".join ( map ( str , g ) ))
    print ( f"Fita Antiparalela: 3' - {_reversa} - 5'" )

    if taxa is True:
        media ( sequencia )

def trancricao(sequencia):
        global _transcrita

        fita = [ ]
        # verifica as bases da fita principal e decodifica para formar a fita complementar
        for base in sequencia:
            if base == "A":
                base = 'U'
                fita.append ( base )
            elif base == 'T':
                base = 'A'
                fita.append ( base )
            elif base == 'C':
                base = 'G'
                fita.append ( base )
            elif base == 'G':
                base = 'C'
                fita.append ( base )
            elif base == 'U':
                base = 'A'
                fita.append ( base )
        print ( f"Fita paralela: 5' - {sequencia} - 3'" )
        transcrita = list (split_list ( fita , len ( fita ) ) )
        for g in transcrita:
            _transcrita = ("".join ( map ( str , g ) ))
        print ( f"RNA: 5' - {_transcrita} - 3'" )

        # separa a lista de bases geradas por trinca de códons
        n = 3
        saida = list (split_list ( lst=fita , n=n ) )
        for p in saida:
            item = ("".join ( map ( str , p ) ))
            if item in CODONS.keys ( ):
                print ( f'{item} - {CODONS[ item ][ 0 ]}' )

