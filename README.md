# Math127Project1
Neighbor Joining algorithm and graph visualization software for Phylogenetic Project

Repository tree as of now: <br/> 

/Math127 <br/>
&nbsp;&nbsp;/algorithms <br/>
    &nbsp;&nbsp;"Holds the algorithms for the project"<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;-Makefile<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;-"GNU Makefile to automate testing"<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;-mutate.py<br/> 
        &nbsp;&nbsp;&nbsp;&nbsp;"Jukes Cantor mutation model"<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;-neighborJoining.py<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"Neighbor Joining algoithm"<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;-Test.py<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"Unit tests for our classes"<br/>
&nbsp;&nbsp;/Simulations</br>
    &nbsp;&nbsp;"Simulations of Thread Effeciency"<br/>


To run the testing suite for this repo, cd into the algorithms folder and run "make test".

To test the effeciency of mutate over threads, change the permission of mutate_simulations.sh (chmod u+x mutate_simulations.sh). Then run the script. It will create a repository "simulations" with csv files logging the simulation.
    