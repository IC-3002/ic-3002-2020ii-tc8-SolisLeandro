def contar_rutas_mas_cortas(C):
    cont=[]
    aux_contar_rutas(C,0,0,1,((len(C[0]))+(len(C)))-1,cont)
    return len(cont)

def aux_contar_rutas(arr,x,y,cantMovimientos,limiteMov,cont):
    if(cantMovimientos<limiteMov):
        arr[y][x]=2
        if(canMove(arr,1,len(arr[0])-1, len(arr)-1,x,y)):
            aux_contar_rutas(arr,x+1,y,cantMovimientos+1,limiteMov,cont)
        if(canMove(arr,2,len(arr[0])-1, len(arr)-1,x,y)):
            aux_contar_rutas(arr,x-1,y,cantMovimientos+1,limiteMov,cont)
        if(canMove(arr,3,len(arr[0])-1, len(arr)-1,x,y)):
            aux_contar_rutas(arr,x,y-1,cantMovimientos+1,limiteMov,cont)
        if(canMove(arr,4,len(arr[0])-1, len(arr)-1,x,y)):
            aux_contar_rutas(arr,x,y+1,cantMovimientos+1,limiteMov,cont)
    else:
        if(x==len(arr[0])-1 and y==len(arr)-1):
            cont.append(1)
    arr[y][x]=0

def canMove(arr,direccion,limiteDerecho, limiteAbajo,x,y): #direccion: 1=derecha,2=izquierda,3=arriba,4=abajo
    if(direccion==1):
        if(x<limiteDerecho):    #ver si no supero el limite
            if(arr[y][x+1]==0):  #ver si puedo ir a la derecha
                return True
    if(direccion==2):
        if(x>0):                #ver si no supero el limite
            if(arr[y][x-1]==0):  #ver si puedo ir a la izquierda
                return True
    if(direccion==3):
        if(y>0):                #ver si no supero el limite
            if(arr[y-1][x]==0):  #ver si puedo ir a la arriba
                return True
    if(direccion==4):
        if(y<limiteAbajo):      #ver si no supero el limite
            if(arr[y+1][x]==0):  #ver si puedo ir a la abajo
                return True
