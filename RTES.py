# -*- coding: utf-8 -*-
"""
Created on Mon May 31 18:27:41 2021

@author: Erik Trincado
"""

import numpy as np
import matplotlib.pyplot as plt
from tkinter import*
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

########### Funciones auxiliares ###############
def radianes(angulo):
    radianes=(np.pi*angulo)/180
    return radianes



############### Inicio ventana principal ###################


ventana= Tk()
ventana.title("RTES - Análisis de Esfuerzos")
ventana.config(bd=20)
ventana.geometry("300x400")
ventana.resizable(0,0)



################## Ventana Resultado 1 ##########################
def resultado1():
    ventana2 = tk.Toplevel(ventana)
    ventana2.title("Resultado - Verificación Vectorial")
    ventana2.geometry("300x600")
    ventana2.resizable(0,0)
    
    ##convertir variables en numeros usables
    #vs1_1 = float(vs1.get())
    #vs2_1 = float(vs2.get())
    #vs3_1 = float(vs3.get())
    as1_1 = float(as1.get())
    as2_1 = float(as2.get())
    as3_1 = float(as3.get())
    is1_1 = float(is1.get())
    is2_1 = float(is2.get())
    is3_1 = float(is3.get())
    trend_1=float(trend.get())
    plunge_1=float(plunge.get())
    
    ############## calculo matriciales ################
    #obtener beta y delta para matriz de cosenos directores
    if as1_1<270:
        beta_s1=90-as1_1
    else:
        beta_s1=360+90-as1_1
    alfa_s1=is1_1
    
    if as2_1<270:
        beta_s2=90-as2_1
    else:
        beta_s2=360+90-as2_1
    alfa_s2=is2_1
    
    if as3_1<270:
        beta_s3=90-as3_1
    else:
        beta_s3=360+90-as3_1
    alfa_s3=is3_1
    
    #valores de matriz L
    l0_0 = np.cos(radianes(beta_s1))*np.cos(radianes(alfa_s1))
    l0_1 = np.sin(radianes(beta_s1))*np.cos(radianes(alfa_s1))
    l0_2 = np.sin(radianes(alfa_s1))
    
    l1_0 = np.cos(radianes(beta_s2))*np.cos(radianes(alfa_s2))
    l1_1 = np.sin(radianes(beta_s2))*np.cos(radianes(alfa_s2))
    l1_2 = np.sin(radianes(alfa_s2))
    
    l2_0 = np.cos(radianes(beta_s3))*np.cos(radianes(alfa_s3))
    l2_1 = np.sin(radianes(beta_s3))*np.cos(radianes(alfa_s3))
    l2_2 = np.sin(radianes(alfa_s3))
    
    #Matriz L
    l= np.array([[l0_0,l0_1,l0_2],[l1_0,l1_1,l1_2],[l2_0,l2_1,l2_2]],float)
    
    ##Unitarios
    us1=(l[0][0]**2 + l[0][1]**2 + l[0][2]**2)**(1/2)
    us2=(l[1][0]**2 + l[1][1]**2 + l[1][2]**2)**(1/2)
    us3=(l[2][0]**2 + l[2][1]**2 + l[2][2]**2)**(1/2)

    ##ortogonales
    s1_s2=np.dot(l[0],l[1])
    s2_s3=np.dot(l[1],l[2])
    s3_s1=np.dot(l[2],l[0])
    
    ## Edición de presentación de resultados
    us1=round(us1,2)
    us2=round(us1,2)
    us2=round(us1,2)
    s1_s2=round(s1_s2,4)
    s2_s3=round(s2_s3,4)
    s3_s1=round(s3_s1,4)
    
    #########Grafica de esfuerzos ############
    
    ##Edición de datos para graficar esfuerzos
    #Edición de azimut
    if is1_1<0:
        as1_1=as1_1
    else:
        if as1_1<180:
            as1_1=as1_1+180
        else:
            as1_1=as1_1-180
    
    if is2_1<0:
        as2_1=as2_1
    else:
        if as2_1<180:
            as2_1=as2_1+180
        else:
            as2_1=as2_1-180
            
    if is3_1<0:
        as3_1=as3_1
    else:
        if as3_1<180:
            as3_1=as3_1+180
        else:
            as3_1=as3_1-180
    
    #Edición de inclinaciones
    if is1_1<0:
        is1_1=is1_1
    else:
        is1_1=is1_1*-1
        
    if is2_1<0:
        is2_1=is2_1
    else:
        is2_1=is2_1*-1
        
    if is3_1<0:
        is3_1=is3_1
    else:
        is3_1=is3_1*-1
        
    #Obtener radio para graficar esfuerzos
    xs1=np.cos(radianes(90-as1_1))*(90-np.absolute(is1_1))
    ys1=np.sin(radianes(90-as1_1))*(90-np.absolute(is1_1))
    rs1=(xs1**2 + ys1**2)**(1/2)
    
    xs2=np.cos(radianes(90-as2_1))*(90-np.absolute(is2_1))
    ys2=np.sin(radianes(90-as2_1))*(90-np.absolute(is2_1))
    rs2=(xs2**2 + ys2**2)**(1/2)
    
    xs3=np.cos(radianes(90-as3_1))*(90-np.absolute(is3_1))
    ys3=np.sin(radianes(90-as3_1))*(90-np.absolute(is3_1))
    rs3=(xs3**2 + ys3**2)**(1/2)
    
    ############ Grafica de proyecciones ##############
    
    ##Edición de datos para graficar proyecciones
    #corrección de eje z
    if plunge_1<0:
        iz=trend_1
    else:
        iz=trend_1+180
        
    #calculo de auxiliares
    td1=trend_1+90
    pd1=0
    td2=trend_1
    td3=trend_1
    pd2=plunge_1
    pd3=plunge_1+90
    
    #Obtener radio para graficar proyecciones
    xd1=np.cos(radianes(90-td1))*(90-np.absolute(pd1))
    yd1=np.sin(radianes(90-td1))*(90-np.absolute(pd1))
    rd1=(xd1**2 + yd1**2)**(1/2)
    
    xd2=np.cos(radianes(90-td2))*(90-np.absolute(pd2))
    yd2=np.sin(radianes(90-td2))*(90-np.absolute(pd2))
    rd2=(xd2**2 + yd2**2)**(1/2)
    
    xd3=np.cos(radianes(90-td3))*(90-np.absolute(pd3))
    yd3=np.sin(radianes(90-td3))*(90-np.absolute(pd3))
    rd3=(xd3**2 + yd3**2)**(1/2)
    
    ############## Ploteo de datos ############
    
    #Crea el grafico
    figura=Figure(figsize=(3,3.2), dpi=100)
    x1=figura.add_subplot(111, polar=True)
    
    #Plotear esfuerzos
    x1.plot(radianes(as1_1), rs1, 'o-',color='g', linewidth=8)
    x1.plot(radianes(as2_1), rs2, 'o-',color='g', linewidth=8)
    x1.plot(radianes(as3_1), rs3, 'o-',color='g', linewidth=8)
    
    #poner nombre a los esfuerzos
    x1.text(radianes(as1_1),rs1,"S1",color="g",
         horizontalalignment='right', verticalalignment='bottom')
    x1.text(radianes(as2_1),rs2,"S2",color="g",
         horizontalalignment='right', verticalalignment='bottom')
    x1.text(radianes(as3_1),rs3,"S3",color="g",
         horizontalalignment='right', verticalalignment='bottom')
    
    #Graficar ejes del túnel
    x1.annotate("", xy = (radianes(trend_1), rd2), xycoords = 'data',
                 xytext = (0, 0), textcoords = 'data',
                          arrowprops = dict(arrowstyle = "->"),fontsize=10)
    x1.annotate("", xy = (radianes(trend_1+90), rd1), xycoords = 'data',
                 xytext = (0, 0), textcoords = 'data',
                          arrowprops = dict(arrowstyle = "->"),fontsize=10)
    x1.annotate("", xy = (radianes(iz), rd3), xycoords = 'data',
                 xytext = (0, 0), textcoords = 'data',
                          arrowprops = dict(arrowstyle = "->"),fontsize=10)
    
    #Poner nombre a los ejes
    x1.text(radianes(trend_1),rd2,"Y'(T)",color='r',fontsize=10,
             horizontalalignment='right', verticalalignment='bottom')
    x1.text(radianes(trend_1+90),rd1,"X'",color='r',fontsize=10,
             horizontalalignment='right', verticalalignment='bottom')
    x1.text(radianes(iz),rd3,"Z'",color='r',fontsize=10,
             horizontalalignment='right', verticalalignment='bottom')
    
    #configuración del grafico
    x1.set_theta_zero_location("N")
    x1.set_theta_direction(-1)
    x1.set_title("INPUT", va='bottom')
    x1.set_rticks(np.arange(90,90,90))
    x1.set_rmax(90)
    x1.grid()
    
    #Dibujar en pantalla
    canvas = FigureCanvasTkAgg(figura, master=ventana2)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    ###########  etiquetas y pantallas de resultados ######
    
    #etiquetas de resultados
    etiqueta1= Label(ventana2, text="Verificación de Vectores Unitarios")
    etiqueta1.place(x=10,y=350)
    
    etiqueta2= Label(ventana2, text="S1")
    etiqueta2.place(x=20,y=370)
    
    etiqueta3= Label(ventana2, text="S2")
    etiqueta3.place(x=20,y=400)
    
    etiqueta4= Label(ventana2, text="S3")
    etiqueta4.place(x=20,y=430)
    
    etiqueta5= Label(ventana2, text="Verificación de Vectores Ortogonales")
    etiqueta5.place(x=10,y=460)
    
    etiqueta6= Label(ventana2, text="S1-S2")
    etiqueta6.place(x=20,y=490)
    
    etiqueta7= Label(ventana2, text="S2-S3")
    etiqueta7.place(x=20,y=520)
    
    etiqueta8= Label(ventana2, text="S3-S1")
    etiqueta8.place(x=20,y=550)
    
    ##resultados
    resultado_us1= DoubleVar()
    resultado_us1.set(us1)
    resultado_us2= DoubleVar()
    resultado_us2.set(us2)
    resultado_us3= DoubleVar()
    resultado_us3.set(us3)
    
    r_s1_s2=DoubleVar()
    r_s1_s2.set(s1_s2)
    
    r_s2_s3=DoubleVar()
    r_s2_s3.set(s2_s3)
    
    r_s3_s1=DoubleVar()
    r_s3_s1.set(s3_s1)
    
    
    #Pantallas de resultados
    pantalla1= Entry(ventana2, textvariable=resultado_us1, width=8,state="disable")
    pantalla1.place(x=50, y=370)
    pantalla2= Entry(ventana2, textvariable=resultado_us2, width=8,state="disable")
    pantalla2.place(x=50, y=400)
    pantalla3= Entry(ventana2, textvariable=resultado_us3, width=8,state="disable")
    pantalla3.place(x=50, y=430)
    
    pantalla4= Entry(ventana2, textvariable=r_s1_s2, width=8,state="disable")
    pantalla4.place(x=70, y=490)
    pantalla5= Entry(ventana2, textvariable=r_s2_s3, width=8,state="disable")
    pantalla5.place(x=70, y=520)
    pantalla6= Entry(ventana2, textvariable=r_s3_s1, width=8,state="disable")
    pantalla6.place(x=70, y=550)
    
    
