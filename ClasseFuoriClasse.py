I=0
classi=[]
class Classs:
      def __init__ (self, Nome, Cognome, Classe, Matricola):
          self.Record=(Nome, Cognome, Classe, Matricola)
     
      def get(self):
          return self.Record


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
            if Matricola == Allievo.Record[3]:
               print('Matricola gia esistente')
               Matricola=input('inserirne una diversa-->')
               M=0
            M+=1
      Allievo= Classs(Nome, Cognome, classe, Matricola)
      classi.append(Allievo)
      classi[I]=Allievo
      print('----------')
      I+=1
I=0
while I<Stu:
      print('Studente N°',I+1,'==',classi[I].Record)
      I+=1