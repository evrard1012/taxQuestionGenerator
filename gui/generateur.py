import random

def distractor(liste_result):
    result=[]
    for elt in liste_result:
        result.append(elt)
    return result,1

##la liste des min_max
##liste a la structure suivante =>(id,min,max,pour)
def transform_list_paliers_to_dict(liste):
    #la clef c'est le taux et la valeur est le couple(valeur_min,valeur_max)
    dictionnaire=dict()
    for elt in liste:
        dictionnaire[elt[3]]=elt[1],elt[2]
    return dictionnaire

#les clefs sont des entiers 
#les valeurs peuvent etre des tuples de 1,2 ou 3
#liste_montants a la structure suivante =>(montant,id)
def transform_list_montants_to_dict(liste_montants):
    dictionnaire_un=dict()
    dictionnaire_deux=dict()
    dictionnaire_trois=dict()
    
    i=1
    for elt in liste_montants:
        dictionnaire_un[i]=elt[0]
        i=i+1
    i=1   
    for j in range(len(liste_montants)):
        for k in range(j+1,len(liste_montants)):
            dictionnaire_deux[i]=liste_montants[j][0],liste_montants[k][0]
            i=i+1
    i=1       
    for j in range(len(liste_montants)):
        for k in range(j+1,len(liste_montants)):
            for l in range(k+1,len(liste_montants)):
                dictionnaire_trois[i]=liste_montants[j][0],liste_montants[k][0],liste_montants[l][0]
                i=i+1
    return dictionnaire_un,dictionnaire_deux,dictionnaire_trois

    
                
#liste(id,min,max,pour),liste_de_tuple (montant,id),nombreQts
#list_min_max_pour doit etre un dictionnaire ou la cles
#3 3 ou  deux deux ou un un        
def generateur(list_min_max_pour,list_mts,nombreQts):
    dict_min_max=transform_list_paliers_to_dict(list_min_max_pour)
    dictionnaire_mts_un,dictionnaire_mts_deux,dictionnaire_mts_trois=transform_list_montants_to_dict(list_mts)
    
    questions=list()
    options = list()
    answers = list()

    q=1
    if nombreQts !=0 and nombreQts >0:
        while nombreQts > 0:
            #genere aleatoirement le nombre de mantants
            #soit 1, 2 ou 3
            valeur=random.randrange(1, 3)
            liste_mts=[]

            if(valeur==1):
                liste_mts=list(set(random.sample(list(dictionnaire_mts_un.values()),valeur)))
            elif(valeur==2):
                tampon=random.sample(list(dictionnaire_mts_deux.values()),valeur)
                for elt in tampon:
                    liste_mts.append(elt[0])
                    liste_mts.append(elt[1])
                liste_mts=list(set(liste_mts))
            else:
                tampon=random.sample(list(dictionnaire_mts_trois.values()),valeur)
                for elt in tampon:
                    liste_mts.append(elt[0])
                    liste_mts.append(elt[1])
                    liste_mts.append(elt[2])
                liste_mts=list(set(liste_mts))
                    

            liste_result=[]
            print('----')
            for elt in liste_mts:
                print(elt)
                for pourcent,interval in dict_min_max.items():
                    if(interval[0]<=elt and elt<=interval[1]):
                        liste_result.append((pourcent*elt)/100)
                        
            la_question=""         
            for elt in liste_mts:
                la_question=la_question+str(elt)+"f, "
            #la_question=la_question+"\\n Les différents taux d’enregistrement sont respectivement de "  

            questions.append("Q"+str(q)+". "+la_question)
            o,a=distractor(tuple(liste_result))

            answers.append(a)
            options.append(o)

            q=q+1
            nombreQts=nombreQts-1
        
    return {"question": questions,"options": options, "answers": answers}


#print(transform_list_montants_to_dict([(1,0),(2,7),(3,9),(4,10)]))
print('*****************')
#print(transform_list_paliers_to_dict([(0,0,50,7),(1,50,100,5),(2,100,150,2)]))

list_min_max_pour=[(1,0,5000000,7),(2,5000000,50000000,5),(3,50000000,10000000000,3.3)]
list_mts=[(4850000,1),(14350000,2),(86775240,3)]
print(generateur(list_min_max_pour,list_mts,2))


    