################## Ventana Resultado2 ##########################
def resultado2():
    ventana3 = tk.Toplevel(ventana)
    ventana3.title("Resultado - Rotación de Tensor")
    ventana3.geometry("300x600")
    ventana3.resizable(0,0)
    
    ##convertir variables en numeros usables
    vs1_2 = float(vs1.get())
    vs2_2 = float(vs2.get())
    vs3_2 = float(vs3.get())
    as1_2 = float(as1.get())
    as2_2 = float(as2.get())
    as3_2 = float(as3.get())
    is1_2 = float(is1.get())
    is2_2 = float(is2.get())
    is3_2 = float(is3.get())
    trend_2=float(trend.get())
    plunge_2=float(plunge.get())
    
    ######## Rotacion de esfuerzos a ejes cartesianos #####
    
    ## obtener beta y delta para matriz de cosenos directores
    
    if as1_2<270:
        beta_s1_2=90-as1_2
    else:
        beta_s1_2=360+90-as1_2
    alfa_s1_2=is1_2
    
    if as2_2<270:
        beta_s2_2=90-as2_2
    else:
        beta_s2_2=360+90-as2_2
    alfa_s2_2=is2_2
    
    if as3_2<270:
        beta_s3_2=90-as3_2
    else:
        beta_s3_2=360+90-as3_2
    alfa_s3_2=is3_2
    
    ## valores de matriz L
    l0_0_2 = np.cos(radianes(beta_s1_2))*np.cos(radianes(alfa_s1_2))
    l0_1_2 = np.sin(radianes(beta_s1_2))*np.cos(radianes(alfa_s1_2))
    l0_2_2 = np.sin(radianes(alfa_s1_2))
    
    l1_0_2 = np.cos(radianes(beta_s2_2))*np.cos(radianes(alfa_s2_2))
    l1_1_2 = np.sin(radianes(beta_s2_2))*np.cos(radianes(alfa_s2_2))
    l1_2_2 = np.sin(radianes(alfa_s2_2))
    
    l2_0_2 = np.cos(radianes(beta_s3_2))*np.cos(radianes(alfa_s3_2))
    l2_1_2= np.sin(radianes(beta_s3_2))*np.cos(radianes(alfa_s3_2))
    l2_2_2= np.sin(radianes(alfa_s3_2))
    
    ## matriz M
    m_2 = np.array([[vs1_2,0,0],[0,vs2_2,0],[0,0,vs3_2]],float)
    ## Matriz L
    l_2= np.array([[l0_0_2,l0_1_2,l0_2_2],[l1_0_2,l1_1_2,l1_2_2],[l2_0_2,l2_1_2,l2_2_2]],float)
    ##Matriz L transpuesta
    l_t_2=np.transpose(l_2)
    
    ### tensor de esfuerzo en XYZ
    s_xyz_2=np.matmul((np.matmul(l_t_2,m_2)),l_2)
    
    ######## Rotacion de esfuerzos a ejes del túnel #####
    
    #calculo de auxiliares
    td1_2=trend_2+90
    pd1_2=0
    td2_2=trend_2
    td3_2=trend_2
    pd2_2=plunge_2
    pd3_2=plunge_2+90
    
    #obtener beta y delta para matriz de cosenos directores
    
    if td1_2<270:
        beta2_s1_2=90-td1_2
    else:
        beta2_s1_2=360+90-td1_2
    alfa2_s1_2=pd1_2
    
    if td2_2<270:
        beta2_s2_2=90-td2_2
    else:
        beta2_s2_2=360+90-td2_2
    alfa2_s2_2=pd2_2
    
    if td3_2<270:
        beta2_s3_2=90-td3_2
    else:
        beta2_s3_2=360+90-td3_2
    alfa2_s3_2=pd3_2
    
    #valores de matriz L
    l0_0_2_2 = np.cos(radianes(beta2_s1_2))*np.cos(radianes(alfa2_s1_2))
    l0_1_2_2 = np.sin(radianes(beta2_s1_2))*np.cos(radianes(alfa2_s1_2))
    l0_2_2_2 = np.sin(radianes(alfa2_s1_2))
    
    l1_0_2_2 = np.cos(radianes(beta2_s2_2))*np.cos(radianes(alfa2_s2_2))
    l1_1_2_2 = np.sin(radianes(beta2_s2_2))*np.cos(radianes(alfa2_s2_2))
    l1_2_2_2 = np.sin(radianes(alfa2_s2_2))
    
    l2_0_2_2 = np.cos(radianes(beta2_s3_2))*np.cos(radianes(alfa2_s3_2))
    l2_1_2_2 = np.sin(radianes(beta2_s3_2))*np.cos(radianes(alfa2_s3_2))
    l2_2_2_2 = np.sin(radianes(alfa2_s3_2))
    
    ##matriz M
    m_2_2 = s_xyz_2
    #Matriz L
    l_2_2= np.array([[l0_0_2_2,l0_1_2_2,l0_2_2_2],[l1_0_2_2,l1_1_2_2,l1_2_2_2],[l2_0_2_2,l2_1_2_2,l2_2_2_2]],float)
    #Matriz L transpuesta
    l_t_2_2=np.transpose(l_2_2)
    
    ### tensor de esfuerzo en XYZ
    s_xyz_2_s=np.matmul((np.matmul(l_2_2,m_2_2)),l_t_2_2)
    
    ########### calculo para P y Q ##########
    sxx_2=s_xyz_2_s[0][0]
    szz_2=s_xyz_2_s[2][2]
    sxz_2=s_xyz_2_s[0][2]
    szx_2=s_xyz_2_s[2][0]
    
    lmda_2=(np.arctan((2*sxz_2/(sxx_2-szz_2))))*180/np.pi
    
    P_2= ((sxx_2+szz_2)/2)+(((1/4)*((sxx_2-szz_2)**2))+(sxz_2**2))**(1/2)
    Q_2=((sxx_2+szz_2)/2)-(((1/4)*((sxx_2-szz_2)**2))+(sxz_2**2))**(1/2)
    P_Q_2=P_2/Q_2
    
    ## calculos de angulos ##
    #Sacar angulo
    if sxx_2>szz_2:
        ang1_2=lmda_2/2
    elif sxx_2<szz_2 and sxz_2>0:
        ang1_2=(lmda_2/2)+90
    elif sxx_2<szz_2 and sxz_2<0:
        ang1_2=(lmda_2/2)-90
    ang2_2=ang1_2+90

    ############# Ploteo de datos #############
    
    figura=Figure(figsize=(3,3.2), dpi=100)
    #Crea el grafico y configuración
    x1=figura.add_subplot(111, polar=True)
    
    
    ####circulo
    thetas=np.arange(0,361,10)
    m_thetas=[]
    r_thetas=[]
    
    for i in thetas:
        a=radianes(i)
        m_thetas.append(a)
        r_thetas.append(4)
    
    ##plotear circulo
    x1.plot(m_thetas, r_thetas,color='#804000', linewidth=1)
    
    ##plotear P y Q
    x1.annotate("", xy = (radianes(ang1_2), 4), xycoords = 'data',
                xytext = (radianes(ang1_2),10), textcoords = 'data',
                         arrowprops = dict(arrowstyle = "->"),fontsize=15)
    x1.annotate("", xy = (radianes(ang2_2), 4), xycoords = 'data',
                xytext = (radianes(ang2_2),10), textcoords = 'data',
                         arrowprops = dict(arrowstyle = "->"),fontsize=15)
    
    ##Nombres P y Q
    x1.text(0,0,"Túnel",color="#804000",fontsize=8,
            horizontalalignment='center', verticalalignment='center')
    x1.text(radianes(ang1_2),4,"P",color="blue",fontsize=12,
            horizontalalignment='left', verticalalignment='bottom')
    x1.text(radianes(ang2_2),4,"Q",color="magenta",fontsize=12,
            horizontalalignment='left', verticalalignment='bottom')
    
    #crear el area de dibujo
    x1.set_theta_zero_location("E")
    x1.set_theta_direction(1)
    x1.set_title("Corte en sección del Túnel", va="bottom")
    x1.set_rticks(np.arange(10,10,10))
    x1.set_rmax(10)
    x1.grid()
    canvas = FigureCanvasTkAgg(figura, master=ventana3) 
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    ########### Etiquetas y pantallas ########
    
    #etiquetas de resultados
    etiqueta1= Label(ventana3, text="Tensor en ejes Cartesianos (X,Y,Z)")
    etiqueta1.place(x=10,y=330)
    
    etiqueta3= Label(ventana3, text="S [XYZ]= ")
    etiqueta3.place(x=20,y=370)
    
    etiqueta5= Label(ventana3, text="Tensor en ejes del Túnel (X',Y',Z')")
    etiqueta5.place(x=10,y=410)
    
    etiqueta7= Label(ventana3, text="S [X'Y'Z']= ")
    etiqueta7.place(x=20,y=450)
    
    etiqueta8= Label(ventana3, text="Análisis en sección del túnel")
    etiqueta8.place(x=10,y=490)
    
    etiqueta9= Label(ventana3, text="P (Mpa)")
    etiqueta9.place(x=20,y=510)
    etiqueta10= Label(ventana3, text="Q (Mpa)")
    etiqueta10.place(x=20,y=530)
    
    etiqueta11= Label(ventana3, text="Ángulo P-X' (º)'")
    etiqueta11.place(x=135,y=510)
    etiqueta12= Label(ventana3, text="Ángulo Q-X' (º)'")
    etiqueta12.place(x=135,y=530)
    
    etiqueta12= Label(ventana3, text="P/Q")
    etiqueta12.place(x=20,y=550)
    
    
    ######## Resultados  ##########
    ## Sentencia de variables
    Parentesis1= StringVar()
    Parentesis1.set("[")
    Parentesis2= StringVar()
    Parentesis2.set("]")
    
    s_xyz_0_0= DoubleVar()
    s_xyz_0_1= DoubleVar()
    s_xyz_0_2= DoubleVar()
    s_xyz_1_0= DoubleVar()
    s_xyz_1_1= DoubleVar()
    s_xyz_1_2= DoubleVar()
    s_xyz_2_0= DoubleVar()
    s_xyz_2_1= DoubleVar()
    s_xyz_2_2= DoubleVar()
    
    s_xyz_0_0_t= DoubleVar()
    s_xyz_0_1_t= DoubleVar()
    s_xyz_0_2_t= DoubleVar()
    s_xyz_1_0_t= DoubleVar()
    s_xyz_1_1_t= DoubleVar()
    s_xyz_1_2_t= DoubleVar()
    s_xyz_2_0_t= DoubleVar()
    s_xyz_2_1_t= DoubleVar()
    s_xyz_2_2_t= DoubleVar()
    
    P_2_s=DoubleVar()
    Q_2_s=DoubleVar()
    P_Q_s=DoubleVar()
    
    ang1_s=DoubleVar()
    ang2_s=DoubleVar()
    
    ## redondear resultados
    s_xyz_2[0][0]=round(s_xyz_2[0][0],2)
    s_xyz_2[0][1]=round(s_xyz_2[0][1],2)
    s_xyz_2[0][2]=round(s_xyz_2[0][2],2)
    
    s_xyz_2[1][0]=round(s_xyz_2[1][0],2)
    s_xyz_2[1][1]=round(s_xyz_2[1][1],2)
    s_xyz_2[1][2]=round(s_xyz_2[1][2],2)
    
    s_xyz_2[2][0]=round(s_xyz_2[2][0],2)
    s_xyz_2[2][1]=round(s_xyz_2[2][1],2)
    s_xyz_2[2][2]=round(s_xyz_2[2][2],2)
    
    s_xyz_2_s[0][0]=round(s_xyz_2_s[0][0],2)
    s_xyz_2_s[0][1]=round(s_xyz_2_s[0][1],2)
    s_xyz_2_s[0][2]=round(s_xyz_2_s[0][2],2)
    
    s_xyz_2_s[1][0]=round(s_xyz_2_s[1][0],2)
    s_xyz_2_s[1][1]=round(s_xyz_2_s[1][1],2)
    s_xyz_2_s[1][2]=round(s_xyz_2_s[1][2],2)
    
    s_xyz_2_s[2][0]=round(s_xyz_2_s[2][0],2)
    s_xyz_2_s[2][1]=round(s_xyz_2_s[2][1],2)
    s_xyz_2_s[2][2]=round(s_xyz_2_s[2][2],2)
    
    P_2=round(P_2,2)
    Q_2=round(Q_2,2)
    P_Q_2=round(P_Q_2,2)
    
    ang1_2=round(ang1_2,2)
    ang2_2=round(ang2_2,2)
    
    ## resultados finales
    
    s_xyz_0_0.set(s_xyz_2[0][0])
    s_xyz_0_1.set(s_xyz_2[0][1])
    s_xyz_0_2.set(s_xyz_2[0][2])
    s_xyz_1_0.set(s_xyz_2[1][0])
    s_xyz_1_1.set(s_xyz_2[1][1])
    s_xyz_1_2.set(s_xyz_2[1][2])
    s_xyz_2_0.set(s_xyz_2[2][0])
    s_xyz_2_1.set(s_xyz_2[2][1])
    s_xyz_2_2.set(s_xyz_2[2][2])
    
    s_xyz_0_0_t.set(s_xyz_2_s[0][0])
    s_xyz_0_1_t.set(s_xyz_2_s[0][1])
    s_xyz_0_2_t.set(s_xyz_2_s[0][2])
    s_xyz_1_0_t.set(s_xyz_2_s[1][0])
    s_xyz_1_1_t.set(s_xyz_2_s[1][1])
    s_xyz_1_2_t.set(s_xyz_2_s[1][2])
    s_xyz_2_0_t.set(s_xyz_2_s[2][0])
    s_xyz_2_1_t.set(s_xyz_2_s[2][1])
    s_xyz_2_2_t.set(s_xyz_2_s[2][2])
    
    P_2_s.set(P_2)
    Q_2_s.set(Q_2)
    P_Q_s.set(P_Q_2)
    
    ang1_s.set(ang1_2)
    ang2_s.set(ang2_2)
    
    #pantallas de resultados
    pantalla1= Entry(ventana3, textvariable=Parentesis1, width=1,state="disable")
    pantalla1.place(x=70, y=350)
    pantalla2= Entry(ventana3, textvariable=s_xyz_0_0 ,width=6,state="disable")
    pantalla2.place(x=80, y=350)
    pantalla3= Entry(ventana3, textvariable=s_xyz_0_1 ,width=6,state="disable")
    pantalla3.place(x=115, y=350)
    pantalla4= Entry(ventana3, textvariable=s_xyz_0_2 ,width=6,state="disable")
    pantalla4.place(x=150, y=350)
    pantalla5= Entry(ventana3, textvariable=Parentesis2, width=1,state="disable")
    pantalla5.place(x=185, y=350)
    
    pantalla6= Entry(ventana3, textvariable=Parentesis1, width=1,state="disable")
    pantalla6.place(x=70, y=370)
    pantalla7= Entry(ventana3, textvariable=s_xyz_1_0, width=6,state="disable")
    pantalla7.place(x=80, y=370)
    pantalla8= Entry(ventana3, textvariable=s_xyz_1_1, width=6,state="disable")
    pantalla8.place(x=115, y=370)
    pantalla9= Entry(ventana3, textvariable=s_xyz_1_2, width=6,state="disable")
    pantalla9.place(x=150, y=370)
    pantalla10= Entry(ventana3, textvariable=Parentesis2, width=1,state="disable")
    pantalla10.place(x=185, y=370)
    
    pantalla11= Entry(ventana3, textvariable=Parentesis1, width=1,state="disable")
    pantalla11.place(x=70, y=390)
    pantalla12= Entry(ventana3, textvariable=s_xyz_2_0 , width=6,state="disable")
    pantalla12.place(x=80, y=390)
    pantalla13= Entry(ventana3, textvariable=s_xyz_2_1 ,width=6,state="disable")
    pantalla13.place(x=115, y=390)
    pantalla14= Entry(ventana3, textvariable=s_xyz_2_2 , width=6,state="disable")
    pantalla14.place(x=150, y=390)
    pantalla15= Entry(ventana3, textvariable=Parentesis2, width=1,state="disable")
    pantalla15.place(x=185, y=390)
    
    pantalla16= Entry(ventana3, textvariable=Parentesis1, width=1,state="disable")
    pantalla16.place(x=80, y=430)
    pantalla17= Entry(ventana3, textvariable=s_xyz_0_0_t , width=6,state="disable")
    pantalla17.place(x=90, y=430)
    pantalla18= Entry(ventana3, textvariable=s_xyz_0_1_t , width=6,state="disable")
    pantalla18.place(x=125, y=430)
    pantalla19= Entry(ventana3, textvariable=s_xyz_0_2_t , width=6,state="disable")
    pantalla19.place(x=160, y=430)
    pantalla20= Entry(ventana3, textvariable=Parentesis2, width=1,state="disable")
    pantalla20.place(x=195, y=430)
    
    pantalla21= Entry(ventana3, textvariable=Parentesis1, width=1,state="disable")
    pantalla21.place(x=80, y=450)
    pantalla22= Entry(ventana3, textvariable=s_xyz_1_0_t , width=6,state="disable")
    pantalla22.place(x=90, y=450)
    pantalla23= Entry(ventana3, textvariable=s_xyz_1_1_t , width=6,state="disable")
    pantalla23.place(x=125, y=450)
    pantalla24= Entry(ventana3, textvariable=s_xyz_1_2_t , width=6,state="disable")
    pantalla24.place(x=160, y=450)
    pantalla25= Entry(ventana3, textvariable=Parentesis2, width=1,state="disable")
    pantalla25.place(x=195, y=450)
    
    pantalla26= Entry(ventana3, textvariable=Parentesis1, width=1,state="disable")
    pantalla26.place(x=80, y=470)
    pantalla27= Entry(ventana3, textvariable=s_xyz_2_0_t , width=6,state="disable")
    pantalla27.place(x=90, y=470)
    pantalla28= Entry(ventana3, textvariable=s_xyz_2_1_t , width=6,state="disable")
    pantalla28.place(x=125, y=470)
    pantalla29= Entry(ventana3, textvariable=s_xyz_2_2_t , width=6,state="disable")
    pantalla29.place(x=160, y=470)
    pantalla30= Entry(ventana3, textvariable=Parentesis2, width=1,state="disable")
    pantalla30.place(x=195, y=470)
    
    pantalla31= Entry(ventana3, textvariable=P_2_s, width=8,state="disable")
    pantalla31.place(x=70, y=510)
    pantalla32= Entry(ventana3, textvariable=Q_2_s, width=8,state="disable")
    pantalla32.place(x=70, y=530)
    
    pantalla33= Entry(ventana3, textvariable=ang1_s, width=8,state="disable")
    pantalla33.place(x=230 , y=510)
    pantalla34= Entry(ventana3, textvariable=ang2_s, width=8,state="disable")
    pantalla34.place(x=230, y=530)
    
    pantalla35= Entry(ventana3, textvariable=P_Q_s, width=8,state="disable")
    pantalla35.place(x=70, y=550)
    

