#include "data.h"
#include <math.h>

#ifdef ARRAY_OF_STRUCTS
double 
distance(particle_t *p, int n) {
    
    double dist = -99.0;
    /* fill in your code here
     *
     */
    for(int i = 0; i < n; i++){
        dist = p[i].x*p[i].x + p[i].y*p[i].y + p[i].z*p[i].z;
        p[i].dist = sqrt(dist);
        dist += p[i].dist;
    }

    return dist;
}
#else
double 
distance(particle_t p, int n) {

    double dist = -99.0;
    /* fill in your code here
     *
     */
    for(int i=0; i < n; i++){
        dist = p.x[i]*p.x[i] + p.y[i]*p.y[i] + p.z[i]*p.z[i];
        p.dist[i] = sqrt(dist);
        dist += p.dist[i];

    }

    return dist;
}
#endif
