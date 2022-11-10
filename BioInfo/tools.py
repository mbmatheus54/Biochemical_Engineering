from collections import Counter

import pandas as pd


def media(sequencia):
    seq = "".join(map(str, sequencia))
    tam = len(seq)

    taxa = Counter ( seq).most_common ( )
    print ( )
    print ( "#######################################" )
    print ( "############### Média #################" )
    print ( "#######################################" )
    print(f'Tamanho da sequencia: {tam}')
    for p in taxa:
        p_taxa = (p[1] / tam) *100
        print ( (" = ".join ( map ( str , p ) )) + f' unidades ------- {p_taxa.__round__ ( 2 )} %' )
    print ( "#######################################" )
    return ''


def split_list(lst , n):
    for i in range ( 0 , len ( lst ) , n ):
        yield lst[ i:i + n ]

