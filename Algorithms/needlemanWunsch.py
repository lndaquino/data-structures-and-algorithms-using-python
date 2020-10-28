'''
alinhamento de sequencias - medir simularidade, medir diferenças, identidade
alinhamento global que compara a sequencia em toda sua extensão (proteinas, nucleotideos)
algoritmo que garante o ótimo a um custo alto, mas como são sequencias muito grandes pode tornar-se inviavel, dai aparecerem novas técnicas
algoritmo faz uso de uma matriz de pontuações (scores) para medir similaridade entre caracteres. Match (caracteres iguais), mismatch (caracteres diferentes) e gap penalty (penalidade por lacuna)
'''
import sys
#obtendo parâmetros da linha de comando

def needlemanWunsch(s1, s2, match, mismatch, gap):

  def max_valor(i, j):
    v1 = mat[i - 1][j - 1] + (match if s2[i - 1] == s1[j - 1] else mismatch) #diagonal superior esquerda
    v2 = mat[i-1][j] + gap #topo
    v3 = mat[i][j - 1] + gap #esquerda

    #calcula o valor máximo
    max_v = max([v1,v2,v3])

    #verifica o valor máximo
    if max_v == v1:
      traceback[(i,j)] = (i - 1, j - 1)
    elif max_v == v2:
      traceback[(i,j)] = (i - 1, j)
    else:
      traceback[(i,j)] = (i , j - 1)

    return max_v


  col, lin = len(s1) + 1, len(s2) + 1

  #cria a matriz
  mat = [[0 for i in range(col)] for i in range(lin)]

  #direções para construir o alinhamento
  traceback = {}

  #preenche o primeira linha e primeira coluna
  mat[0][0] = 0
  for i in range(1, col):
    mat[0][i] = mat[0][i - 1] + gap
    traceback[(0, i)] = (0, i - 1)
  for i in range(1, lin):
    mat[i][0] = mat[i - 1][0] + gap
    traceback[(i, 0)] = (i - 1, 0)

  #imprime traceback
  # print(str(traceback))
  for i in range(1, lin):
    for j in range(1, col):
      mat[i][j] = max_valor(i,j)
    
  s1_result, s2_result = '', '' #resultados do alinhamento
  i, j = lin - 1, col - 1 #inicia do último valor

  while True:
    i_next, j_next = traceback[(i,j)]

    if (i - 1) == i_next and (j - 1) == j_next: #diagonal
      s1_result += s1[j_next]
      s2_result += s2[i_next]
    if (i - 1) == i_next and j == j_next: #topo
      s1_result += '-'
      s2_result += s2[i_next]
    if i == i_next and (j - 1) == j_next: #esquerda
      s1_result += s1[j_next]
      s2_result += '-'

    i, j = i_next, j_next

    if not i and not j:
      break

    #inverte as strings, pois fizemos o caminho de trás pra frente no traceback
  s1_result, s2_result = s1_result[::-1], s2_result[::-1]

  print('{0}\n{1}'.format(s1_result, s2_result))

  






if __name__ == "__main__":
  #obtém a quantidade de argumentos passados
  len_args = len(sys.argv)

  #script s1 s2 match mismatch gap_penalty
  if len_args == 6:
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    match = sys.argv[3]
    mismatch = sys.argv[4]
    gap = sys.argv[5]
    needlemanWunsch(s1, s2, int(match), int(mismatch), int(gap))

  else:
    print('\nExecute:\n\tpython needlemanWunsch.py <sequence1> <sequence2> <match> <mismatch> <gap>')
    print('\nExample:\n\tpython needlemanWunsch.py GCATGCU GATTACA 1 -1 -1\n')


