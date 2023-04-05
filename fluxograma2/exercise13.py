# 13)Em uma eleição sindical concorreram ao cargo de presidente três candidados (A, B e C).
#    Escreva um algoritmo em FLUXOGRAMA que solicite a quantidade de votos de cada candidato,
#    a quantidade de votos nulos e votos em branco. Calcule o percentual DE CADA CANDIDATO em relação ao total de votos válidos. 
#    E o percentual de votos nulos e votos em branco do total geral de votos.


print("Let's calculate the percentual of votes, null votes or abstained votes")

print("Type how many votes were registered for the candidate A:")
firstCandidateVotes = int(input())

print("Type how many votes were registered for the candidate B:")
secondCandidateVotes = int(input())

print("Type how many votes were registered for the candidate C:")
thirdCandidateVotes = int(input())

print("Type how many votes were registered for null votes:")
nullVotes = int(input())

print("Type how many votes were registered for abstained votes:")
abstainedVotes = int(input())

validVotes = firstCandidateVotes + secondCandidateVotes + thirdCandidateVotes

totalVotes = firstCandidateVotes + secondCandidateVotes + thirdCandidateVotes + nullVotes + abstainedVotes

percFirstCandidateVotes = (firstCandidateVotes * 100) / validVotes

percSecondCandidateVotes = (secondCandidateVotes * 100) / validVotes

percthirdVotes = (thirdCandidateVotes * 100) / validVotes

percNullVotes = (nullVotes * 100) / totalVotes

percAbstainedVotes = (abstainedVotes * 100) / totalVotes


