# Project 4:  Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax

## ACP controle times

That's "controle" with an 'e', because it's French, although "control"
is also accepted.  Controls are points where   
a rider must obtain proof of passage, and control[e] times are the
minimum and maximum times by which the rider must  
arrive at the location.   

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html . The description is ambiguous,
but the examples help.  Part of finishing this project is clarifying
anything that is not clear about the requirements, and documenting it
clearly.  

We are essentially replacing the calculator at
https://rusa.org/octime_acp.html .  We can also use that calculator
to clarify requirements and develop test data.  

## AJAX and Flask reimplementation

The current RUSA controle time calculator is a Perl script that takes
an HTML form and emits a text page. The reimplementation will fill in
times as the input fields are filled.  Each time a distance is filled
in, the corresponding open and close times should be filled in.   


## To run automated tests 
* `nosetests`

There are currently nose tests only for acp_times.py. 

## How to Run the Code
```
  git clone  YourRepositoryURL myTestArea
  cd myTestArea
  bash ./configure
  make test    # All tests should pass
  make service # Then I test from browser on another machine
```

If you have issues with the service you can stop the service by typing the following:
```
ps -e | grep gunicorn #Find the PID for gunicorn
kill -9 pid #where pid is the process id returned by the last command
make service
```
