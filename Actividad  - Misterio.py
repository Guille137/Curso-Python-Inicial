# ACTIVIDAD - MISTERIO

abecedario=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

parrafo1= ['15', '05', '15', '03'], ['05', '15', '03', '15', '17', '06', '19'], ['19', '18'], ['15', '26'], ['15', '26', '06', '23'], ['15', '06', '02', '23', '05', '19', '07', '06', '23', '00'], ['01', '15', '05', '19', '16', '19', '18'], ['05', '15', '05', '07', '01', '02', '17', '01', '19'], ['06', '19', '05', '07'], ['06', '19', '09', '15', '26', '26'], ['06', '15', '07', '26', '08', '17', '02']
parrafo2= ['15', '26'], ['15', '05', '19', '00', '23', '05', '03'], ['15', '07', '06', '19'], ['15', '18', '15', '05', '05', '19', '07', '01', '19'], ['01', '19'], ['15', '26'], ['15', '12', '15', '26', '03'], ['19', '18'], ['15', '26'], ['15', '01', '08', '26'], ['15', '01', '19', '26', '26']
parrafo3= ['15', '26'], ['15', '18', '01', '08', '21', '19', '06'], ['15', '07', '06', '19'], ['15', '18', '23', '18', '01', '02', '17', '06', '19'], ['01', '19'], ['15', '26'], ['15', '09', '19', '08', '17'], ['19', '18'], ['06', '02', '26'], ['06', '02', '05', '05', '08', '06', '08', '06']
parrafo4= ['15', '26'], ['15', '05', '19', '17', '05', '19', '07'], ['15', '07', '06', '19'], ['15', '18', '23', '21', '19', '07', '02', '05', '03'], ['05', '02', '03'], ['26', '19'], ['01', '15', '23', '18', '05', '15', '08', '21'], ['26', '19', '18'], ['02', '05', '15', '20']
parrafo5= ['01', '02', '17'], ['06', '15', '26'], ['06', '19', '05', '07'], ['06', '19', '09', '15', '26', '26'], ['01', '15', '05', '18', '02', '03'], ['05', '23', '05', '16', '15'], ['26', '19'], ['26', '15', '07', '05', '02', '03'], ['19', '08', '04'], ['06', '02', '26'], ['15', '05', '15', '09', '19', '26', '26'], ['15'], ['15', '06', '15', '17']

mensaje= [parrafo1,parrafo2,parrafo3,parrafo4,parrafo5]

def descifrar_codigo(mensaje):
    i=0
    mensaje_descifrado=[]
    
    
    for palabra in mensaje:
        palabra_descifrada=[]
        for letra in palabra:
            i=int(letra)-15
            if i<0:
                i+=27
            palabra_descifrada.append(abecedario[i])
        
        palabra_descifrada.reverse()
        mensaje_descifrado.append(''.join(palabra_descifrada))
        
    
        
    print(' '.join(mensaje_descifrado))
    
for parrafo in mensaje:
    descifrar_codigo(parrafo)