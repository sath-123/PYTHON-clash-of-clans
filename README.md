Q1)
code is written in c.
Time complexity:((N*M)*K/size)
here size=number of processors

Message complexity: 2(p-1)*(N*M/p) ,(p-1)(N*M)/p for sending input to each processor and receving answer from each proccesor

space complexity: 2*N*M for root process,one is for input other is for storing computed values
-> 2(N*M)/p for remaining procssese,one (N*M)/p is for storing values,and other for computed answers

performance : considered input as 30 30 10000
1 process Total time (s): 4.688960
2 Total time (s): 3.311700
3 Total time (s): 3.065280
4 Total time (s): 2.926174
5 Total time (s): 2.316099
6 Total time (s): 2.945268
7 Total time (s): 2.972469
8 Total time (s): 3.221441
9 Total time (s): 3.482193
10 Total time (s): 3.699775
11 Total time (s): 3.712265
12 Total time (s): 3.909257

Q2) code is written in c++.
Time complexity : (K*T)/p,for ecah process

space complexity: K+N*(M/p)+somemore ,here K is for storing the vector of k struct ,and N*(M/p) to store the counts of particles in each place ,and something is for storing the map values to finding collisons
for child proccess K will be reduced.K*log(K )for sorting the final values in root process.

message complexity: thsi depends on how the particles moving between the proccessors so we can't exactly tell how much is the message complexity between 2 proccessors.

performance : considered iput 100 120 16 1000

2 Total time (s): 7.456329
3 Total time (s): 6.050313
4 Total time (s): 8.096125
5 Total time (s): 7.64096
6 Total time (s): 7.032178
11 Total time (s): 8.229354
12 Total time (s): 8.525119

Q3) code is written in c

Time complexity : N*N*(N/p) approximately

space complexity: 2*N*N + 2*N  for rroot process. one N*N is for storing cost values and other is for storing parent(x,y) and 2*N is for input. N*N + N is for child ,because N*N for storing cost(x,y) and N is storing the frequencies of keys.

message complexity : 2*(2*N)/p+N+reduce messages
2(2*N)/p is for sending the input and collecting the output sorted part of input and N is for sending freq array.

performance : considered input N=500
2 Total time (s): 5.695705
3 Total time (s): 4.710292
4 Total time (s): 3.659714
5 Total time (s): 3.318716
6 Total time (s): 4.364928
7 Total time (s): 5.131445
8 Total time (s): 5.468585
9 Total time (s): 7.155930
10 Total time (s): 7.701772
11 Total time (s): 7.673195
12 Total time (s): 7.951062





            