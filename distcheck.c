#include "data.h"
#include <stdio.h>

#ifdef ARRAY_OF_STRUCTS
double 
distcheck(particle_t *p, int n) {

    double dist = -99.0;
    /* fill in your code here
     *
     */
    for(int i = 0; i < n; i++){
        dist += p[i].dist;
        //printf("distance %f",dist);
    }
    return dist;
}
#else
double 
distcheck(particle_t p, int n) {

    double dist = -99.0;
    /* fill in your code here
     *
     */
    for(int i = 0; i < n; i++) {
        dist += p.dist[i];
       //printf("distance %f",dist);
    }
    return dist;
}
#endif
