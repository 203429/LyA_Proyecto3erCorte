from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from turing_machine import TuringMachine
from automata.fa.dfa import DFA
from nltk import CFG
from nltk.parse.generate import generate
from nltk.corpus import words
import random

# Create your views here.

class Calculo(APIView):
    def createJson(self,message,data,status):
        custom={"messages":message,"Cardinalidad":data,"status":status}
        auxiliar=json.dumps(custom)
        responseOk=json.loads(auxiliar)
        return responseOk

    def get(self, request, format=None):
        responseOk=self.createJson("succes","202","funciona")
        return Response(responseOk)

    def post(self, request, format=None):
        serializer = request.data
        data = str(serializer)
        tam=14-len(data)
        data=(data[tam:])
        tam2=len(data)-2
        data=(data[:tam2])

        llaves = TuringMachine(
        {
            ('q0', '{'): ('q1', '*', 'R'), 
            ('q1', '{'): ('q1', '*', 'R'), ('q1', '}'): ('q1', '}', 'R'), ('q1', ''): ('q2', '', 'L'), 
            ('q2', '}'): ('q2', '}', 'L'), ('q2', '#'): ('q2', '#', 'L'), ('q2', '{'): ('q2', '{', 'L'), ('q2', ''): ('q6', '', 'R'), ('q2', '*'): ('q3', '{', 'R'), 
            ('q3', '*'): ('q3', '*', 'R'), ('q3', '{'): ('q3', '{', 'R'), ('q3', '}'): ('q3', '}', 'R'), ('q3', '#'): ('q3', '#', 'R'), ('q3', ''): ('q4', '', 'L'), 
            ('q4', '*'): ('q4', '*', 'L'), ('q4', '{'): ('q4', '{', 'L'), ('q4', '#'): ('q4', '#', 'L'), ('q4', '}'): ('q5', '#', 'R'), 
            ('q5', '*'): ('q5', '*', 'R'), ('q5', '{'): ('q5', '{', 'R'), ('q5', '#'): ('q5', '#', 'R'), ('q5', '}'): ('q5', '}', 'R'), ('q5', ''): ('q2', '', 'L'),
            ('q6', '*'): ('q6', '*', 'R'), ('q6', '{'): ('q6', '{', 'R'), ('q6', '#'): ('q6', '#', 'R'), ('q6', '}'): ('q8', '}', 'R'), ('q6', ''): ('q7', '', 'L'),
            ('q7', '*'): ('q7', '*', 'L'), ('q7', '{'): ('q7', '{', 'L'), ('q7', '#'): ('q7', '}', 'L'), ('q7', '}'): ('q7', '}', 'L'), ('q7', ''): ('qa', '', 'R'),  
        }
        )

        paren = TuringMachine(
        {
            ('q0', '('): ('q1', '*', 'R'), 
            ('q1', '('): ('q1', '*', 'R'), ('q1', ')'): ('q1', ')', 'R'), ('q1', ''): ('q2', '', 'L'), 
            ('q2', ')'): ('q2', ')', 'L'), ('q2', '#'): ('q2', '#', 'L'), ('q2', '('): ('q2', '(', 'L'), ('q2', ''): ('q6', '', 'R'), ('q2', '*'): ('q3', '(', 'R'), 
            ('q3', '*'): ('q3', '*', 'R'), ('q3', '('): ('q3', '(', 'R'), ('q3', ')'): ('q3', ')', 'R'), ('q3', '#'): ('q3', '#', 'R'), ('q3', ''): ('q4', '', 'L'), 
            ('q4', '*'): ('q4', '*', 'L'), ('q4', '('): ('q4', '(', 'L'), ('q4', '#'): ('q4', '#', 'L'), ('q4', ')'): ('q5', '#', 'R'), 
            ('q5', '*'): ('q5', '*', 'R'), ('q5', '('): ('q5', '(', 'R'), ('q5', '#'): ('q5', '#', 'R'), ('q5', ')'): ('q5', ')', 'R'), ('q5', ''): ('q2', '', 'L'),
            ('q6', '*'): ('q6', '*', 'R'), ('q6', '('): ('q6', '(', 'R'), ('q6', '#'): ('q6', '#', 'R'), ('q6', ')'): ('q8', ')', 'R'), ('q6', ''): ('q7', '', 'L'),
            ('q7', '*'): ('q7', '*', 'L'), ('q7', '('): ('q7', '(', 'L'), ('q7', '#'): ('q7', ')', 'L'), ('q7', ')'): ('q7', ')', 'L'), ('q7', ''): ('qa', '', 'R'),  
        }
        )

        dfa = DFA(
            states={'q0', 'q1', 'q2','q3','q4','q5','q6','q7'},
            input_symbols={
                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                '0','1','2','3','4','5','6','7','8','9',
                ' ','{','}','(',')',','
                },
            transitions={
                'q0': {'{': 'q1'},
                'q1': {' ': 'q1', '{': 'q1', '(':'q1', ')':'q5', '}':'q7',
                    'a':'q2','b':'q2','c':'q2','d':'q2','e':'q2','f':'q2','g':'q2','h':'q2','i':'q2','j':'q2','k':'q2','l':'q2','m':'q2','n':'q2','o':'q2','p':'q2','q':'q2','r':'q2','s':'q2','t':'q2','u':'q2','v':'q2','w':'q2','x':'q2','y':'q2','z':'q2',
                    'A':'q2','B':'q2','C':'q2','D':'q2','E':'q2','F':'q2','G':'q2','H':'q2','I':'q2','J':'q2','K':'q2','L':'q2','M':'q2','N':'q2','O':'q2','P':'q2','Q':'q2','R':'q2','S':'q2','T':'q2','U':'q2','V':'q2','W':'q2','X':'q2','Y':'q2','Z':'q2',
                    '0':'q2','1':'q2','2':'q2','3':'q2','4':'q2','5':'q2','6':'q2','7':'q2','8':'q2','9':'q2'
                    },
                'q2': {' ': 'q2', '}': 'q6', ')':'q3', ',':'q4', '{':'q1', '(':'q1',
                    'a':'q2','b':'q2','c':'q2','d':'q2','e':'q2','f':'q2','g':'q2','h':'q2','i':'q2','j':'q2','k':'q2','l':'q2','m':'q2','n':'q2','o':'q2','p':'q2','q':'q2','r':'q2','s':'q2','t':'q2','u':'q2','v':'q2','w':'q2','x':'q2','y':'q2','z':'q2',
                    'A':'q2','B':'q2','C':'q2','D':'q2','E':'q2','F':'q2','G':'q2','H':'q2','I':'q2','J':'q2','K':'q2','L':'q2','M':'q2','N':'q2','O':'q2','P':'q2','Q':'q2','R':'q2','S':'q2','T':'q2','U':'q2','V':'q2','W':'q2','X':'q2','Y':'q2','Z':'q2',
                    '0':'q2','1':'q2','2':'q2','3':'q2','4':'q2','5':'q2','6':'q2','7':'q2','8':'q2','9':'q2'
                    },
                'q3': {')':'q3', ',':'q2', ' ':'q3', '}':'q6'},
                'q4': {' ':'q4', '{':'q1', '(':'q1',
                    'a':'q2','b':'q2','c':'q2','d':'q2','e':'q2','f':'q2','g':'q2','h':'q2','i':'q2','j':'q2','k':'q2','l':'q2','m':'q2','n':'q2','o':'q2','p':'q2','q':'q2','r':'q2','s':'q2','t':'q2','u':'q2','v':'q2','w':'q2','x':'q2','y':'q2','z':'q2',
                    'A':'q2','B':'q2','C':'q2','D':'q2','E':'q2','F':'q2','G':'q2','H':'q2','I':'q2','J':'q2','K':'q2','L':'q2','M':'q2','N':'q2','O':'q2','P':'q2','Q':'q2','R':'q2','S':'q2','T':'q2','U':'q2','V':'q2','W':'q2','X':'q2','Y':'q2','Z':'q2',
                    '0':'q2','1':'q2','2':'q2','3':'q2','4':'q2','5':'q2','6':'q2','7':'q2','8':'q2','9':'q2'
                    },
                'q5': {')':'q5', ' ':'q5', '}':'q7'},
                'q6': {',':'q2', '}':'q6'},
                'q7': {',':'q1', '}':'q7'}
            },
            allow_partial=True,
            initial_state='q0',
            final_states={'q6','q7'}
        )

        resultante1 = ''
        resultante2 = ''
        aux=True
        for indice in range(len(data)):
            caracter = data[indice]
            if (caracter=='{' or caracter=='}'):
                resultante1 = resultante1 + caracter
                
        for indice2 in range(len(data)):
            caracter = data[indice2]
            if (caracter=='(' or caracter==')'):
                resultante2 = resultante2 + caracter
        if (len(resultante2)==0):
            aux=False

        if (llaves.accepts(resultante1) == True):
            if(aux==False):
                #return Response('Conjunto valido')
                if dfa.accepts_input(data):
                    #return Response('Conjunto valido')
                    pass
                    # responseOk=self.createJson("succes","202","Valido")
                    # return Response(responseOk)
                else:
                    #return Response('conjunto no valido')
                    responseOk=self.createJson("succes","202","No valido")
                    return Response(responseOk)
            else:
                if (paren.accepts(resultante2)==True):
                    #return Response('Conjunto valido')
                    if dfa.accepts_input(data):
                        # responseOk=self.createJson("succes","202","Valido")
                        # return Response(responseOk)
                        pass
                    else:
                        responseOk=self.createJson("succes","202","No valido")
                        return Response(responseOk)
                else:
                    print(resultante2)
                    responseOk=self.createJson("succes","202","No valido")
                    return Response(responseOk)
        else:
                responseOk=self.createJson("succes","202","No valido")
                return Response(responseOk)

        resultado=self.turing_M(
                    state = 'q0', # Estado inicial
                    blank = 'B', # El simbolo que representa blanco
                    tape = list(data), # cinta
                    final = 'q9',# Estado final
                    final2 = 'q6',

                    rules = map(tuple,
                    [
                        'q0 { {  right q1'.split(),
                        'q1 , , right q1'.split(),'q1 * * right q1'.split(),'q1 a a right q2'.split(),'q1 , , right q1'.split(),'q1 { { right q7'.split(),'q1 ( ( right q7'.split(), 'q1 b b right q2'.split(), 'q1 c c right q2'.split(),'q1 d d right q2'.split(),'q1 e e right q2'.split(),'q1 f f right q2'.split(),'q1 g g right q2'.split(),'q1 h h right q2'.split(),'q1 i i right q2'.split(),'q1 j j right q2'.split(),'q1 k k right q2'.split(),'q1 l l right q2'.split(),'q1 m m right q2'.split(),'q1 n n right q2'.split(),'q1 o o right q2'.split(),'q1 p p right q2'.split(),'q1 q q right q2'.split(),'q1 r r right q2'.split(),'q1 s s right q2'.split(),'q1 t t right q2'.split(),'q1 u u right q2'.split(),'q1 v v right q2'.split(),'q1 w w right q2'.split(),'q1 x x right q2'.split(),'q1 y y right q2'.split(),'q1 z z right q2'.split(),'q1 0 0 right q2'.split(),'q1 1 1 right q2'.split(),'q1 2 2 right q2'.split(),'q1 3 3 right q2'.split(),'q1 4 4 right q2'.split(),'q1 5 5 right q2'.split(),'q1 6 6 right q2'.split(),'q1 7 7 right q2'.split(),'q1 8 8 right q2'.split(),'q1 9 9 right q2'.split(), 'q1 } } right q9'.split(),
                        'q2 , , right q3'.split(), 'q2 } } right q3'.split(),
                        'q3 a a right q3'.split(), 'q3 b b right q3'.split(), 'q3 c c right q3'.split(), 'q3 , , right q3'.split(), 'q3 * * right q3'.split(), 'q3 ( ( right q3'.split(),'q3 ) ) right q3'.split(),'q3 { { right q3'.split(), 'q3 B B left q4'.split(), 'q3 } } right q3'.split(),'q3 E E right q4'.split(), 'q3 d d right q3'.split(), 'q3 e e right q3'.split(),'q3 f f right q3'.split(), 'q3 g g right q3'.split(),'q3 h h right q3'.split(),'q3 i i right q3'.split(),'q3 j j right q3'.split(),'q3 k k right q3'.split(),'q3 l l right q3'.split(),'q3 m m right q3'.split(),'q3 n n right q3'.split(),'q3 o o right q3'.split(),'q3 p p right q3'.split(),'q3 q q right q3'.split(),'q3 r r right q3'.split(),'q3 s s right q3'.split(),'q3 t t right q3'.split(),'q3 u u right q3'.split(),'q3 v v right q3'.split(),'q3 w w right q3'.split(),'q3 x x right q3'.split(),'q3 y y right q3'.split(),'q3 z z right q3'.split(),'q3 0 0 right q3'.split(),'q3 1 1 right q3'.split(),'q3 2 2 right q3'.split(),'q3 3 3 right q3'.split(),'q3 4 4 right q3'.split(),'q3 5 5 right q3'.split(),'q3 6 6 right q3'.split(),'q3 7 7 right q3'.split(),'q3 8 8 right q3'.split(),'q3 9 9 right q3'.split(),
                        'q4 1 1 left q4'.split(), 'q4 2 2 left q4'.split(), 'q4 3 3 left q4'.split(), 'q4 } } left q4'.split(), 'q4 * * left q4'.split(),'q4 ( ( left q4'.split(),'q4 ) ) left q4'.split(),'q4 , , left q4'.split(), 'q4 { { left q4'.split(), 'q4 0 0 left q4'.split(), 'q4 4 4 left q4'.split(), 'q4 5 5 left q4'.split(), 'q4 6 6 left q4'.split(), 'q4 7 7 left q4'.split(), 'q4 8 8 left q4'.split(), 'q4 9 9 left q4'.split(),'q4 a a left q4'.split(),'q4 b b left q4'.split(),'q4 c c left q4'.split(),'q4 d d left q4'.split(),'q4 e e left q4'.split(),'q4 f f left q4'.split(),'q4 g g left q4'.split(),'q4 h h left q4'.split(),'q4 i i left q4'.split(),'q4 j j left q4'.split(),'q4 k k left q4'.split(),'q4 l l left q4'.split(),'q4 m m left q4'.split(),'q4 n n left q4'.split(),'q4 o o left q4'.split(),'q4 p p left q4'.split(),'q4 q q left q4'.split(),'q4 r r left q4'.split(),'q4 s s left q4'.split(),'q4 t t left q4'.split(),'q4 u u left q4'.split(),'q4 v v left q4'.split(),'q4 w w left q4'.split(),'q4 x x left q4'.split(),'q4 y y left q4'.split(),'q4 z z left q4'.split(),
                        'q5 , , right q5'.split(),'q5 1 1 right q3'.split(), 'q5 2 2 right q3'.split(), 'q5 3 3 right q3'.split(),'q5 { { right q7'.split(), 'q5 } } right q6'.split(),'q5 ( ( right q7'.split(), 'q5 ) ) right q6'.split(),'q5 * * right q5'.split(),'q5 4 4 right q3'.split(),'q5 5 5 right q3'.split(),'q5 6 6 right q3'.split(),'q5 7 7 right q3'.split(),'q5 8 8 right q3'.split(),'q5 9 9 right q3'.split(),'q5 0 0 right q3'.split(),'q5 a a right q3'.split(),'q5 b b right q3'.split(),'q5 c c right q3'.split(),'q5 d d right q3'.split(),'q5 e e right q3'.split(),'q5 f f right q3'.split(),'q5 g g right q3'.split(),'q5 h h right q3'.split(),'q5 i u right q3'.split(),'q5 j j right q3'.split(),'q5 k k right q3'.split(),'q5 l l right q3'.split(),'q5 m m right q3'.split(),'q5 n n right q3'.split(),'q5 o o right q3'.split(),'q5 p p right q3'.split(),'q5 q q right q3'.split(),'q5 r r right q3'.split(),'q5 s s right q3'.split(),'q5 t t right q3'.split(),'q5 u u right q3'.split(),'q5 v v right q3'.split(),'q5 w w right q3'.split(),'q5 x x right q3'.split(),'q5 y y right q3'.split(),'q5 z z right q3'.split(),
                        'q7 , , right q7'.split(),'q7 * * right q7'.split(),'q7 1 1 right q7'.split(), 'q7 2 2 right q7'.split(), 'q7 3 3 right q7'.split(),'q7 ) ) right q8'.split(),'q7 ( ( right q10'.split(),'q7 } } right q8'.split(),'q7 { { right q10'.split(),'q7 4 4 right q7'.split(),'q7 5 5 right q7'.split(),'q7 6 6 right q7'.split(),'q7 7 7 right q7'.split(),'q7 8 8 right q7'.split(),'q7 9 9 right q7'.split(),'q7 a a right q7'.split(),'q7 b b right q7'.split(),'q7 c c right q7'.split(),'q7 d d right q7'.split(),'q7 e e right q7'.split(),'q7 f f right q7'.split(),'q7 g g right q7'.split(),'q7 h h right q7'.split(),'q7 i i right q7'.split(),'q7 j j right q7'.split(),'q7 k k right q7'.split(),'q7 l l right q7'.split(),'q7 m m right q7'.split(),'q7 n n right q7'.split(),'q7 o o right q7'.split(),'q7 p p right q7'.split(),'q7 q q right q7'.split(),'q7 r r right q7'.split(),'q7 s s right q7'.split(),'q7 t t right q7'.split(),'q7 u u right q7'.split(),'q7 v v right q7'.split(),'q7 w w right q7'.split(),'q7 x x right q7'.split(),'q7 y y right q7'.split(),'q7 z z right q7'.split(),
                        'q8 , , right q1'.split(),'q8 B B right q9'.split(), 'q8 } } right q8'.split(),'q8 * * right q8'.split(),'q8 ) ) right q8'.split(),
                        'q10 , , right q10'.split(),'q10 * * right q10'.split(),'q10 1 1 right q10'.split(), 'q10 2 2 right q10'.split(), 'q10 3 3 right q10'.split(), 'q10 ) ) right q7'.split(), 'q10 ( ( right q10'.split(),'q10 } } right q7'.split(), 'q10 { { right q10'.split(),'q10 4 4 right q10'.split(),'q10 5 5 right q10'.split(),'q10 6 6 right q10'.split(),'q10 7 7 right q10'.split(),'q10 8 8 right q10'.split(),'q10 9 9 right q10'.split(),'q10 0 0 right q10'.split(),'q10 0 0 right q10'.split(),'q10 a a right q10'.split(),'q10 b b right q10'.split(),'q10 c c right q10'.split(),'q10 d d right q10'.split(),'q10 f f right q10'.split(),'q10 g g right q10'.split(),'q10 h h right q10'.split(),'q10 i i right q10'.split(),'q10 j j right q10'.split(),'q10 k k right q10'.split(),'q10 l l right q10'.split(),'q10 m m right q10'.split(),'q10 n n right q10'.split(),'q10 o o right q10'.split(),'q10 p p right q10'.split(),'q10 q q right q10'.split(),'q10 r r right q10'.split(),'q10 s s right q10'.split(),'q10 t t right q10'.split(),'q10 u u right q10'.split(),'q10 v v right q10'.split(),'q10 w w right q10'.split(),'q10 x x right q10'.split(),'q10 y y right q10'.split(),'q10 z z right q10'.split(),


                    ], # reglas para las transiciones
                    ))
        responseOk=self.createJson("succes",resultado,"Valido")
        return Response(responseOk)
            

    def turing_M(
                self,
                state = None, # Los estados de la MT
                blank = None, # El simbolo que representa blanco
                rules = [], # reglas para las transiciones
                tape = [], # cinta
                final = None,# Estado final
                final2 = None,
                final3 = None,
                position = 0 #posicion del cabezal
                ):
        st = state
        if not tape: tape = [blank]
        if position < 0: position += len(tape)
        if position >= len(tape) or position < 0: raise Exception("Se inicializo mal la posicion")
        SV = ''
        rules = dict(((s0,v0),(v1,dr,s1)) for (s0,v0,v1,dr,s1) in rules)
        """
        Estado         Simbolo a leer       Simbolo a escribir       Mov     Sig. EStado
        q0(s0)            {(v0)                  {(v1)             D(dr)      q1(s1)
        """
        cardinalidad = 0
        while True:
        
            print(st,'\t', end = '  ')
            for i, v in enumerate(tape):
                if i == position:
                    print("[%s]"%(v,),end=" ")
                else: print (v, end=" ")
            print()
            print('valor de SV '+SV)

            if st == final2 or st == final3:
                if st == 'q9':
                    print('Cardinalidad = ',cardinalidad )
                if st == 'q6':
                    print('Cardinalidad = ',cardinalidad )

                break
            if (st, tape[position]) not in rules:
                print('no validado')
                break

            (v1,dr,s1) = rules[(st,tape[position])]

            if st == 'q3' and SV == v1:
                v1 = '*'
            if st == 'q4' and SV== v1:
                cardinalidad = cardinalidad+1
                s1 = 'q5'
                dr = 'right'
                print("Cardinalidad = ", cardinalidad)
            if st == 'q1' and v1 == '{':
                cardinalidad = cardinalidad+1
                print("Cardinalidad = ", cardinalidad)
            if st == 'q5' and v1 == '{':
                cardinalidad = cardinalidad+1
                print("Cardinalidad = ", cardinalidad)
            if st == 'q1' and v1 == '(':
                cardinalidad = cardinalidad+1
                print("Cardinalidad = ", cardinalidad)
            if st == 'q5' and v1 == '(':
                cardinalidad = cardinalidad+1
                print("Cardinalidad = ", cardinalidad)






            tape[position] = v1

            
            if st == 'q1' and (v1 =='{' or v1 =='(' or v1 =='a'  or  v1 =='b' or v1 =='c' or v1 =='d' or v1 =='e' or v1 =='f' or v1 =='g' or v1 =='h' or v1 =='i' or v1 =='j' or v1 =='k' or v1 =='l' or v1 =='m' or v1 =='n' or v1 =='o' or v1 =='p' or v1 =='q' or v1 =='r'or v1 =='s' or v1 =='t'or v1 =='u' or v1 =='v'or v1 =='w' or v1 =='x'or v1 =='y' or v1 =='z' or v1 =='0'or v1 =='1' or v1 =='2' or v1 =='3' or v1 =='4' or v1 =='5' or  v1 =='6'or v1 =='7' or v1 =='8' or v1 =='9'):
                SV = v1
            if st == 'q5' and (v1 =='{' or v1 =='('  or v1 =='a' or v1 =='b' or v1 =='c' or v1 =='d' or v1 =='e' or v1 =='f' or v1 =='g' or v1 =='h' or v1 =='i' or v1 =='j' or v1 =='k' or v1 =='l' or v1 =='m' or v1 =='n' or v1 =='o' or v1 =='p' or v1 =='q' or v1 =='r'or v1 =='s' or v1 =='t'or v1 =='u' or v1 =='v'or v1 =='w' or v1 =='x'or v1 =='y' or v1 =='z' or v1 =='0'or v1 =='1' or v1 =='2' or v1 =='3' or v1 =='4' or v1 =='5' or  v1 =='6'or v1 =='7' or v1 =='8' or v1 =='9'):
                SV = v1
            if dr == 'left':
                if position > 0: position -= 1
                else: tape.insert(0, blank)
            if dr == 'right':
                position += 1
                if position >= len(tape): tape.append(blank)

            st = s1
        return cardinalidad


