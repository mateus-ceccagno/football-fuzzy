import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def inicializaVariaveis():
    x_vitorias = np.arange(0, 21, 1)
    x_touchdowns = np.arange(0, 21, 1)
    x_jardas = np.arange(0, 2000, 1)
    x_recepcoes = np.arange(0, 201, 1)
    x_resultado  = np.arange(0, 11, 1)

    vitorias = ctrl.Antecedent(x_vitorias, 'Vitorias')
    touchdowns = ctrl.Antecedent(x_touchdowns, 'Touchdowns')
    jardas = ctrl.Antecedent(x_jardas, 'Jardas')
    recepcoes = ctrl.Antecedent(x_recepcoes, 'Recepções')
    resultado = ctrl.Consequent(x_resultado, 'Resultado')

    vitorias['Pouco'] = fuzz.zmf(x_vitorias, 3,5)
    vitorias['Intermediario'] = fuzz.trapmf(x_vitorias, [3, 5, 9, 11])
    vitorias['Excelente'] = fuzz.smf(x_vitorias, 9,11)

    touchdowns['Pouco'] = fuzz.zmf(x_touchdowns, 2, 4)
    touchdowns['Intermediario'] = fuzz.trapmf(x_touchdowns, [2, 4, 7, 10])
    touchdowns['Excelente'] = fuzz.smf(x_touchdowns, 6, 10)

    jardas['Pouco'] = fuzz.zmf(x_jardas, 400, 500)
    jardas['Intermediario'] = fuzz.trapmf(x_jardas, [400, 500, 800, 900])
    jardas['Bom'] = fuzz.trapmf(x_jardas, [800, 900, 1250, 1300])
    jardas['Excelente'] = fuzz.smf(x_jardas, 1150, 1400)

    recepcoes['Pouco'] = fuzz.zmf(x_recepcoes, 35, 45)
    recepcoes['Intermediario'] = fuzz.trapmf(x_recepcoes, [35, 45, 70, 85])
    recepcoes['Bom'] = fuzz.trapmf(x_recepcoes, [70, 85, 105, 115])
    recepcoes['Excelente'] = fuzz.smf(x_recepcoes, 105, 115)

    resultado['Desclassificado'] = fuzz.zmf(x_resultado,1,2)
    resultado['Top 100'] = fuzz.trapmf(x_resultado, [1, 2, 3, 4])
    resultado['Top 50'] = fuzz.trapmf(x_resultado, [3, 4, 5, 6])
    resultado['Top 20'] = fuzz.trapmf(x_resultado, [5, 6, 7, 8])
    resultado['Top 10'] = fuzz.smf(x_resultado,7, 8)


    rule1 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Pouco'] & recepcoes['Pouco'], resultado['Desclassificado'])         #OK
    rule2 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Pouco'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK
    rule3 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco'] & jardas['Pouco'] & recepcoes['Pouco'], resultado['Desclassificado'])     #OK

    rule4 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Pouco'] & recepcoes['Pouco'], resultado['Desclassificado'])#OK
    rule5 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Pouco'] & recepcoes['Pouco'], resultado['Desclassificado'])     #OK

    rule6 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Intermediario'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK
    rule7 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Bom'] & recepcoes['Pouco'], resultado['Desclassificado'])            #OK
    rule8 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Excelente'] & recepcoes['Pouco'], resultado['Desclassificado'])     #OK

    rule9 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Pouco'] & recepcoes['Intermediario'], resultado['Desclassificado'])#OK
    rule10 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Pouco'] & recepcoes['Bom'], resultado['Desclassificado'])          #OK
    rule11 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Pouco'] & recepcoes['Excelente'], resultado['Desclassificado'])    #OK

    rule12 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Intermediario'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK
    rule13 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Bom'] & recepcoes['Pouco'], resultado['Desclassificado'])          #OK
    rule14 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Excelente'] & recepcoes['Pouco'], resultado['Desclassificado'])    #OK

    rule15 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Pouco'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule16 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Pouco'] & recepcoes['Bom'], resultado['Desclassificado']) #OK
    rule17 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Pouco'] & recepcoes['Excelente'], resultado['Desclassificado']) #OK

    rule18 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Intermediario'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK
    rule19 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Bom'] & recepcoes['Pouco'], resultado['Desclassificado'])          #OK
    rule20 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Excelente'] & recepcoes['Pouco'], resultado['Top 50'])             #OK

    rule21 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Pouco'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule22 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Pouco'] & recepcoes['Bom'], resultado['Desclassificado'])          #OK
    rule23 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Pouco'] & recepcoes['Excelente'], resultado['Desclassificado'])             #OK

    rule24 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Intermediario'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule25 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Intermediario'] & recepcoes['Bom'], resultado['Desclassificado'])            #OK
    rule26 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Intermediario'] & recepcoes['Excelente'], resultado['Desclassificado'])      #OK

    rule27 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Excelente'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule28 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Excelente'] & recepcoes['Bom'], resultado['Desclassificado'])          #OK
    rule29 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Excelente'] & recepcoes['Excelente'], resultado['Desclassificado'])             #OK

    rule30 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Intermediario'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule31 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Bom'] & recepcoes['Intermediario'], resultado['Desclassificado'])          #OK
    rule32 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Excelente'] & recepcoes['Intermediario'], resultado['Desclassificado'])    #OK

    rule33 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Intermediario'] & recepcoes['Bom'], resultado['Desclassificado']) #OK
    rule34 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Bom'] & recepcoes['Bom'], resultado['Desclassificado'])          #OK
    rule35 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Excelente'] & recepcoes['Bom'], resultado['Desclassificado'])    #OK

    rule36 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Intermediario'] & recepcoes['Excelente'], resultado['Desclassificado']) #OK
    rule37 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Bom'] & recepcoes['Excelente'], resultado['Desclassificado'])            #OK
    rule38 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Intermediario'] & jardas['Excelente'] & recepcoes['Excelente'], resultado['Desclassificado'])        #OK

    rule39 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Bom'] & recepcoes['Bom'], resultado['Desclassificado'])            #OK
    rule40 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Intermediario'] & recepcoes['Bom'], resultado['Desclassificado']) #OK
    rule41 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Excelente'] & recepcoes['Bom'], resultado['Top 100'])    #OK

    rule42 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Bom'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule43 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Bom'] & recepcoes['Excelente'], resultado['Desclassificado']) #OK

    rule44 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Excelente'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule45 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Excelente'] & recepcoes['Excelente'], resultado['Top 100'])             #OK

    rule46 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Intermediario'] & recepcoes['Excelente'], resultado['Desclassificado']) #OK
    rule47 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Excelente'] & jardas['Intermediario'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK

    rule48 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Bom'] & recepcoes['Intermediario'], resultado['Desclassificado'])      #OK
    rule49 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Bom'] & recepcoes['Excelente'], resultado['Desclassificado'])          #OK
    rule50 = ctrl.Rule(vitorias['Pouco'] & touchdowns['Pouco'] & jardas['Bom'] & recepcoes['Bom'], resultado['Desclassificado'])                #OK

    rule51 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Pouco'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK
    rule52 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Pouco'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK

    rule53 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Intermediario'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK
    rule54 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Bom'] & recepcoes['Pouco'], resultado['Desclassificado'])            #OK
    rule55 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Excelente'] & recepcoes['Pouco'], resultado['Desclassificado'])      #OK

    rule56 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Pouco'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule57 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Pouco'] & recepcoes['Bom'], resultado['Desclassificado'])          #OK
    rule58 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Pouco'] & recepcoes['Excelente'], resultado['Desclassificado'])    #OK

    rule59 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Intermediario'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK
    rule60 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Bom'] & recepcoes['Pouco'], resultado['Desclassificado'])            #OK
    rule61 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Excelente'] & recepcoes['Pouco'], resultado['Desclassificado'])      #OK

    rule62 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Pouco'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule63 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Pouco'] & recepcoes['Bom'], resultado['Desclassificado'])           #OK
    rule64 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Pouco'] & recepcoes['Excelente'], resultado['Desclassificado'])      #OK

    rule65 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Intermediario'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK
    rule66 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Bom'] & recepcoes['Pouco'], resultado['Desclassificado'])          #OK
    rule67 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Excelente'] & recepcoes['Pouco'], resultado['Desclassificado'])    #OK

    rule68 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Pouco'] & recepcoes['Intermediario'], resultado['Desclassificado'])    #OK
    rule69 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Pouco'] & recepcoes['Bom'], resultado['Desclassificado'])            #OK
    rule70 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Pouco'] & recepcoes['Excelente'], resultado['Desclassificado'])        #OK

    rule71 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Intermediario'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule72 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Intermediario'] & recepcoes['Bom'], resultado['Desclassificado'])            #OK
    rule73 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Intermediario'] & recepcoes['Excelente'], resultado['Desclassificado'])      #OK

    rule74 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Excelente'] & recepcoes['Intermediario'], resultado['Desclassificado'])      #OK
    rule75 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Excelente'] & recepcoes['Bom'], resultado['Desclassificado'])                #OK
    rule76 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Excelente'] & recepcoes['Excelente'], resultado['Desclassificado'])          #OK

    rule77 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Intermediario'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule78 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Bom'] & recepcoes['Intermediario'], resultado['Desclassificado'])
    rule79 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Excelente'] & recepcoes['Intermediario'], resultado['Top 100'])

    rule80 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Intermediario'] & recepcoes['Bom'], resultado['Desclassificado']) #OK
    rule81 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Bom'] & recepcoes['Bom'], resultado['Desclassificado'])
    rule82 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Excelente'] & recepcoes['Bom'], resultado['Top 50'])

    rule83 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Intermediario'] & recepcoes['Excelente'], resultado['Desclassificado']) #OK
    rule84 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Bom'] & recepcoes['Excelente'], resultado['Desclassificado'])
    rule85 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Intermediario'] & jardas['Excelente'] & recepcoes['Excelente'], resultado['Top 50'])

    rule86 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Bom'] & recepcoes['Bom'], resultado['Desclassificado'])
    rule87 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Intermediario'] & recepcoes['Bom'], resultado['Desclassificado']) #OK
    rule88 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Excelente'] & recepcoes['Bom'], resultado['Top 50'])

    rule89 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Bom'] & recepcoes['Intermediario'], resultado['Desclassificado'])
    rule90 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Bom'] & recepcoes['Excelente'], resultado['Desclassificado'])

    rule91 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Excelente'] & recepcoes['Intermediario'], resultado['Top 20'])
    rule92 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Excelente'] & recepcoes['Excelente'], resultado['Top 10'])

    rule93 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Intermediario'] & recepcoes['Excelente'], resultado['Desclassificado'])    #OK
    rule94 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Excelente'] & jardas['Intermediario'] & recepcoes['Intermediario'], resultado['Desclassificado'])#OK

    rule95 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Bom'] & recepcoes['Intermediario'], resultado['Desclassificado'])  #OK
    rule96 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Bom'] & recepcoes['Excelente'], resultado['Desclassificado'])      #OK
    rule97 = ctrl.Rule(vitorias['Intermediario'] & touchdowns['Pouco'] & jardas['Bom'] & recepcoes['Bom'], resultado['Desclassificado'])          #OK

    rule98 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']   & jardas['Pouco'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK
    rule99 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']       & jardas['Pouco'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK

    rule100 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Intermediario'] & recepcoes['Pouco'], resultado['Desclassificado']) #OK
    rule101 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Bom'] & recepcoes['Pouco'], resultado['Desclassificado'])            #OK
    rule102 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Excelente'] & recepcoes['Pouco'], resultado['Desclassificado'])      #OK

    rule103 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Pouco']         & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule104 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Pouco']         & recepcoes['Bom'], resultado['Desclassificado']) #OK
    rule105 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Pouco']         & recepcoes['Excelente'], resultado['Desclassificado']) #OK

    rule106 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Intermediario'] & recepcoes['Pouco'], resultado['Desclassificado'])      #OK
    rule107 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Bom']           & recepcoes['Pouco'], resultado['Desclassificado'])      #OK
    rule108 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Excelente']     & recepcoes['Pouco'], resultado['Desclassificado'])      #OK

    rule109 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Pouco']         & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule110 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Pouco']         & recepcoes['Bom'], resultado['Desclassificado'])          #OK
    rule111 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Pouco']         & recepcoes['Excelente'], resultado['Desclassificado'])    #OK

    rule112 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Intermediario'] & recepcoes['Pouco'], resultado['Desclassificado'])      #OK
    rule113 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Bom']           & recepcoes['Pouco'], resultado['Desclassificado'])      #OK
    rule114 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Excelente']     & recepcoes['Pouco'], resultado['Desclassificado'])      #OK

    rule115 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Pouco']         & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule116 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Pouco']         & recepcoes['Bom'], resultado['Desclassificado'])          #OK
    rule117 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Pouco']         & recepcoes['Excelente'], resultado['Desclassificado'])     #OK

    rule118 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Intermediario'] & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule119 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Intermediario'] & recepcoes['Bom'], resultado['Desclassificado'])            #OK
    rule120 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Intermediario'] & recepcoes['Excelente'], resultado['Desclassificado'])      #OK

    rule121 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Excelente']     & recepcoes['Intermediario'], resultado['Desclassificado'])   #OK
    rule122 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Excelente']     & recepcoes['Bom'], resultado['Desclassificado'])              #OK
    rule123 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Excelente']     & recepcoes['Excelente'], resultado['Desclassificado'])      

    rule124 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Intermediario'] & recepcoes['Intermediario'], resultado['Desclassificado'])  #OK
    rule125 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Bom']           & recepcoes['Intermediario'], resultado['Desclassificado'])
    rule126 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Excelente']     & recepcoes['Intermediario'], resultado['Desclassificado'])

    rule127 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Intermediario'] & recepcoes['Bom'], resultado['Desclassificado'])    #OK
    rule128 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Bom']           & recepcoes['Bom'], resultado['Desclassificado'])
    rule129 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Excelente']     & recepcoes['Bom'], resultado['Top 50'])             #OK

    rule130 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Intermediario'] & recepcoes['Excelente'], resultado['Desclassificado']) #OK
    rule131 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Bom']           & recepcoes['Excelente'], resultado['Top 100'])
    rule132 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Intermediario']  & jardas['Excelente']     & recepcoes['Excelente'], resultado['Top 20'])           #ok

    rule133 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Bom']           & recepcoes['Bom'], resultado['Top 50']) #OK
    rule134 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Intermediario'] & recepcoes['Bom'], resultado['Desclassificado'])  #OK
    rule135 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Excelente']     & recepcoes['Bom'], resultado['Top 50'])           #OK

    rule136 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Bom']           & recepcoes['Intermediario'], resultado['Top 100']) #ok
    rule137 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Bom']           & recepcoes['Excelente'], resultado['Top 50'])      #ok

    rule138 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Excelente']     & recepcoes['Intermediario'], resultado['Top 50'])       #OK
    rule139 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Excelente']     & recepcoes['Excelente'], resultado['Top 10'])           #OK

    rule140 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Intermediario'] & recepcoes['Excelente'], resultado['Desclassificado']) #OK
    rule141 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Excelente']      & jardas['Intermediario'] & recepcoes['Intermediario'], resultado['Desclassificado']) # OK

    rule142 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Bom']           & recepcoes['Intermediario'], resultado['Desclassificado']) #OK
    rule143 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Bom']           & recepcoes['Excelente'], resultado['Desclassificado'])    #OK
    rule144 = ctrl.Rule(vitorias['Excelente'] & touchdowns['Pouco']          & jardas['Bom']           & recepcoes['Bom'], resultado['Desclassificado'])          #OK

    SE_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule18,rule19,
                                rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36,
                                rule37,rule38,rule39,rule40,rule41,rule42,rule43,rule44,rule45,rule46,rule47,rule48,rule49,rule50,rule51,rule52,rule53,
                                rule54,rule55,rule56,rule57,rule58,rule59,rule60,rule61,rule62,rule63,rule64,rule65,rule66,rule67,rule68,rule69,rule70,
                                rule71,rule72,rule73,rule74,rule75,rule76,rule77,rule78,rule79,rule80,rule81,rule82,rule83,rule84,rule85,rule86,rule87,
                                rule88,rule89,rule90,rule91,rule92,rule93,rule94,rule95,rule96,rule97,rule98,rule99,rule100,rule101,rule102,rule103,
                                rule104,rule105,rule106,rule107,rule108,rule109,rule110,rule111,rule112,rule113,rule114,rule115,rule116,rule117,rule118
                                ,rule119,rule120,rule121,rule122,rule123,rule124,rule125,rule126,rule127,rule128,rule129,rule130,rule131,rule132,
                                rule133,rule134,rule135,rule136,rule137,rule138,rule139,rule140,rule141,rule142,rule143,rule144])
    return ctrl.ControlSystemSimulation(SE_ctrl)

SE = inicializaVariaveis()

def classificacao(vitorias, touchdowns, jardas, recepcoes):
    SE.input['Vitorias'] = vitorias
    SE.input['Touchdowns'] = touchdowns
    SE.input['Jardas'] = jardas
    SE.input['Recepções'] = recepcoes
    SE.compute()
    return SE.output['Resultado']