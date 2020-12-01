def  prestamo(informacion: dict)-> dict:
    #definir variables
    id_prestamo = informacion['id_prestamo']
    casado = informacion['casado']
    dependientes = informacion['dependientes']
    educacion = informacion['educacion']
    independiente = informacion['independiente']
    i_d = informacion['ingreso_deudor']
    i_c = informacion['ingreso_codeudor']
    c_p = informacion['cantidad_prestamo']
    p_p = informacion['plazo_prestamo']
    historia_credito = informacion['historia_credito']
    tipo_propiedad = informacion['tipo_propiedad']
    independiente == 'independiente'
    #Variable Dependientes
    
    def quitar_plus(cadena, cuantos):
        temp = len(cadena)
        cadena1 = cadena[:temp - cuantos]
        dependientes = int(cadena1)
        return dependientes
    dependientes_bool = isinstance(dependientes, str)
    if dependientes_bool:
        dependientes = quitar_plus(dependientes, 1)
    else:
        dependientes = dependientes

    #Validaciones
    if historia_credito == 1:
        if i_c > 0 and i_d /9 > c_p:
            aprobado = True
        else:
            if dependientes > 2 and independiente:
                if i_c / 12 > c_p:
                    aprobado = True
                else:
                    aprobado = False
            else:
                if c_p < 200:
                    aprobado = True
                else:
                    aprobado = False
    else:
        if independiente:
            if  casado == 'No' and dependientes <= 1:
                if i_d / 10 > c_p or i_c/10 > c_p:
                    if c_p < 180:
                        aprobado = True
                    else:
                        aprobado = False
                else:
                    aprobado =  False
            else:
                aprobado = False
        else:
            if not tipo_propiedad != 'Semiurbano' and dependientes < 2:
                if educacion == 'Graduado':
                    if i_d/11 > c_p and i_c/11 > c_p:
                        aprobado = True
                    else:
                        aprobado = False
                else:
                    aprobado = False
            else:
                aprobado = False
    #Diccionario de salida
    salida = {'id_prestamo': id_prestamo, 'aprobado': aprobado}
    return salida


#**** CASO DE PRUEBA 1:****   Salida 1: True
print(prestamo(informacion = {'id_prestamo': 'SALIDA_1', 'casado': 'No', 'dependientes': 0, 'educacion': 'No Graduado', 'independiente': 'No', 'ingreso_deudor': 3748, 'ingreso_codeudor': 1668, 'cantidad_prestamo': 110, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Semiurbano'}))

#**** CASO DE PRUEBA 2:****   Salida 2: Caso True
print(prestamo(informacion = {'id_prestamo': 'SALIDA_2', 'casado': 'Si', 'dependientes': '3+', 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 1500, 'ingreso_codeudor': 18564, 'cantidad_prestamo': 206, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Urbano'}))

#**** CASO DE PRUEBA 3:****   Salida 2: Caso False
print(prestamo(informacion = {'id_prestamo': 'SALIDA_2', 'casado': 'Si', 'dependientes': '3+', 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 1500, 'ingreso_codeudor': 1, 'cantidad_prestamo': 206, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Urbano'}))

#**** CASO DE PRUEBA 4:****  Salida 3: Caso True
print(prestamo(informacion = {'id_prestamo': 'SALIDA_3', 'casado': 'No', 'dependientes': 2, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 3083, 'ingreso_codeudor': 0, 'cantidad_prestamo': 155, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))

#**** CASO DE PRUEBA 5:****  Salida 3: Caso False
print(prestamo(informacion = {'id_prestamo': 'SALIDA_3', 'casado': 'No', 'dependientes': '3+', 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 3083, 'ingreso_codeudor': 0, 'cantidad_prestamo': 255, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))

#**** CASO DE PRUEBA 6:****  Salida 4: Caso True
print(prestamo(informacion = {'id_prestamo': 'SALIDA_4', 'casado': 'No', 'dependientes': 0, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 0, 'cantidad_prestamo': 106, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))

#**** CASO DE PRUEBA 7:****  Salida 4: Caso False
print(prestamo(informacion = {'id_prestamo': 'SALIDA_4', 'casado': 'No', 'dependientes': '3+', 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 0, 'ingreso_codeudor': 11500, 'cantidad_prestamo': 206, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))

#**** CASO DE PRUEBA 8:****  Salida 5 Falso
print(prestamo(informacion = {'id_prestamo': 'SALIDA_5', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 0, 'ingreso_codeudor': 0, 'cantidad_prestamo': 206, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))

#**** CASO DE PRUEBA 9:****  Salida 6 Falso
print(prestamo(informacion = {'id_prestamo': 'SALIDA_6', 'casado': 'Si', 'dependientes': 2, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 0, 'cantidad_prestamo': 206, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))

#**** CASO DE PRUEBA 10:****  Salida 7: Caso True
print(prestamo(informacion = {'id_prestamo': 'SALIDA_7', 'casado': 'No', 'dependientes': 0, 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 10830, 'ingreso_codeudor': 10000, 'cantidad_prestamo': 100, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))

#**** CASO DE PRUEBA 11:****  Salida 7: Caso False
print(prestamo(informacion = {'id_prestamo': 'SALIDA_7', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 100, 'ingreso_codeudor': 10000, 'cantidad_prestamo': 206, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Rural'}))

#**** CASO DE PRUEBA 12:****  Salida 8 False
print(prestamo(informacion = {'id_prestamo': 'SALIDA_8', 'casado': 'Si', 'dependientes': 1, 'educacion': 'No Graduado', 'independiente': 'No', 'ingreso_deudor': 11500, 'ingreso_codeudor': 0, 'cantidad_prestamo': 206, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))

#**** CASO DE PRUEBA 13:****  Salida 9 False
print(prestamo(informacion = {'id_prestamo': 'SALIDA_9', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 11500, 'ingreso_codeudor': 0, 'cantidad_prestamo': 206, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Semiurbano'}))

