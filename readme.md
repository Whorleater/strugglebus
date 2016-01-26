# strugglebus - a really simple journaling app
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
    
    -- entry #
       |--- date
       |--- struggle
       |--- why?
       |--- solved?

#### Why?
I've always been terrible at journaling, mostly because I find that I try to go too far in depth and write too much. This is my attempt to summarize my day by listing the biggest struggle I had that day. 

#### Roadmap
- [x] Build the application
- [ ] Allow adding of struggles from previous dates
- [x] Allow the renaming of journal files?
- [ ] Remind at specific times 
- [ ] Only allow journaling at specific times? 
- [ ] Set up tags
- [ ] Set up some form of analytics
- [ ] Difficulty of struggle
- [ ] Convert to csv
- [ ] Move to a webapp? 
- [ ] Entries from phone?