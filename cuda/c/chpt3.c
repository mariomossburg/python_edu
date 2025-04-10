// intro to Cuda


// Note: make sure correct compiler...
// Need a compiler for cpu and gpu


#include <stdio.h>

__global__ void kernal(void){
}

int main(void) {
    kernal<<<1,1>>>():
    printf('hello, world!\n');
    return 0
}


// passing parameters
__global__ void add(int a, int b, int *c){
    *c = a + b;
}

int main(void) {
    int c;
    int *dev_c;
    HANDLE_ERROR ( cudaMalloc( (void**)&dev_c, sizeof(int) ) );

    add<<<1,1>>>(2, 7, dev_c);

    HANDLE_ERROR( cudaMemcpy(&c, 
                             dev_c,
                             sizeof(int), 
                             cudaMemcpyDeviceToHost ) );
    

    printf("2 + 7 = %d\n", c);
    cudaFree(dev_c);

    return 0;
}


// querying devices... page 57-59
// int count;
// HANDLE_ERROR ( cudaMalloc( cudaGetDeviceCount( &count));







// Last example of chapter
#include "../common/book.h"

int main( void ) {
    cudaDeviceProp prop;

    int count;
    HANDLE_ERROR( cudaGetDeviceCount( &count ) );
    for (int i=0; i< count; i++) {
        HANDLE_ERROR( cudaGetDeviceProperties( &prop, i ) );
        printf("--- General Information for device %d ---\n", i );
        printf("Name: %s\n", prop.name );
        printf("Compute capability: %d.%d\n", prop.major, prop.minor );
        printf("Clock rate: %d\n", prop.clockRate );
        printf("Device copy overlap: ");
        if (prop.deviceOverlap)
            printf("Enabled\n");
        else
            printf("Disabled\n");
        printf("Kernel execution timeout: ");
        if (prop.kernelExecTimeoutEnabled)
            printf("Enabled\n");
        else
            printf("Disabled\n");

        printf("--- Memory Information for device %d ---\n", i );
        printf("Total global mem: %ld\n", prop.totalGlobalMem );
        printf("Total constant Mem: %ld\n", prop.totalConstMem );
        printf("Max mem pitch: %ld\n", prop.memPitch );
        printf("Texture Alignment: %ld\n", prop.textureAlignment);
        printf(" --- MP Information for device %d ---\n", i );
        printf("Multiprocessor count: %d\n", prop.multiProcessorCount );
        printf("Shared mem per mp: %ld\n", prop.sharedMemPerBlock );
        printf("Registers per mp: %d\n", prop.regsPerBlock );
        printf("Threads in warp: %d\n", prop.warpSize );
        printf("Max threads per block: %d\n", prop.maxThreadsPerBlock );

        printf("Max thread dimensions: {%d, %d, %d}\n",
            prop.maxThreadsDim[0], prop.maxThreadsDim[1],
            prop.maxThreadsDim[2] );
        printf("Max grid dimensions: {%d, %d, %d}\n",
            prop.maxGridSize[0], prop.maxGridSize[1],
            prop.maxGridSize[2] );
        printf("\n");
    }
}