################## Ventana Resultado2 ##########################
def resultado3():
    ventana4=tk.Toplevel(ventana)
    ventana4.title("Resultado - Roseta de Anisitroía")
    ventana4.geometry("300x500")
    ventana4.resizable(0,0)
    
    ##### Convertir variables de entrada
    vs1_3 = float(vs1.get())
    vs2_3 = float(vs2.get())
    vs3_3 = float(vs3.get())
    as1_3 = float(as1.get())
    as2_3 = float(as2.get())
    as3_3 = float(as3.get())
    is1_3 = float(is1.get())
    is2_3 = float(is2.get())
    is3_3 = float(is3.get())
    trend_3=float(trend.get())
    plunge_3=float(plunge.get())
    
    ####### Funcion que permite calcular P/Q para un trend dado
    def anisotropia(ta):
        if as1_3<270:
            beta_s1=90-as1_3
        else:
            beta_s1=360+90-as1_3
        alfa_s1=is1_3
        
        if as2_3<270:
            beta_s2=90-as2_3
        else:
            beta_s2=360+90-as2_3
        alfa_s2=is2_3
        
        if as3_3<270:
            beta_s3=90-as3_3
        else:
            beta_s3=360+90-as3_3
        alfa_s3=is3_3
        
        #valores de matriz L
        l0_0 = np.cos(radianes(beta_s1))*np.cos(radianes(alfa_s1))
        l0_1 = np.sin(radianes(beta_s1))*np.cos(radianes(alfa_s1))
        l0_2 = np.sin(radianes(alfa_s1))
        
        l1_0 = np.cos(radianes(beta_s2))*np.cos(radianes(alfa_s2))
        l1_1 = np.sin(radianes(beta_s2))*np.cos(radianes(alfa_s2))
        l1_2 = np.sin(radianes(alfa_s2))
        
        l2_0 = np.cos(radianes(beta_s3))*np.cos(radianes(alfa_s3))
        l2_1 = np.sin(radianes(beta_s3))*np.cos(radianes(alfa_s3))
        l2_2 = np.sin(radianes(alfa_s3))
        
        ##matriz M
        m = np.array([[vs1_3,0,0],[0,vs2_3,0],[0,0,vs3_3]],float)
        #Matriz L
        l= np.array([[l0_0,l0_1,l0_2],[l1_0,l1_1,l1_2],[l2_0,l2_1,l2_2]],float)
        #Matriz L transpuesta
        l_t=np.transpose(l)
        
        ### tensor de esfuerzo en XYZ
        s_xyz=np.matmul((np.matmul(l_t,m)),l)
        
        ####### Rotación de esfuerzo
        #### Modificaciones, calculo de auxiliares
        td1=ta+90
        pd1=0
        td2=ta
        td3=ta
        pd2=plunge_3
        pd3=plunge_3+90
        
        #obtener beta y delta para matriz de cosenos directores
        if td1<270:
            beta2_s1=90-td1
        else:
            beta2_s1=360+90-td1
        alfa2_s1=pd1
        
        if td2<270:
            beta2_s2=90-td2
        else:
            beta2_s2=360+90-td2
        alfa2_s2=pd2
        
        if td3<270:
            beta2_s3=90-td3
        else:
            beta2_s3=360+90-td3
        alfa2_s3=pd3
        
        #valores de matriz L
        l0_0_2 = np.cos(radianes(beta2_s1))*np.cos(radianes(alfa2_s1))
        l0_1_2 = np.sin(radianes(beta2_s1))*np.cos(radianes(alfa2_s1))
        l0_2_2 = np.sin(radianes(alfa2_s1))
        
        l1_0_2 = np.cos(radianes(beta2_s2))*np.cos(radianes(alfa2_s2))
        l1_1_2 = np.sin(radianes(beta2_s2))*np.cos(radianes(alfa2_s2))
        l1_2_2 = np.sin(radianes(alfa2_s2))
        
        l2_0_2 = np.cos(radianes(beta2_s3))*np.cos(radianes(alfa2_s3))
        l2_1_2 = np.sin(radianes(beta2_s3))*np.cos(radianes(alfa2_s3))
        l2_2_2 = np.sin(radianes(alfa2_s3))
        
        ##matriz M
        m_2 = s_xyz
        #Matriz L
        l_2= np.array([[l0_0_2,l0_1_2,l0_2_2],[l1_0_2,l1_1_2,l1_2_2],[l2_0_2,l2_1_2,l2_2_2]],float)
        #Matriz L transpuesta
        l_t_2=np.transpose(l_2)
        
        ### tensor de esfuerzo en XYZ
        s_xyz_2=np.matmul((np.matmul(l_2,m_2)),l_t_2)
        
        ### calculo para P y Q
        sxx=s_xyz_2[0][0]
        szz=s_xyz_2[2][2]
        sxz=s_xyz_2[0][2]
        szx=s_xyz_2[2][0]
        lmda=(np.arctan((2*sxz/(sxx-szz))))*180/np.pi
        
        #Sacar P y Q
        P= ((sxx+szz)/2)+(((1/4)*((sxx-szz)**2))+(sxz**2))**(1/2)
        Q=((sxx+szz)/2)-(((1/4)*((sxx-szz)**2))+(sxz**2))**(1/2)
        return P/Q
    
    ###### obtener todas las anisotropias para cada angulo #####
    thetas_3=np.arange(0,361,1)
    m_thetas_3=[]
    r_thetas_3=[]
    a1=[]
    a2=[]
    
    for i in thetas_3:
        g= anisotropia(i)
        an = radianes(i)
        m_thetas_3.append(an)
        r_thetas_3.append(g)
        
    PQ_min=(min(r_thetas_3))
    PQ_max=(max(r_thetas_3))
    PQ_t=anisotropia(trend_3)
    
    ##### Obtener angulos donde se encuentran PQ max y min ####
    
    ang_min=(list(m_thetas_3)[list(r_thetas_3).index(PQ_min)])
    ang_max=(list(m_thetas_3)[list(r_thetas_3).index(PQ_max)])
    
    ang_min_grados= ang_min*180/np.pi
    ang_max_grados= ang_max*180/np.pi
    
    ######## Identificar cuadrantes ###########
    def cuadrante(angu):
        if angu == 0 or angu == 180 or angu == 360:
            result= "N-S"
        elif angu>0 and angu<90:
            result= "N " + str(angu) + "(º) ""E"
        elif angu == 90 or angu == 270:
            result= "E-O"
        elif angu>90 and angu<180:
            angu=180-angu
            result= "S "+ str(angu)+ "(º) ""E"
        elif angu>180 and angu<270:
            angu=angu-180
            result= "S "+ str(angu)+ "(º) ""O"
        elif angu>270 and angu<360:
            angu=360-angu
            result= "N "+ str(angu)+ "(º) ""O"
        return result
    
    resu1= cuadrante(ang_min_grados)
    resu2= cuadrante(ang_max_grados)
    resu3= cuadrante(trend_3) 
    
    #### Datos para plotear túnel ######
    a_t=[0,radianes(trend_3)]
    b_t=[0,round(PQ_max,0)+1]
    c_t=[0,radianes(trend_3+180)]
    d_t=[0,round(PQ_max,0)+1]
    
    ###plotear mejor caso
    a_b=[0,ang_min]
    b_b=[0,round(PQ_max,0)+1]
    c_b=[0,ang_min+radianes(180)]
    d_b=[0,round(PQ_max,0)+1]
    
    ###plotear peor caso
    a_w=[0,ang_max]
    b_w=[0,round(PQ_max,0)+1]
    c_w=[0,ang_max+radianes(180)]
    d_w=[0,round(PQ_max,0)+1]
    
    figura=Figure(figsize=(3,3.2), dpi=100)
    #Crea el grafico y configuración
    x1=figura.add_subplot(111, polar=True)
    
    ##### Ploteo ######
    ## datos P/Q ##
    x1.plot(m_thetas_3, r_thetas_3,color='blue', linewidth=1)
    
    ##plotear túnel
    x1.plot(a_t,b_t,color="#804000", linewidth=2.5)
    x1.plot(c_t, d_t, color='#804000', linewidth=2.5)
    x1.text(radianes(trend_3),round(PQ_max,0)+1,"Túnel",color='#804000',fontsize=8,
            horizontalalignment='right', verticalalignment='bottom')
    
    ##Plotear mejor caso
    x1.plot(a_b,b_b,color="g",linestyle = '--', linewidth=1)
    x1.plot(c_b,d_b, color='g',linestyle = '--', linewidth=1)
    x1.text(ang_min,round(PQ_max,0)+1,"B-DIR",color='g',fontsize=8,
            horizontalalignment='right', verticalalignment='bottom')
    
    ##Plotear peor caso
    x1.plot(a_w,b_w,color="r",linestyle = '--', linewidth=1)
    x1.plot(c_w,d_w, color='r',linestyle = '--', linewidth=1)
    x1.text(ang_max,round(PQ_max,0)+1,"W-DIR",color='r',fontsize=8,
            horizontalalignment='right', verticalalignment='bottom')
    
    x1.set_theta_zero_location("N")
    x1.set_theta_direction(-1)
    x1.set_title("Relación P/Q - Dirección", va='bottom')
    x1.set_rticks(np.arange(0,round(PQ_max,0)+1,1.0))
    x1.set_rmax(round(PQ_max,0)+1)
    x1.grid(True)
    #crear el area de dibujo
    canvas = FigureCanvasTkAgg(figura, master=ventana4)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    ########### Etiquetas y pantallas ########
    
    #etiquetas de resultados
    etiqueta1= Label(ventana4, text="La dirección actual del túnel es: ")
    etiqueta1.place(x=10,y=330)
    etiqueta2= Label(ventana4, text="Con un índice P/Q igual a: ")
    etiqueta2.place(x=10,y=350)
    
    etiqueta3= Label(ventana4, text="La mejor dirección para el túnel es: ")
    etiqueta3.place(x=10,y=380)
    etiqueta4= Label(ventana4, text="Con un índice P/Q igual a: ")
    etiqueta4.place(x=10,y=400)
    
    etiqueta5= Label(ventana4, text="La peor dirección para el túnel es: ")
    etiqueta5.place(x=10,y=430)
    etiqueta6= Label(ventana4, text="Con un índice P/Q igual a: ")
    etiqueta6.place(x=10,y=450)
    
    #### Resultados #####
    #Sentencia de variables
    resu_3_p = StringVar()
    resu_3_p.set(resu3)
    
    PQ_t_p=DoubleVar()
    PQ_t_p.set(round(PQ_t,2))
    
    resu_1_p= StringVar()
    resu_1_p.set(resu1)
    
    PQ_min_p=DoubleVar()
    PQ_min_p.set(round(PQ_min,2))
    
    resu_2_p= StringVar()
    resu_2_p.set(resu2)
    
    PQ_max_p=DoubleVar()
    PQ_max_p.set(round(PQ_max,2))
    
    #Pantallas de resultados
    pantalla1= Entry(ventana4, textvariable=resu_3_p, width=10,state="disable")
    pantalla1.place(x=200, y=330)
    pantalla2= Entry(ventana4, textvariable=PQ_t_p, width=6,state="disable")
    pantalla2.place(x=200, y=350)
    
    pantalla3= Entry(ventana4, textvariable=resu_1_p, width=10,state="disable")
    pantalla3.place(x=200, y=380)
    pantalla4= Entry(ventana4, textvariable=PQ_min_p, width=6,state="disable")
    pantalla4.place(x=200, y=400)
    
    pantalla5= Entry(ventana4, textvariable=resu_2_p, width=10,state="disable")
    pantalla5.place(x=200, y=430)
    pantalla6= Entry(ventana4, textvariable=PQ_max_p, width=6,state="disable")
    pantalla6.place(x=200, y=450)
    