class Quiz(APIView): 
    # def consultar(p1,p2,p3,p4,p5,value):
    #     if value == 0:
    #         r1 = p1
    #         r2 = p2
    #         r3 = p3
    #         r4 = p4
    #         r5 = p5

    def createJson(self,p1,p2,p3,p4,p5):
        custom={"p1":p1,"p2":p2,"p3":p3,"p4":p4,"p5":p5,}
        auxiliar=json.dumps(custom)
        responseOk=json.loads(auxiliar)
        return responseOk

    def get(self, request, format=None):
        # Crear preguntas
        correctos = CFG.fromstring("""
            S -> KI VC VC V KF 
            KI -> '{' 
            VC -> V C
            KF -> '}'
            V -> ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0'
            C -> ','
        """)

        erroneos = CFG.fromstring("""
            S -> KI VE KF 
            KI -> '{' | '['
            VE -> VX VC V | VC VX V | VC VC VX | VC VC VC
            KF ->  '}' | ' '
            VX -> ' a)' | ' b(,' | ', c' | ' (e,)' | ' f(,' | ' 4),' | ' 5)' | ' 6},' | ' 7,,' | ' (8),'
            VC -> V C
            V -> ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0'
            C -> ','
        """)
        cBuenos = []
        cMalos = []
        valor=0
        vran1=random.randint(1,4095)
        vran2=random.randint(1,4095)
        vran3=random.randint(1,4095)
        for s in generate(correctos,n=4095):
            #print(''.join(s))
            valor = ''.join(s)
            cBuenos.append(valor)

        for s in generate(erroneos,n=6095):
            #print(''.join(s))
            valor = ''.join(s)
            cMalos.append(valor)
        print('hola')

        p1 = random.randint(1,4)
        p2=''
        p3 = random.randint(1,4)
        p4=''
        p5 = random.randint(1,4)



        aux1=random.randint(1,3)
        for i in range(1,4):
            if aux1 == i:
                p2 = p2 + cMalos[vran1] + '|'
            else: 
                p2 = p2 + cBuenos[random.randint(1,4095)] + '|'

        aux2=random.randint(1,3)
        for y in range(1,4):
            if aux2 == y:
                p4 = p4 + cBuenos[vran2] + '|'
            else: 
                p4 = p4 + cMalos[random.randint(1,4095)] + '|'

        p2 = p2 + str(aux1)
        p4 = p4 + str(aux2)




        print(p4)
        responseOk=self.createJson(p1,p2,p3,p4,p5)
        return Response(responseOk) 

        