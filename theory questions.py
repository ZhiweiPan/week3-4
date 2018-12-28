"""
1.
-(1)
      (a)I want to see a movie
      (b)I have enough money to buy a movie ticket
- (2.) role:
      I,the conductor,the projector,the doorman
- (3.) props:
    Movie tickets,chairs,projection equipment(screens, video cameras), money
- (4.)the scene:
    Scene one: buy a ticket
      (a)I walked to the ticket office and take out the money to the conductor.
      (b)the conductor took the money and gave me a movie ticket.
   Scene two: go to the cinema
      (a)I took the ticket, walked into the entrance, and took out the ticket for the doorman.
      (b)the doorman let me in.
  Scene three: waiting for the movie to start, I find my seat and sit down.
  Scene four: see a movie
      (a)the movie started
      (b)I was deeply attracted by the story and absorbed in the movie.
  Scene five: The film is finished
      (a)the film is over
      (b)I left the cinema with others.
- (5.)results
    (a.)I had a good mood
    (b)I spent the money
- (C.)the cinema earned money.

2.
 Initial State
- (1) Farmer takes duck to left bank
- (2) Farmer returns alone to right bank
- (3) Farmer takes wolf to left bank
- (4) Farmer returns with duck
- (5) Farmer takes corn to left bank
- (6) Farmer returns alone
- (7) Farmer takes duck to left bank
- (8) Success

3.
In goal formulation, we decide which aspects of the world we are interested in, and which can be ignored or abstracted away. Then in problem formulation we decide how to manipulate the important aspects (and ignore the others). If we did problem formulation first we would not know what to include and what to leave out. That said, it can happen that there is a cycle of iterations between goal formulation, problem formulation, and problem solving until one arrives at a sufficiently useful and efficient solution.

4.
- 1\.BFS(there are used right hand rule .Maybe you can ues the left hand rule).
    A:[B]
    B:[C,D]
    C:[D,E,F]
    D:[E,F,H,G]
    E:[F,H,G]
    F:[H,G]
    H:[G,K,I]
    G:[K,I]
    K=goal
- 2\. DFS(there are used right hand rule .Maybe you can ues the left hand rule).
    A:[B]
    B:[C,D]
    C:[E,G,D]
    E:[F,D]
    F:[D]
    D:[H,G]
    H:[I,K,G]
    I=goal

5.
2. Breadth-first: 1 2 3 4 5 6 7 8 9 10 11.
   Depth-limited: 1 2 4 8 9 5 10 11.
   Iterative deepening: 1;   1 2 3;   1 2 4 5 3 6 7;  1 2 4 8 9 5 10 11
3. Bidirectional search is very useful, because the only successor of n in the reverse direction is ⌊(n/2)⌋. This helps focus the search. The branching factor is 2 in the forward  direction; 1 in the reverse direction.
4. Yes; start at the goal, and apply the single reverse successor action until you reach 1.
5. The solution can be read off the binary numeral for the goal number. Write the goal number in binary. Since we can only reach positive integers, this binary expansion beings with a 1.  From  most- to least- significant bit, skipping the initial 1, go Left to the node 2n if this bit is 0 and go Right to node 2n + 1 if it is 1. For example, suppose the goal is 11, which is 1011 in binary. The solution is therefore Left, Right, Right.
"""