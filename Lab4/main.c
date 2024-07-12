#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

//Declaración de los prototipos de nuestras funciones
extern void rxy_ASM(float mediaX,float mediaY,float *x,float *y,int N,float *rxy);
void ini_vector_X(float *arreglo,int N);
void ini_vector_Y(float *arreglo,int N);
float calculo_media(float *arreglo,int N);
void rxy_C(float mediaX,float mediaY,float *x,float *y,int N,float *rxy);


int main(int argc, char const *argv[]){

    //Semilla para los numeroa aleatorios
    srandom(time(NULL));

    //Declaramos los vectores, y las variables donde se almacenará el producto interno en C y ASM
    float *X,*Y,med_X,med_Y,rxy_c,rxy_asm;

    //Declaramos el valor de N que será ingresado por terminal
    int N=atoi(argv[1]);

    //Reservamos espacio de memoria para los dos arreglos float
    X=malloc(N*sizeof(float));
    Y=malloc(N*sizeof(float));

    //Inicializamos ambos arreglos
    ini_vector_X(X,N);
    ini_vector_Y(Y,N);

    //Hallamos la media de ambos arreglos
    med_X=calculo_media(X,N);
    med_Y=calculo_media(Y,N);

    
   //Se declaran dos variables de tipo struct
    //struct timespec es una estructura que tiene dos miembros: tv_sec, tv_nsec
    struct timespec ti,tf;

    //Declaramos la variable
    double elapsed;

    //Medimos el tiempo en que tarde ejecutarse la función rxy_C(en C)
    clock_gettime(CLOCK_REALTIME, &ti);
    rxy_C(med_X,med_Y,X,Y,N,&rxy_c);
    clock_gettime(CLOCK_REALTIME, &tf);
    elapsed = (tf.tv_sec - ti.tv_sec) * 1e6 + (tf.tv_nsec - ti.tv_nsec);
    printf("El tiempo en microsegundos que toma la función en C es %lf\n", elapsed);

    //Medimos el tiempo en que tarde ejecutarse la función rxy_ASM(en ASM)
    clock_gettime(CLOCK_REALTIME, &ti);
    rxy_ASM(med_X,med_Y,X,Y,N,&rxy_asm);
    clock_gettime(CLOCK_REALTIME, &tf);
    elapsed = (tf.tv_sec - ti.tv_sec) * 1e6 + (tf.tv_nsec - ti.tv_nsec);
    printf("El tiempo en microsegundos que toma la función en ASM es %lf\n", elapsed); 


    return 0;
}
void ini_vector_X(float *arreglo,int N){
    for(int i=0;i<N;i++){
        float e=-20+random()%41; //Genera numeros aleatorios entre -20 a 20
        arreglo[i]=e;
    }
}

void ini_vector_Y(float *arreglo,int N){
    for(int i=0;i<N;i++){
        float e=random()%51; //Genera numeros aleatorios entre 0 a 50
        arreglo[i]=e;
    }
}
float calculo_media(float *arreglo,int N){
    float suma=0,media;
    for(int i=0;i<N;i++){
        suma=suma+arreglo[i];
    }
    media=suma/N;
    return media;
}
void rxy_C(float mediaX,float mediaY,float *x,float *y,int N,float *rxy){
    float a,b,suma_den1=0,suma_den2=0,suma_num=0,den;
    for(int i=0;i<N;i++){
        a=x[i]-mediaX;
        b=y[i]-mediaY;
        suma_num=suma_num+(a*b);
        suma_den1=suma_den1+(a*a);
        suma_den2=suma_den2+(b*b);
        den=sqrt(suma_den1)*sqrt(suma_den2);
    }
    rxy[0]=suma_num/den;
    printf("El resultado es: %f\r\n",rxy[0]);
}