################# Edición Ventana Principal #####################

#funcion clear
def clear():
    vs1.set(" ")
    vs2.set(" ")
    vs3.set(" ")
    as1.set(" ")
    as2.set(" ")
    as3.set(" ")
    is1.set(" ")
    is2.set(" ")
    is3.set(" ")
    trend.set(" ")
    plunge.set(" ")
    
#control de variables de entrada
vs1=DoubleVar()
vs2=DoubleVar()
vs3=DoubleVar()
as1=DoubleVar()
as2=DoubleVar()
as3=DoubleVar()
is1=DoubleVar()
is2=DoubleVar()
is3=DoubleVar()
trend=DoubleVar()
plunge=DoubleVar()

vs1.set(" ")
vs2.set(" ")
vs3.set(" ")
as1.set(" ")
as2.set(" ")
as3.set(" ")
is1.set(" ")
is2.set(" ")
is3.set(" ")
trend.set(" ")
plunge.set(" ")

#Etiquetas
etiqueta1= Label(ventana, text="Información Tensor de Esfuerzos")
etiqueta1.place(x=10,y=10)

etiqueta2= Label(ventana, text= "ESF")
etiqueta2.place(x=20, y=40)

etiqueta3= Label(ventana, text="S1")
etiqueta3.place(x=20, y=60)

