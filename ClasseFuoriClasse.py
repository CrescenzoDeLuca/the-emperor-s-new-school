I=0
classi=[]

def Studente (Nome, Cognome, Classe, Matricola):
    Record=(Nome, Cognome, Classe, Matricola)
    return Record


Stu = input ('quanti studenti ci sono??--->')
Stu=int(Stu)


while I<Stu:
      print('inserire i dati del nuovo studente')
      Nome=input('nome studente= ')
      Cognome=input('Cognome studente= ')
      classe=input('classe studente=')
      Matricola=input('matricola studente=')
      M=0
      while M<I:
            if Matricola == Allievo[3]:
               print('Matricola gia esistente')
               Matricola=input('inserirne una diversa-->')
            M+=1
      Allievo= Studente(Nome, Cognome, classe, Matricola)
      classi.append(I)
      classi[I]=Allievo
      print('----------')
      I+=1
I=0
while I<Stu:
      print('Studente N°',I+1,'==',classi[I])
      I+=1      