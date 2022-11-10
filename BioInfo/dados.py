CODONS = {
    'UUU': [ 'FENILALANINA' , 'F' , 'codify' ] ,
    'UUC': [ 'FENILALANINA' , 'F' , 'codify' ] ,
    'UUG': [ 'LEUCINA' , 'L' , 'codify' ] ,
    'CUU': [ 'LEUCINA' , 'L' , 'codify' ] ,
    'CUC': [ 'LEUCINA' , 'L' , 'codify' ] ,
    'CUA': [ 'LEUCINA' , 'L' , 'codify' ] ,
    'CUG': [ 'LEUCINA' , 'L' , 'codify' ] ,
    'UUA': [ 'LEUCINA' , 'L' , 'codify' ] ,
    'AUU': [ 'ISOLEUCINA' , 'I' , 'codify' ] ,
    'AUC': [ 'ISOLEUCINA' , 'I' , 'codify' ] ,
    'AUA': [ 'ISOLEUCINA' , 'I' , 'codify' ] ,
    'AUG': [ 'METIONINA' , 'M' , 'start_codify' ] ,
    'GUU': [ 'VALINA' , 'V' , 'codify' ] ,
    'GUC': [ 'VALINA' , 'V' , 'codify' ] ,
    'GUA': [ 'VALINA' , 'V' , 'codify' ] ,
    'GUG': [ 'VALINA' , 'V' , 'codify' ] ,
    'UCU': [ 'SERINA' , 'S' , 'codify' ] ,
    'UCC': [ 'SERINA' , 'S' , 'codify' ] ,
    'UCA': [ 'SERINA' , 'S' , 'codify' ] ,
    'UCG': [ 'SERINA' , 'S' , 'codify' ] ,
    'CCU': [ 'PROLINA' , 'P' , 'codify' ] ,
    'CCC': [ 'PROLINA' , 'P' , 'codify' ] ,
    'CCA': [ 'PROLINA' , 'P' , 'codify' ] ,
    'CCG': [ 'PROLINA' , 'P' , 'codify' ] ,
    'ACU': [ 'TREONINA' , 'T' , 'codify' ] ,
    'ACC': [ 'TREONINA' , 'T' , 'codify' ] ,
    'ACA': [ 'TREONINA' , 'T' , 'codify' ] ,
    'ACG': [ 'TREONINA' , 'T' , 'codify' ] ,
    'GCU': [ 'ALANINA' , 'A' , 'codify' ] ,
    'GCC': [ 'ALANINA' , 'A' , 'codify' ] ,
    'GCA': [ 'ALANINA' , 'A' , 'codify' ] ,
    'GCG': [ 'ALANINA' , 'A' , 'codify' ] ,
    'UAU': [ 'TIROSINA' , 'Y' , 'codify' ] ,
    'UAC': [ 'TIROSINA' , 'Y' , 'codify' ] ,
    'UAA': [ 'STOP-CODON' , 'NON-codify' ] ,
    'UAG': [ 'STOP-CODON' , 'NON-codify' ] ,
    'UGA': [ 'STOP-CODON' , 'NON-codify' ] ,
    'CAU': [ 'HISTIDINA' , 'H' , 'codify' ] ,
    'CAC': [ 'HISTIDINA' , 'H' , 'codify' ] ,
    'CAA': [ 'GLUTAMINA' , 'Q' , 'codify' ] ,
    'CAG': [ 'GLUTAMINA' , 'Q' , 'codify' ] ,
    'AAU': [ 'ASPARAGINA' , 'N' , 'codify' ] ,
    'AAC': [ 'ASPARAGINA' , 'N' , 'codify' ] ,
    'AAA': [ 'LISINA' , 'K' , 'codify' ] ,
    'AAG': [ 'LISINA' , 'K' , 'codify' ] ,
    'GAU': [ 'ÁCIDO ASPÁRTICO' , 'D' , 'codify' ] ,
    'GAC': [ 'ÁCIDO ASPÁRTICO' , 'D' , 'codify' ] ,
    'GAA': [ 'ÁCIDO GLUTÂMICO' , 'E' , 'codify' ] ,
    'GAG': [ 'ÁCIDO GLUTÂMICO' , 'E' , 'codify' ] ,
    'UGU': [ 'CISTEÍNA' , 'C' , 'codify' ] ,
    'UGC': [ 'CISTEÍNA' , 'C' , 'codify' ] ,
    'CGU': [ 'ARGININA' , 'R' , 'codify' ] ,
    'CGC': [ 'ARGININA' , 'R' , 'codify' ] ,
    'CGA': [ 'ARGININA' , 'R' , 'codify' ] ,
    'CGG': [ 'ARGININA' , 'R' , 'codify' ] ,
    'AGU': [ 'SERINA' , 'S' , 'codify' ] ,
    'AGC': [ 'SERINA' , 'S' , 'codify' ] ,
    'AGA': [ 'ARGININA' , 'R' , 'codify' ] ,
    'AGG': [ 'ARGININA' , 'R' , 'codify' ] ,
    'GGU': [ 'GLICINA' , 'G' , 'codify' ] ,
    'GGC': [ 'GLICINA' , 'G' , 'codify' ] ,
    'GGA': [ 'GLICINA' , 'G' , 'codify' ] ,
    'GGG': [ 'GLICINA' , 'G' , 'codify' ] ,
    'UGG': [ 'TRIPTOFANO' , 'W' , 'codify' ]
}
TATABOX = 'TATAAAA' , 'TATAAAT' , 'TATATAA' , 'TATATAT'
GCBOX = 'GGGCGG'
CATBOX = 'TGATTGGTTA' , 'TGATTGGTTG' , 'TGATTGGCTA' , 'TGATTGGCTG' , 'TGATTGGCCA' , 'TGATTGGCCG' , 'TGATTGGTCA' , 'TGATTGGTCG'

