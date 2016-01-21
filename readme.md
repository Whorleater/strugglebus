# strugglebus - a really terrible journaling app
strugglebus is a command line journaling app that asks you of only one main thing per day: "what was today's struggles?" 

### How?
1. `python strugglebus.py`
2. Answer the questions:
    1. What was your biggest struggle of today?
    2. Why did you have that struggle?
    3. Did you solve it today?
3. Done.

### Tech details: 
strugglebus writes everything to a giant json file named `strugglebus.json`. Not pretty, but you can track it with versioning, and it's pretty easy to unravel if you want the data later on. 
json format:
    
    -- date
       |--- struggle
       |--- why?
       |--- solved?

#### Why?
I've always been terrible at journaling, mostly because I find that I try to go too far in depth and write too much. This is my attempt to summarize my day by listing the biggest struggle I had that day. 

#### Roadmap
[] Build the application
[] Allow adding of struggles from previous dates
[] Set up tags
[] Set up some form of analytics
[] Move to a webapp? 