etiqueta4= Label(ventana, text="S2")
etiqueta4.place(x=20, y=80)

etiqueta5= Label(ventana, text="S3")
etiqueta5.place(x=20, y=100)

etiqueta6= Label(ventana, text="Valor (Mpa)")
etiqueta6.place(x=50, y=40)

etiqueta7= Label(ventana, text="Azimut (º)")
etiqueta7.place(x=120, y=40)

etiqueta8= Label(ventana, text="Inclinación (º)")
etiqueta8.place(x=190, y=40)

etiqueta9= Label(ventana, text="Información del Túnel")
etiqueta9.place(x=10,y=140)

etiqueta10= Label(ventana, text="Trend (º)")
etiqueta10.place(x=20,y=160)

etiqueta11= Label(ventana, text="Plunge (º)")
etiqueta11.place(x=20,y=180)

etiqueta12= Label(ventana, text="Opciónes de Cálculo")
etiqueta12.place(x=10,y=210)

etiqueta17= Label(ventana, text= "Creado por: ERIK TRINCADO CABEZAS")
etiqueta17.place(x=70, y=350)

#ventanas de entrada
##Valores esfuerzos
entrada1= Entry(textvariable=vs1, width=10)
entrada1.place(x=50,y=60)

entrada2= Entry(textvariable=vs2, width=10)
entrada2.place(x=50, y=80)

