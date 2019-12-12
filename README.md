# Graph Creator

Simple program built in Python 2.7 that does the following:
* Takes as input a series of commands that describe streets
* Uses the input to construct a particular kind of undirected graph as defined further below


## Sample Input

There are 4 commands available:
1. Add a street
2. Change a street
3. Remove a street
4. Generate a graph

Sample run below:
```
a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)
a "King Street S" (4,2) (4,8)
a "Davenport Road" (1,4) (5,8)
g
V = {
1: (2,2)
2: (4,2)
3: (4,4)
4: (5,5)
5: (1,4)
6: (4,7)
7: (5,6)
8: (5,8)
}
E = {
   <1,3>,
   <2,3>,
   <3,4>,
   <3,6>,
   <7,6>,
   <6,5>,
   <9,6>,
   <6,8>,
   <6,10>
}
c "Weber Street" (2,1) (2,2)
g
V = {
   1: (4,2)
   2: (1,4)
   3: (4,7)
   4: (5,8)
   5: (4,8)
}
E = {
   <2,6>,
   <6,5>,
   <6,8>,
   <6,10>
}
r "King Street S"
g
V = {
}
E = {
}
```
## Commands
* ```a``` is used to add a street. It is specified as: ```a "Street Name" (x1,y1) (x2,y2)...(x_n,y_n)```. Each *(x_i,y_i)* is a coordinate. The coordinates are interpreted as a polu-line segment.
* `c` is used to change the specification of a street. It's format is the same as for 'a'. It is interpreted as a new specification for a street that has already been specified.
* `r` is used to remove a street. It is specified as `r "Street Name"`
* `g` causes the program to ouput the corresponding graph

## Input and output
The program takes input from standard input and output is sent to standard putput. Errors are sent to standard error.

## Output Graph
A point on the graph is a vertex if any of the following is true:
1. It is an intersection between line segments
2. It is the end-point of a line segment of a street that intersects with another street.

An example of (1) from the above run example is vertex 3. An example of (2) is vertex 1.

There is an edge between two vertices if:
* At least one of them is an intersection
* Both lie on the same street, and
* One is reachable from the other without traversing another vertex
