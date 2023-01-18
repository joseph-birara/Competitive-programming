'It is summer'.
'It is sunny'.
'It is hot' :- 'It is summer', 'It is sunny'. 
'It is cold' :- 'It is winter', 'It is snowing'. 

ethiopian(doroWot).
lessSpicy(doroWot).
likes(hiwot,Food):-ethiopian(Food),lessSpicy(Food).
female(azeb). 
female(meskerem). 
female(hiwot). 
female(selam). 
female(tizita). 

male(melaku). 
male(eskindir). 
male(kaleab). 
male(worku). 
male(mekuaninit). 
male(alemayehu).
parentof(meskerem,azeb). 
parentof(meskerem, eskindir). 
parentof(meskerem, kaleab). 
parentof(meskerem, hiwot). 
parentof(meskerem, selam). 

parentof(melaku,azeb). 
parentof(melaku, eskindir). 
parentof(melaku, kaleab). 
parentof(melaku, hiwot). 
parentof(melaku, selam).
parentof(hiwot, tizita). 
parentof(hiwot, worku). 
parentof(hiwot, mekuaninit). 

parentof(alemayehu, tizita). 
parentof(alemayehu, worku). 
parentof(alemayehu, mekuaninit). 

siblingof(X,Y) :-parentof(Z,X), parentof(Z,Y), not(X =Y). 
brotherof(X,Y):-parentof(Z,X),parentof(Z,Y), not(X=Y), male(X).
sisterof(X,Y):-parentof(Z,X),parentof(Z,Y), not(X=Y), female(X).
motherof(X,Y):-parent(X,Y),female(X).
fatherof(X,Y):-parent(X,Y), male(X).
wifeof(X,Y):-husband(X,Y).
husbandof(X,Y):-parentof(X,Z),parent(Y,Z), male(X), female(Y).

circle:-
    write("enter the radius of the:"),tab(6),
    read(R),
    Area is 3.14 *R*R ,
    Perimeter is 2*3.14*R,
    write('area ='), write(Area),nl,
    write('perimeter = '), write(Perimeter).
cube:-
    write("enter the num: "),tab(6),
    read(Num),
    procces(Num).
procces(stop):- !.
procces(Num):-
    C is Num*Num*Num,
    write(C),nl,cube.
    