entrada3= Entry(textvariable=vs3, width=10)
entrada3.place(x=50, y=100)

##Azimut
entrada4= Entry(textvariable=as1, width=10)
entrada4.place(x=120, y=60)

entrada5= Entry(textvariable=as2, width=10)
entrada5.place(x=120, y=80)

entrada6= Entry(textvariable=as3, width=10)
entrada6.place(x=120, y=100)

##Inclinción
entrada7= Entry(textvariable=is1, width=10)
entrada7.place(x=190, y=60)

entrada8= Entry(textvariable=is2, width=10)
entrada8.place(x=190, y=80)

entrada9= Entry(textvariable=is3, width=10)
entrada9.place(x=190, y=100)

##Túnel
entrada10= Entry(textvariable=trend, width=10)
entrada10.place(x=80, y=160)

entrada11= Entry(textvariable=plunge, width=10)
entrada11.place(x=80, y=180)

#Creación de Botones
calcular= Button(ventana, text="Verificación Vectorial", width=16, command=resultado1)
calcular.place(x=70, y=240)
calcular= Button(ventana, text="Rotación de Tensor", width=16,command=resultado2)
calcular.place(x=70, y=270)
calcular= Button(ventana, text="Roseta de Anisotripía", width=16,command=resultado3)
calcular.place(x=70, y=300)


limpiar= Button(ventana, text="Limpiar", command= clear)
limpiar.place(x=170, y=165)


ventana.mainloop()