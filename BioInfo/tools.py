from collections import Counter

from BioInfo.dados import CATBOX , GCBOX , TATABOX , CODONS


def media(sequencia):
    """ gera a media de uma sequencia unica """
    tam = len ( list ( sequencia ) )

    taxa = Counter ( sequencia ).most_common ( )
    print ( )
    print ( "#######################################" )
    print ( "############### Média #################" )
    print ( "#######################################" )
    print ( f'Tamanho da sequencia: {tam}' )
    for p in taxa:
        p_taxa = (p[ 1 ] / tam) * 100
        print ( (" = ".join ( map ( str , p ) )) + f' unidades ------- {p_taxa.__round__ ( 2 )} %' )
    print ( "#######################################" )

    return ''


def split_list(lst , n):
    for i in range ( 0 , len ( lst ) , n ):
        yield lst[ i:i + n ]


def compara_med(*sequencias) -> str:
    """ gera a média para uma lista de sequencias """
    tam = len ( list ( sequencias ) )
    if tam > 1:
        for _ in range ( tam ):
            print ( '----------' * 20 )
            print ( f"Sequencia : '{sequencias[ _ ]}'" )
            media ( sequencias[ _ ] )
            print ( )
            print ( '----------' * 20 )
    else:
        media ( sequencias )

    return ''


def check_tam(sequencia):
    """
    Checa o tamanho das sequencias fornecidas

    :param sequencias: lista com diferentes sequências de DNA ou RNA
    :param exp: Se True : representação da comparação entre as sequencias, se False: Lista com o tamanho das sequencias
    :return:
    """
    tam_conj = len ( list ( sequencia ) )
    tam_seq = [ ]
    for _ in range ( tam_conj ):
        tam_seq.append ( len ( list ( sequencia[ _ ] ) ) )
    return f'Menor sequência - {min ( tam_seq )} bases' "\n" f'Maior sequência {max ( tam_seq )} bases'


def check_promoters(sequencia):
    tam = len ( list ( sequencia ) )
    if tam > 200:
        tam = 50
        half = int ( tam / 2 )
    else:
        half = int ( tam / 2 )

    # TATA-box
    print ( "*" * half , 'TATA-Box' , '*' * half )
    for x in TATABOX:
        if x in sequencia:
            print ( f'Sequência promotora: "{x}" -- posição: {sequencia.index ( x )}' )
        else:
            print ( f'Sequência promotora: "{x}" ausente' )

    # GC-box
    print ( "*" * (half + 1) , 'GC-Box' , '*' * (half + 1) )
    if GCBOX in sequencia:
        print ( f'Sequência promotora: "{GCBOX}" -- posição: {sequencia.index ( GCBOX )}' )
    else:
        print ( f'Sequência promotora: "{GCBOX}" ausente' )
        # CAT-box
    print ( "*" * half , 'CAT-Box' , '*' * (half + 1) )
    for x in CATBOX:
        if x in sequencia:
            print ( f'Sequência promotora: "{x}" -- posição: {sequencia.index ( x )}' )
        else:
            print ( f'Sequência promotora: "{x}" ausente' )
    print ( '*' * tam )
    return ""


def convert(sequencia):
    elementos = [ ]
    for i in sequencia:
        for key , item in CODONS.items():
            if item[ 1 ] == i:
                elementos.append ( key )
    for x in elementos:
        chaveamento = [ ]
        for key , item in CODONS.items ( ):
            if x == key:
                chaveamento.append ( [ x , item[ 1 ] ] )
                print ( chaveamento )
